import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the news source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news', 'ABC News', 'This is ABC News, home to the best news')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

