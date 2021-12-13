from re import DEBUG


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey=API_KEY'

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
