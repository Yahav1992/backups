import telepot
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StockNasBot(object):
    def __init__(self):
        # Token of bot StockerNasBot
        self.StockBot = telepot.Bot('400106985:AAENxyatWTXW1WPnI6W9ZWf37ls8RpMBJlc')
        # ID of @bestAdviceStock channel
        self.ChannelId = -1001124715725L

    def sendmessage(self, message):
        logging.info('Message is: [%s]', message)
        self.StockBot.sendMessage(self.ChannelId, message)
        logging.info('Sent to channel')


if __name__ == "__main__":
    bot = StockNasBot()
    bot.sendmessage('Testing, testing..Gefen has won! Alon is the man. And yahav is malshin')
