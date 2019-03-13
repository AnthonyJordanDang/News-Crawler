import pandas as pd

import re

#import functions for the website extractions
from modules.crawl_process import getJSON, getArticleURLs, contentOfSource, refineData, getArticleData

# import the classes for each news source
from modules.news_classes import NewsWebsite 

#Data required from the user
keywords_raw = input("What are you web crawling for? ")

#removes special characters and replaces spaces with hyphen
keywords = re.sub('[^a-zA-Z]+', '-',  re.sub('[^a-zA-Z]+', ' ', keywords_raw.strip()) .strip()) 
 
#html of various websites that contain article content
cbc_html = [['div', 'class', 'story']]
globeAndMail_html = [['p', 'class', 'c-article-body__text']]
fortune_html = [['div', 'id', 'article-body'],['div', 'class', 'article content']]
businessInsider_html = [['section', 'class', 'post-content typography ']]
dailyMail_html = [['div', 'itemprop', 'articleBody']]
financialPost_html = [['div', 'class', 'story-content']]
foxNews_html = [['div', 'class', 'article-content']]
nbcNews_html = [['div', 'class', 'body___']]
cnn_html = [['div', 'class', 'l-container']]
theNewYorkTimes_html = [['div', 'class', 'css-1fanzo5 StoryBodyCompanionColumn']]

#Asks user for number of articles desired
size_raw = int(input("How many articles do you want to extract? (minimum: 10) "))

#Number of news sources
newsOutlet_len = 10

#Makes sure the size input is greater than 10
while size_raw < newsOutlet_len:
    print('Oops! Please try again')
    size_raw = int(input("How many articles do you want to extract? (minimum: " + newsOutlet_len + ") "))
    if size_raw > newsOutlet_len:
        break

#sets the size for each news source
size = round(size_raw / newsOutlet_len)

#creating objects for each news source
cbc = NewsWebsite('cbc-news', keywords, size, cbc_html)
globeandmail = NewsWebsite('the-globe-and-mail', keywords, size, globeAndMail_html)
fortune = NewsWebsite('fortune', keywords, size, fortune_html)
business_insider = NewsWebsite('business-insider', keywords, size, businessInsider_html)
daily_mail = NewsWebsite('daily-mail', keywords, size, dailyMail_html)
financial_post = NewsWebsite('financial-post', keywords, size, financialPost_html)
fox_news = NewsWebsite('fox-news', keywords, size, foxNews_html)
nbc_news = NewsWebsite('nbc-news', keywords, size, nbcNews_html)
cnn = NewsWebsite('cnn', keywords, size, cnn_html)
thenewyorktimes = NewsWebsite('the-new-york-times', keywords, size, theNewYorkTimes_html)

#Concatenation of all the data collection from the news sources
articles_data = cbc.data \
                + globeandmail.data \
                + fortune.data \
                + business_insider.data \
                + daily_mail.data \
                + financial_post.data \
                + fox_news.data \
                + nbc_news.data \
                + cnn.data \
                + thenewyorktimes.data

#Convert the dictionary into a Dataframe for analysis
df = pd.DataFrame.from_dict(articles_data)    

print('Congrats! Crawl Complete! :)', flush = True)

#catch if data file is open and cannot be modified
try:
    df.to_csv('Data/data.csv')
except PermissionError:
    print('Please close the data.csv file and try again!', flush = True)








