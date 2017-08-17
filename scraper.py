import scrapy
import time
from scrapy.crawler import CrawlerProcess


class NasSpider(scrapy.Spider):
    name = "nas_spider"

    def __init__(self, category=None, *args, **kwargs):
        super(NasSpider, self).__init__(*args, **kwargs)
        print args, kwargs
        print category
        if not isinstance(category, basestring):
            self.start_urls = ['http://www.nasdaq.com/symbol/%s/news-headlines?page=1' % category[0]]
        else:
            self.start_urls = ['http://www.nasdaq.com/symbol/%s/news-headlines?page=1' % category]

    def parse(self, response):
        SET_SELECTOR = '.news-headlines'
        for headline in response.css(SET_SELECTOR):
            LINK_SELECTOR = '.fontS14px'
            for span in headline.css(LINK_SELECTOR):
                IMAGE_SELECTOR = 'a ::attr(href)'
                yield {
                    'link': span.css(IMAGE_SELECTOR).extract_first(),
                }
