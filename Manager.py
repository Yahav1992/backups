from scrapy.crawler import CrawlerProcess
from tel_bot import StockNasBot
from article_processor.article_processor import Processor
from scraper import NasSpider
import json
import os


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
    index = 0
    for array in data:
        for link in array:
            print link
            towriteflag = 0
            url = link["link"]
            # Check url in file

            if os.path.exists('history.json'):
                with open('history.json', 'r+' ) as historyfile:
                    historydata = json.load(historyfile)

                if url in historydata:
                    continue
            res = None
            while res is None:
                try:
                    c = Processor()
                    res = c.process(url)
                    if res is None:
                        raise Exception()

                    urldict = {url: res}
                    if historydata is not None:
                        historydata.update(urldict)
                        with open('history.json', 'w') as historyfile:
                            json.dump(historydata, historyfile)
                    else:
                        raise ValueError()
                    if res[0] == 1:
                        bot.sendmessage('You should buy stock {}  {}'.format(symbList[len(symbList)- index], url))
                        #print "You should buy %s" % sym[index]
                    print res

                except Exception, e:
                    if hasattr(e, 'content'):
                        if "Too Many " in e.content:
                            print "Renew user"
                    res = None
        index += 1