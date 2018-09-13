import unittest
from app.models import News,Articles



class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news=News(90,'cool','new','damn','okay','nice','root')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    # def test_check_instance_variables(self):
    #     self.assertEquals(self)
    #     self.assertEquals(self.new_news.name,cool)
    #     self.assertEquals(self.new_news.description,new)
    #     self.assertEquals(self.new_news.url,damn)
    #     self.assertEquals(self.new_news.category,okay)
    #     self.assertEquals(self.new_news.language,nice)
    #     self.assertEquals(self.new_news.country,root)    
        

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_articles=Articles('nice','forr','what',"ooh",'woow','kiki')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles, Articles)) 

    # def test_check_instance_variables(self):
    #     self.assertEquals(self.new_articles.author,nice)
    #     self.assertEquals(self.new_articles.title,forr)
    #     self.assertEquals(self.new_articles.description,what)
    #     self.assertEquals(self.new_articles.url,ooh)
    #     self.assertEquals(self.new_articles.urlToImage,woow)
    #     self.assertEquals(self.new_articles.urlToImage,kiki)

# 1.importing the news class that we created
# 2.setup method enables our class to take in objects
# 3.the isinstance functions chack if the objects created are instances of a class           