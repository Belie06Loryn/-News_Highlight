import unittest
from app.models_sources import Source

class SourceTest(unittest.TestCase):

    def setUp(self):
        '''
        Set up method that will run before every Tests
        '''
        self.news_source = Source("cnn","CNN","View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN",
"http://us.cnn.com","general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.news_source,Source))