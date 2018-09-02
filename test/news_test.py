import unittest
from app.models import News



class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news=News(90,'cool','new','damn','okay','gdii','good')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

# 1.importing the news class that we created
# 2.setup method enables our class to take in objects
# 3.the isinstance functions chack if the objects created are instances of a class           