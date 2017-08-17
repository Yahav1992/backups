import scrapy
from scrapy.crawler import CrawlerProcess

class NasSpider(scrapy.Spider):
    name = "nas_spider"
    start_urls = ['http://www.nasdaq.com/symbol/viix/news-headlines?page=1']

    def parse(self, response):
        SET_SELECTOR='.news-headlines'
        for headline in response.css(SET_SELECTOR):
            LINK_SELECTOR = '.fontS14px'
            for span in headline.css(LINK_SELECTOR):
                IMAGE_SELECTOR = 'a ::attr(href)'
                yield {
                    'link' : span.css(IMAGE_SELECTOR).extract_first(),
                }