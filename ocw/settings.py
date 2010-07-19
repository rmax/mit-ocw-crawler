# default settings

BOT_NAME = 'ocw'
BOT_VERSION = '0.1'

SPIDER_MODULES = ['ocw.spiders']
NEWSPIDER_MODULE = 'ocw.spiders'
DEFAULT_ITEM_CLASS = 'ocw.items.OcwItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

TELNETCONSOLE_ENABLED = False
WEBSERVICE_ENABLED = False

# be nice not downloading many pages at same time
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS_PER_SPIDER = 1
CONCURRENT_ITEMS = 1

# See in scrapy's docs EXPORT_FORMAT and EXPORT_FILE settings
ITEM_PIPELINES = [
    'scrapy.contrib.pipeline.fileexport.FileExportPipeline',
]

# Uncomment these to improve repetitive crawling by using caching
#HTTPCACHE_DIR = 'cache'
#HTTPCACHE_EXPIRATION_SECS = -1
