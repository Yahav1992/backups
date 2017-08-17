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

            return (-1, 1)

        except Exception, e:
            raise e


