# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteelInfo1Item(scrapy.Item):
    news_id = scrapy.Field()
    title_name = scrapy.Field()
    type_id = scrapy.Field()
    signs = scrapy.Field()
    # release_channel = scrapy.Field()
    info_channel = scrapy.Field()
    audio_path = scrapy.Field()
    img_path = scrapy.Field()
    notes = scrapy.Field()
    texts = scrapy.Field()
    zan_count = scrapy.Field()
    publish_time = scrapy.Field()
    source = scrapy.Field()
    bottom_source = scrapy.Field()
    bottom_url = scrapy.Field()
    # subject = scrapy.Field()
    summary = scrapy.Field()
    website = scrapy.Field()
    website_name = scrapy.Field()
    child_topic = scrapy.Field()
    child_topic_url = scrapy.Field()
    keyword_type = scrapy.Field()
    response = scrapy.Field()
    sql = scrapy.Field()


class SaveImageItem(scrapy.Item):
    pass
