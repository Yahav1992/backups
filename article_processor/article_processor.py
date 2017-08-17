from aylienapiclient import textapi

class Processor:
    def __init__(self):
        self.client = textapi.Client("0037742b", "8b50b7ab13f2d87d915aa88b6ba8699a")

    def _words_in_sentence(self, words, sentence):
        counter = 0
        for w in words:
            if w in sentence:
                counter += 1
        return counter

    def _decide(self, pos_point, neg_point, nlp_decision, nlp_confidence):
        """

        :param pos_point:
        :param neg_point:
        :param nlp_decision:
        :param nlp_confidence:
        :return:
        """
        if pos_point is 0 and neg_point is 0:
            if nlp_confidence > 0.95 and nlp_decision is 1:
                return (1, nlp_confidence)
            else:
                return (-1, 1)
        else:
            # if there is points

            # absolut accourance of type of words
            if pos_point > 2*neg_point:
                return (1, pos_point/(pos_point + neg_point))
            if neg_point > pos_point:
                return (0, neg_point/(pos_point + neg_point))

            if pos_point > neg_point:
                if nlp_decision is 1:
                    return (1, nlp_confidence)
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
        pos = ["grow", "potential", "growth", "economic necessity", "increased demand", "growing", "evolving",
               "major growth", "impressive", "good", "rise", "top stocks for you", "high-yielding",
               "bullish", "attractive", "growth"]
        neg = ["down", "lower", "disappointing", "disappoint", "wrong", "disappointment", "downside", "risk",
               "struggling", "spending", "berish", "falling", "fails", "bearish", "risky", "dropping"]
        pos_point = 0
        neg_point = 0
        try:
            summary = self.client.Summarize({'url': url, 'sentences_number': 5})
            text = u""
            for sen in summary["sentences"]:
                pos_point += self._words_in_sentence(pos, sen.lower())
                neg_point += self._words_in_sentence(neg, sen.lower())
                text += sen + " "

            sentiment = self.client.Sentiment({'text': text.encode('utf-8'), 'mode': 'document'})

            if pos_point + neg_point > 0:
                if sentiment['polarity'] == 'positive':
                        pos_point += (pos_point + neg_point)*sentiment['polarity_confidence']
                if sentiment['polarity'] == 'negative':
                        neg_point += (pos_point + neg_point) * sentiment['polarity_confidence']
            else:
                return (sentiment['polarity'] == 'positive', sentiment['polarity_confidence'])

            return self._decide(pos_point, neg_point, sentiment['polarity'], sentiment['polarity_confidence'])



        except Exception, e:
            raise e


