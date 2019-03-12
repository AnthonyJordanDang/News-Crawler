from modules.crawl_process import getJSON, getArticleURLs, contentOfSource, refineData, getData
#News sources that cannot be scraped: abcnews, huffingtonpost

#Superclass
class NewsWebsite:
    
    def __init__(self, source_id, keyword, size, html):
        self.source_id = source_id
        self.keyword = keyword
        self.size = size
        self.html = html

        self.url = ('https://newsapi.org/v2/everything?'
       'q=' + self.keyword +'&'
       'sources=' + self.source_id + '&'
       'sortBy=relevancy&'
       'pageSize=' + str(self.size) + '&'
       'apiKey=e344a840b71c4e4ba25426f528f8e00e')

    def getArticleContent(obj):
        articleContent_list = contentOfSource(obj.url, obj.html)
        return (articleContent_list)
    

    def getURL(obj):
        return obj.url

        
        




