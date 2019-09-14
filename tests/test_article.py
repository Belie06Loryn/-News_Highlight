import unittest
from app.models_article import Article

class ArticleTest(unittest.TestCase):

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_Article = Article("the-next-web","The Next Web","Satoshi Nakaboto","Satoshi Nakaboto: ‘Bitcoin dips below $10K — again ’","Our robot colleague Satoshi Nakaboto writes about Bitcoin every fucking day. Welcome to another edition of Bitcoin Today, where I, Satoshi Nakaboto, tell you what’s been going on with Bitcoin in the past 24 hours. As Albert Einstein used to say: Let’s whip up…","https://thenextweb.com/hardfork/2019/08/29/satoshi-nakaboto-bitcoin-dips-below-10k-again/","https://img-cdn.tnwcdn.com/image/hardfork?filter_last=1&fit=1280%2C640&url=https%3A%2F%2Fcdn0.tnwcdn.com%2Fwp-content%2Fblogs.dir%2F1%2Ffiles%2F2019%2F08%2Fbitcoin_today-header_bitcoin_today.jpg&signature=30221b6a68049cc6bc3b58f3ddb38864","2019-08-29T08:11:37Z","Our robot colleague Satoshi Nakaboto writes about Bitcoin BTC every fucking day.\r\nWelcome to another edition of Bitcoin Today, where I, Satoshi Nakaboto, tell you whats been going on with Bitcoin in the past 24 hours. As Albert Einstein used to say: Lets whip… [+2977 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.news_Article,Article))