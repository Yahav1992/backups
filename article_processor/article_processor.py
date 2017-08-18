from aylienapiclient import textapi

class Processor:
    pos = ["grow", "potential", "growth", "economic necessity", "increased demand", "growing", "evolving",
           "major growth", "impressive", "good", "rise", "top stocks for you", "high-yielding",
           "bullish", "attractive", "growth", "safe", "dominant", "gains", "impressive", "greatest", "benefit",
           "winners", "increased", "on track", "improve", "announced", "solution"]
    neg = ["down", "lower", "disappointing", "disappoint", "wrong", "disappointment", "downside", "risk",
           "struggling", "spending", "berish", "falling", "fails", "bearish", "risky", "dropping",
           "negative", "decline", "troubling", "low", "disappointing", "risk", "wrong", "However", "fallen",
           "underperformed", "down", "poor", "away", "worst", "warned", "anti", "fall"]
    def __init__(self):
        self.client = textapi.Client("3cd69ba8", "94abc89fc93b8a3392dbc6cd953f48d7")

    def _words_in_sentence(self, words, sentence):
        counter = 0
        for w in words:
            if w in sentence:
                counter += 1
        return counter

    def _decide(self, pos_point, neg_point, nlp_decision, nlp_confidence, url):
        """

        :param pos_point:
        :param neg_point:
        :param nlp_decision:
        :param nlp_confidence:
        :return:
        """

        if self._words_in_sentence(Processor.neg, url) > 0:
            return (0, 1)

        if pos_point is 0 and neg_point is 0:
            if nlp_confidence > 0.95 and nlp_decision is 1:
                return (1, nlp_confidence)
            else:
                return (0, 1)
        else:
            # if there is points

            # absolut accourance of type of words
            if pos_point - neg_point > neg_point and pos_point - neg_point > 3:
                if nlp_decision is 0 and nlp_confidence > 0.8:
                    return (-1, 1)
                return (1, pos_point/(pos_point + neg_point))
            if neg_point > pos_point and neg_point > 1:
                return (0, neg_point/(pos_point + neg_point))
            elif nlp_decision == 1:
                return (1, nlp_confidence)
            else:
                return (-1, neg_point / (pos_point + neg_point))

            if pos_point >= neg_point:
                if nlp_decision == 1 and nlp_confidence > 0.8 and neg_point < 3:
                    return (1, nlp_confidence)
                elif neg_point >= 3 and nlp_decision !=  1:
                    return (0, 1)
                else:
                    return (-1, 1)
            else:
                # more negative:
                return (0, 1)


    def process(self, url = ""):
        """

        :param url:
        :return:
        """
        #url = "http://www.nasdaq.com/article/sap-collaborates-with-ibm-to-revolutionize-procurement-cm791324"

        pos_point = 0
        neg_point = 0
        try:
            summary = self.client.Summarize({'url': url, 'sentences_number': 5})
            text = u""
            for sen in summary["sentences"]:
                pos_point += self._words_in_sentence(Processor.pos, sen.lower())
                neg_point += self._words_in_sentence(Processor.neg, sen.lower())
                text += sen + " "

            sentiment = self.client.Sentiment({'text': text.encode('utf-8'), 'mode': 'document'})

            return self._decide(pos_point, neg_point, sentiment['polarity'] == 'positive', sentiment['polarity_confidence'], url)



        except Exception, e:
            raise e


