# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst

class OcwItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class MaterialItem(Item):
    department_id = Field()
    department = Field()
    course_id = Field()
    course = Field()
    download_size = Field()
    download_url = Field()
    origin_url = Field()

class MaterialItemLoader(XPathItemLoader):
    default_item_class = MaterialItem
    default_output_processor = TakeFirst()
