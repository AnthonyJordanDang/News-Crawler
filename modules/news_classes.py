from modules.crawl_process import getJSON, getArticleURLs, contentOfSource, refineData, getData
#News sources that cannot be scraped: abcnews, huffingtonpost

#Superclass
class Website:
    
    def __init__(self, source_id, keyword, size):
        self.source_id = source_id
        self.keyword = keyword
        self.size = size

        self.url = ('https://newsapi.org/v2/everything?'
       'q=' + self.keyword +'&'
       'sources=' + self.source_id + '&'
       'sortBy=relevancy&'
       'pageSize=' + str(self.size) + '&'
       'apiKey=e344a840b71c4e4ba25426f528f8e00e')
    
    def getURL(obj):
        return obj.url

#class to get Data from a CBC Website
class CBC(Website):
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'div', 'class', 'story')
        return (articleContent_list)
    
        
#class to get Data from a Globe and Mail Website
class GlobeAndMail(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'p', 'class', 'c-article-body__text')
        return (articleContent_list)
    
#class to get Data from Fortune
class Fortune(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'div', 'id', 'article-body')
        return (articleContent_list)

#class to get Data from BusinessInsider Website
class BusinessInsider(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'section', 'class', 'post-content typography ')
        return (articleContent_list)
    
#class to get Data from DailyMail Website
class DailyMail(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'div', 'itemprop', 'articleBody')
        return (articleContent_list)

#class to get Data from FinancialPost Website
class FinancialPost(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'div', 'class', 'story-content')
        return (articleContent_list)


class FoxNews(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'div', 'class', 'article-content')
        return (articleContent_list)
    
class NBCNews(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'div', 'class', 'body___')
        return (articleContent_list)
    
class CNN(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'div', 'class', 'l-container')
        return (articleContent_list)
    
class TheNewYorkTimes(Website):   
    def __init__(self, source_id, keyword, size):
        Website.__init__(self, source_id, keyword, size)    

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, 'div', 'class', 'css-1fanzo5 StoryBodyCompanionColumn')
        return (articleContent_list)








