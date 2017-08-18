from scrapy.crawler import CrawlerProcess
from tel_bot import StockNasBot
from article_processor.article_processor import Processor
from scraper import NasSpider
import json
import os
from email_sender import send_email


if os.path.exists("result.json"):
    os.remove("result.json")

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'result.json'
})

symbList = ["ibm", "viix", "aapl"]
for sym in symbList:
    spider = NasSpider(sym)
    process.crawl(spider, [sym])
process.start()



with open('result.json', 'r+') as datafile:
    lines = datafile.readlines()
    datafile.seek(0)
    datafile.truncate()
    for line in lines:
        if "][" in line:
            line = line.replace("][", "],[")
        elif "[" in line:
            line = line.replace("[", "[[")
        elif "]" in line:
            line = line.replace("]", "]]")
        datafile.write(line)

bot = StockNasBot()

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

                if res[0] == 1:
                    #bot.sendmessage('you should buy Stock VIIX  {}'.format(url))
                    print "You should buy %s" % sym
                    #send_email(r"yahav7rubin@gmail.com",sym,format(url))
                print res

            except Exception, e:
                if "Too Many " in e.content:
                    print "Renew user"
                res = None
