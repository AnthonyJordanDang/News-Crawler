import requests
import json
import copy

from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup

from time import sleep

from random import randint

import re

#returns a dict of articles
def getJSON(api_url):
    
    """ Return list containing details relating to articles from news API

    Parameters:
        api_url (str):The url string to access news API

    Returns:
        article_list:list   

    """
    response = requests.get(api_url)
    articles = response.json()
    articles_prettify = json.dumps(articles, indent = 2)
    articles_dict = json.loads(articles_prettify)
    article_list = articles_dict['articles']
    return(article_list)

#gets the urls to the articles in a list
def getArticleURLs(api_url):
    
    """ Return list of urls to the articles

    Parameters:
        api_url (str):The url string to access news API

    Returns:
        url_list:list of urls to the articles   

    """
    article_list = getJSON(api_url)

    url_list = []

    for idx, url in enumerate(article_list):
        url_list.append(url['url'])

    #print statement for debugging purposes
    #print('..getting URLs', flush = True)
    return(url_list)

#collects the content of each article into a list
def contentOfSource(api_url, htmlSearch):
    
    """ Return list of content from the article urls

    Parameters:
        api_url (str):The url string to access news API
        html_element(str): The html element where content is located on the site
        html_attribute(str): The html attribute under the html element where content is located on the site
        html_attributeName(str): The html attribute name where content is located on the site

    Returns:
        articleContent_list:list of content from the article urls  

    """
    
    articleURLs = getArticleURLs(api_url)
    articleContent_list = []
    
    for url in articleURLs:
        
        articleContent = ""
        
        #handles if the url cannot be opened, and filled content value as null
        try:
            html = urlopen(url)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print('..Url cannot be opened', flush = True)
                articleContent_list.append(articleContent)
                sleep(randint(1,2))
                continue
            else:
                raise
        
        soup = BeautifulSoup(html, 'lxml')
        
        #Loops through list of potential html to search for article content
        for html in htmlSearch:
            element_index = 0
            attribute_index = 1
            attributeName_index = 2
            
            #variable for attribute name that contains
            html_attributeName_regex = re.compile('.*' + html[attributeName_index] + '*')

            result = soup.findAll(html[element_index], {html[attribute_index]:html_attributeName_regex})

            for res in result:
                content_text = res.text.strip() 
                articleContent = articleContent + content_text 

            #if there is nothing in the content continue the loop 
            if articleContent == "":
                continue
            else:
                # indicates the app is crawling through specified url
                print('...crawling through '+url, flush = True)
        
                break

        #checks if article content was found
        if articleContent == '':
            print("...No content found on this page!", flush = True)

        #adds the content collected to the list of article content
        articleContent_list.append(articleContent)
        
        sleep(randint(1,4))
    return articleContent_list

#deletes unnecessary dict values and replaces api content with collected content
def refineData(articleContent_list, api_url):
    
    """ Return dict of all articles with their content

    Parameters:
        articleContent_list (list):The list containing the content from the urls
        api_url (str):The url string to access news API

    Returns:
        article_details_clean:dict containing details from all articles 

    """
    #list of key words in url that indicate it is not an article
    noContent_keywords = ['video']
    article_details = getJSON(api_url)
    article_details_clean = copy.deepcopy(article_details)

    for idx, article in enumerate(article_details_clean):
        
        del [article['urlToImage'],article['description']]
        article['source'] = article['source']['name']
        
        #if the url contains key words that indicate the there is no content that make the content empty
        for word in noContent_keywords:
            if word in article['url']:
                article['content'] = ''
            else:
                article['content'] = articleContent_list[idx]
    
        
    
    return (article_details_clean)

#function that contains methods mentioned above
def getData(obj):
    """ 
    Consolidation of all the three above function
    """
    api_url = obj.getURL()
    json = getJSON(api_url)
    content_list = obj.getArticleContent()
    data = refineData(content_list, api_url)
    
    # indicates if there are any articles found with the given topic
    if data == []:
        #print statement for debugging purposes
        #print('Data Extracted from ' + obj.source_id + '!', flush = True)
        print('No articles found!', flush = True)
       
    return data
