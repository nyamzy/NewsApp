import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Article('cnn', 'Serial killer on the loose', 'There is a serial killer on the loose in city streets', 'http://www.cnn.com/news/world-us-canada-59658661','https://ichef.bbci.co.uk/news/1024/branded_news/14ED7/production/_117891758_gettyimages-111178852.jpg','2021-12-14T18:52:19.4576902Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))
