
from article_processor import Processor

test_set = [
    (r"http://www.nasdaq.com/article/the-3-top-stocks-for-your-ira-in-august-cm830110", 1),
    (r"https://seekingalpha.com/article/4099116-ibm-watson-disappointment-risks-downward-revisions", 0)
    (r"https://seekingalpha.com/article/4099145-blockchain-ibms-comeback", -1),
    (r"http://marketrealist.com/2017/08/how-alphabet-is-tackling-its-cloud-competition/", -1),
    (r"https://seekingalpha.com/article/4099361-ibm-value-trap", -1)

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
                print 'ERROR in url: {} '.format(t[0])
            else:
                print 'GOOD in url: {} '.format(t[0])
        except Exception, e:
            print 'SHIT {}'.format(e)
            res = None
