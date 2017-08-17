from aylienapiclient import textapi
shit_t = r"""
Shares of cybersecurity stocks and related ETFs are up almost across the board on Wednesday after Gartner IT released a report that pointed to the sector's growth potential in 2017 and beyond.

Cybersecurity is in vogue, but based on the increasing amount of incidents, attacks, and multiple reports on its growth potential, including Gartner's recent projections, cybersecurity will be an economic necessity and an even bigger business from now on.

The firm points to an array of factors that will contribute to the sector's rise, one of which is the vast amount of growth potential for IT security startups, especially in the business-to-business sector.

Gartner Report

Gartner, which claims to have the "largest base of IT research analysts and consultants in the world," projects global cybersecurity spending to grow by 7% in 2017 to reach $86.4 billion. The firm pointed to data breaches and an increased demand for app security testing as part of the reason for the growth, as first reported by Tech Crunch .

The report also suggests that spending on emerging application security testing tools will help lead to growth through 2021. Gartner sees interactive application security testing increasing in the ever growing mobile world where apps rule. The idea is that companies and small startups, which count on their apps in order to grow and maintain their business, will need to run security tests and equip their apps with advanced cybersecurity software.

"Rising awareness among CEOs and boards of directors about the business impact of security incidents and an evolving regulatory landscape have led to continued spending on security products and services," principal research analyst Sid Deshpande said in a statement .

While the report notes that IT security spending will go up dramatically, Gartner notes that physical hardware support services will decline due to the rise of cloud computing and non-hardware-based IT services.

Gartner also cites the European Union's " General Data Protection Regulation " as a major growth catalyst because it will force companies to spend money on cybersecurity. The EU regulatory body will begin to enforce the new law, which requires companies and other entities to meet certain cybersecurity thresholds or face heavy fines, on May 25, 2018.

Cybersecurity

Other firms have been even more optimistic than Gartner in terms of cybersecurity's growth potential.

According to a July Markets and Markets report , the worldwide cybersecurity market will soar to $137.85 billion in 2017 and skyrocket to $231.94 billion by 2022. Markets and Markets points to "strict data protection directives and cyber terrorism," and the proliferations of internet-connected devices as major reasons for the firm's massive growth projections.

On Tuesday, Los Angeles city officials announced a plan to have the city and companies share information about cybersecurity threats. The hope is to help businesses in the greater LA area become better protected by sharing their knowledge and experiences with cybersecurity threats and breaches.

"We need to leave behind the concern about how we will be judged by others and realize it happens to everyone," Riot Games' director of security, Christopher Hymes, who is an early partner in the initiative, told the LA Times . "If all participating companies come to the table with that attitude and share their experiences, it will be successful.

Stocks

Shares of some of the biggest cyber security companies all climbed on Wednesday.

Proofpoint PFPT , Palo Alto Networks PANW , and Fortinet FTNT all jumped over 1%. FireEye FEYE , Rapid7 RPD , and Check Point Software CHKP , all gained over 0.60%.

Imperva IMPV , Qualys QLYS , and CyberArk CYBR all saw marginal gains, while ETFMG Prime Cyber Security ETF HACK rose 0.59%.

The Hottest Tech Mega-Trend of All

Last year, it generated $8 billion in global revenues. By 2020, it's predicted to blast through the roof to $47 billion. Famed investor Mark Cuban says it will produce "the world's first trillionaires," but that should still leave plenty of money for regular investors who make the right trades early. See Zacks' 3 Best Stocks to Play This Trend >>


Want the latest recommendations from Zacks Investment Research? Today, you can download 7 Best Stocks for the Next 30 Days. Click to get this free report


"""
shit = r"""
Canada's main stock market slipped into negative territory late in the midweek trading session, fading from earlier highs following U.S. President Trump's decision to disband two advisory councils and the release of the Fed minutes from July, which raised inflation concerns. The S&P/TSX Composite Index was down 15 points or 0.1% to close at 15,082 Wednesday.

Materials led gainers, rising 1.7%, as precious metals climbed, including gold and silver. Copper was up nearly 3%. Financials were modestly weaker while energy lost 1.2% as oil prices declined 1.6%.

In stock news, Loblaw (L.TO) shares fell 0.2% after CIBC (CM.TO) ended its financial partnership with the grocery giant, with the bank absorbing two million PC Financial customers and starting up its own digital banking service, to be known as Simplii. CIBC shares were off 0.5%. Apple ( AAPL ) was down 0.4% after the iPhone maker issued $2.5 billion in maple bonds, its first foray into the Canadian market. Maple bonds are issued by foreign companies in Canadian dollars. Heavily traded Primero Mining (P.TO) shed 15% while Hudbay Minerals (HBM.TO) gained 11%. Suncor Energy (SU.TO), one of the day's most influential shares, lost 2%.

In economic news, Canada saw a $923 million outflow of foreign investment in June after the huge $29.4 billion inflow in May and a $10.6 billion inflow in April. The outflow in June is the first since July 2015. Canadians invested $13.2 billion abroad in June. Manufacturing shipment values are due Thursday, and are projected to fall 1.0% in June after the 1.1% gain in May. CPI, released Friday, is expected to be flat in July after a 0.1% dip in June. The annual growth rate is seen improving to a still lean 1.2% in July from the 1.0% pace in June.

The Canadian dollar gained nearly a full cent to 79.22 as the USD weakened.

The views and opinions expressed herein are the views and opinions of the author and do not necessarily reflect those of Nasdaq, Inc.
"""

class Processor:
    def __init__(self):
        self.client = textapi.Client("dc573498", " 341b6e08b058dca857a2acf0128d31a1")

    def _words_in_sentence(self, words, sentence):
        counter = 0
        for w in words:
            if w in sentence:
                counter += 1
        return counter

    def process(self, url = ""):
        """

        :param url:
        :return:
        """
        pos = ["grow", "potential", "growth", "economic necessity", "increased demand", "growing", "evolving",
               "major growth", "impressive", "good", "rise", "top stocks for you"]
        neg = []
        pos_point = 0
        neg_point = 0
        try:
            summary = self.client.Summarize({'url': url, 'sentences_number': 5})
            text = u""
            for sen in summary["sentences"]:
                pos_point += self._words_in_sentence(pos, sen)
                neg_point += self._words_in_sentence(neg, sen)
                text += sen + " "

            sentiment = self.client.Sentiment({'text': text.encode('utf-8'), 'mode': 'document'})

            if pos_point + neg_point > 0:
                if sentiment['polarity'] == 'positive':
                        pos_point += (pos_point + neg_point)*sentiment['polarity_confidence']
                if sentiment['polarity'] == 'negative':
                        neg_point += (pos_point + neg_point) * sentiment['polarity_confidence']
            else:
                return (sentiment['polarity'] == 'positive', sentiment['polarity_confidence'])


            if pos_point > neg_point:
                return (1, pos_point/(pos_point + neg_point))
            if neg_point > pos_point:
                return (0, neg_point / (pos_point + neg_point))

            return

        except Exception, e:
            print e


c = Processor()
shit = None
while shit is None:
    try:
        shit = c.process(r"http://www.nasdaq.com/press-release/liveperson-ibm-watson-announce-new-offering-to-transform-customer-care-20170615-01051")
        print shit
    except Exception,e:
        print e

