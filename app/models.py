class Source:
    '''
    Source class to define the News Source Objects
    '''
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
       

class Article:
    '''
    Articles class to define the news articles objects
    '''
    def __init__(self, id, title, description, url, image, time):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.time = time
        