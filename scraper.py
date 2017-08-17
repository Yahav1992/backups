import scrapy
from scrapy.crawler import CrawlerProcess

class NasSpider(scrapy.Spider):
    name = "nas_spider"
    start_urls = ['http://www.nasdaq.com/symbol/aapl/news-headlines?page=1']

    def parse(self, response):
        SET_SELECTOR = '.fontS14px'
        for span in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a'
            IMAGE_SELECTOR = 'a ::attr(href)'
            yield  {
              #  'name' : span.css(NAME_SELECTOR).extract_first(),
                'link' : span.css(IMAGE_SELECTOR).extract_first(),
            }

process = CrawlerProcess({})
process.crawl(NasSpider)
process.start()