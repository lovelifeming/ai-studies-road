# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#  /robots.txt

import scrapy


class SteelInformationItem(scrapy.Item):
    title = scrapy.Field()
    notes_list = scrapy.Field()
    website_url = scrapy.Field()
    website_name = scrapy.Field()
    response = scrapy.Field()
