import urlparse

from scrapy.conf import settings
from scrapy.core.exceptions import NotConfigured
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.utils.url import urljoin_rfc

from ocw.items import MaterialItemLoader


class MaterialsSpider(BaseSpider):
    name = 'materials'
    allowed_domains = ['ocw.mit.edu']

    WORD_RE = r'[\w\-]+'
    # /courses/<department>/<course-id>
    COURSE_LINK_RE = r'/courses/%s/%s/?$' % (WORD_RE, WORD_RE)
    COURSE_LINK_XPATH = '//div[@class="course_detail"]'

    course_le = SgmlLinkExtractor(allow=COURSE_LINK_RE, restrict_xpaths=COURSE_LINK_XPATH)

    _department_url = 'http://ocw.mit.edu/courses/%s/'

    def department_url(self, cid):
        return self._department_url % cid

    def start_requests(self):
        department_id = settings.get('DEPARTMENT_ID')
        if not department_id:
            raise NotConfigured("Requires DEPARTMENT_ID setting. Use --set DEPARTMENT_ID=name")

        url = self.department_url(department_id)

        yield self.make_requests_from_url(url)

    def parse(self, response):
        # follow course links
        for link in self.course_le.extract_links(response):
            # go directly to download materials link
            url = '%s/download-course-materials/' % link.url.rstrip('/')
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        # get url's path parts
        # /course/<department>/<course>/download.../
        path = urlparse.urlparse(response.url).path.strip('/').split('/')

        hxs = HtmlXPathSelector(response)
        breads = hxs.select('//div[@id="portal-breadcrumbs"]//a/text()').extract()
        dlink = hxs.select('//div[@class="downloadLink"]')

        url = urljoin_rfc(response.url, dlink.select('./a/@href').extract()[0])
        size = dlink.select('./a//text()').extract()

        loader = MaterialItemLoader(selector=hxs)
        loader.add_value('department_id', path[1])
        loader.add_value('department', breads[2])
        loader.add_value('course_id', path[2])
        loader.add_value('course', breads[2])
        loader.add_value('download_size', size)
        loader.add_value('download_url', url)
        loader.add_value('origin_url', response.url)

        return loader.load_item()


SPIDER = MaterialsSpider()
