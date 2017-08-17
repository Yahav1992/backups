
from article_processor import Processor

test_set = [
    (r"http://www.nasdaq.com/article/the-3-top-stocks-for-your-ira-in-august-cm830110", 1),
    (r"https://seekingalpha.com/article/4099116-ibm-watson-disappointment-risks-downward-revisions", 0),
    (r"https://seekingalpha.com/article/4099145-blockchain-ibms-comeback", 1),
    (r"http://marketrealist.com/2017/08/how-alphabet-is-tackling-its-cloud-competition/", -1),
    (r"https://seekingalpha.com/article/4099361-ibm-value-trap", -1),
    (r"http://www.nasdaq.com/article/the-3-top-stocks-for-your-ira-in-august-cm830110", 1),
    (r"http://www.nasdaq.com/article/verizon-vz-and-amazon-team-up-for-virtual-network-services-cm833256",0),
    (r"http://www.nasdaq.com/article/warren-buffetts-had-it-with-these-stocks-cm833124",0),
    (r"http://www.nasdaq.com/article/2-high-yield-warren-buffett-stocks-and-1-he-wishes-he-could-buy-cm832975",1),
    (r"http://www.nasdaq.com/article/the-2-safest-dividend-stocks-to-buy-in-tech-cm832258",1),
    (r"http://www.nasdaq.com/article/the-zacks-analyst-blog-highlights-intel-microsoft-cisco-ibm-and-nvidia-cm832306",-1),
    (r"http://www.nasdaq.com/article/microsoft-unveils-enterprise-blockchain-coco-framework-cm832313",1),
    (r"http://www.nasdaq.com/article/tableau-acquires-cleargraph-enables-data-discovery-via-voice-cm832233",-1),
    (r"http://www.nasdaq.com/article/3-stocks-that-look-just-like-activision-blizzard-in-2013-cm832133",1),
    (r"http://www.nasdaq.com/article/should-you-invest-in-intel-intc-now-cm831870",-1),
    (r"https://seekingalpha.com/article/4099518-cogint-second-largest-holding?source=nasdaq",1),
    (r"http://www.investopedia.com/news/warren-buffett-enters-synchrony-financial-adds-bank-new-york-mellon-13f-berkshire-hathaway/?utm_campaign=quote-nasdaq&utm_source=nasdaq&utm_medium=referral&utm_term=fb-capture&utm_content=/#ec|rss-nasdaq",0),
    (r"http://www.nasdaq.com/article/worst-performing-etfs-so-far-this-year-cm772238", 0),
    (r"http://www.nasdaq.com/article/profit-from-the-trump-bump-with-volatility-etfs-cm740933", 1),
    (r"http://www.nasdaq.com/article/volatility-etfs-in-focus-as-trump-rally-fizzles-out-cm733427", 0),
    (r"http://www.nasdaq.com/article/why-investors-continue-to-pour-money-into-vix-etfs-cm723593", 1),
    (r"http://www.nasdaq.com/article/etf-launches-set-new-monthly-annual-records-cm688025", 0),
    (r"http://www.nasdaq.com/article/volatility-small-cap-india-2-etfs-trading-with-outsized-volume-cm685237", -1)
]

for t in test_set:
    res = None
    while res is None:
        try:
            if "bump" in t[0]:
                pass
            c = Processor()
            res = c.process(t[0])
            if res is None:
                raise Exception()
            if res[0] != t[1]:
                if t[1] is -1 or t[1] is 0:
                    if res[0] is -1 or res[0] is 0:
                        print 'GOOD in url: {} \n excepted : {} given {}'.format(t[0], t[1], res[0])
                        continue
                print 'ERROR in url: {} \n excepted : {} given {}'.format(t[0], t[1], res[0])
            else:
                print 'GOOD in url: {} \n excepted : {} given {}'.format(t[0], t[1], res[0])
        except Exception, e:
            print 'SHIT {}'.format(e)
            res = None
