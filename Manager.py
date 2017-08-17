from scrapy.crawler import CrawlerProcess
from article_processor.article_processor import Processor
from scraper import NasSpider
import json
import os

if os.path.exists(r"result.json"):
    os.remove(r"result.json")

process = CrawlerProcess({
'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
'FEED_FORMAT': 'json',
'FEED_URI': 'result.json'
})
process.crawl(NasSpider)
process.start()

with open('result.json') as data_file:
    data = json.load(data_file)
    for link in data:
        print link
        url = link["link"]
        res = None
        while res is None:
            try:
                c = Processor()
                res = c.process(url)
                if res is None:
                    raise Exception()
                print res

            except Exception, e:
                if "Too Many " in e.content:
                    print 'Renew user'
                res = None
