class News:
    def __init__(self,id,name,description,url,category,language,country):
        self.id=id
        self.name=name 
        self.description=description
        self.url=url 
        self.category=category
        self.language=language 
        self.country=country

class Articles:
    '''
    class that defines articles objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

# 1.i have created a news class that will hold the responses from the the api call
# 2.The def__init__method means that this clases can be imported anywhere