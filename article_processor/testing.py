
from article_processor import Processor

test_set = [
    (r"http://www.nasdaq.com/article/the-3-top-stocks-for-your-ira-in-august-cm830110", 1),
    (r"https://seekingalpha.com/article/4099116-ibm-watson-disappointment-risks-downward-revisions", 0),
    (r"https://seekingalpha.com/article/4099145-blockchain-ibms-comeback", -1),
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
    (r"http://www.investopedia.com/news/warren-buffett-enters-synchrony-financial-adds-bank-new-york-mellon-13f-berkshire-hathaway/?utm_campaign=quote-nasdaq&utm_source=nasdaq&utm_medium=referral&utm_term=fb-capture&utm_content=/#ec|rss-nasdaq",0)
]

for t in test_set:
    res = None
    while res is None:
        try:
            c = Processor()
            res = c.process(t[0])
            if res is None:
                raise Exception()
            if res[0] != t[1]:
                print 'ERROR in url: {} \n excepted : {}'.format(t[0], t[1])
            else:
                print 'GOOD in url: {} \n excepted : {}'.format(t[0], t[1])
        except Exception, e:
            print 'SHIT {}'.format(e)
            res = None
