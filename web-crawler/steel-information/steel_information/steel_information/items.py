# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#  /robots.txt

import scrapy


class SteelInfoItem(scrapy.Item):
    news_id = scrapy.Field()
    title_name = scrapy.Field()
    notes = scrapy.Field()
    texts = scrapy.Field()
    publish_time = scrapy.Field()
    website_url = scrapy.Field()
    website_name = scrapy.Field()
    response = scrapy.Field()
