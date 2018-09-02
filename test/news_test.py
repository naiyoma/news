import unittest
from app.models import News



class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news=News(90,'cool','new','damn','okay','gdii','good')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

           