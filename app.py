import pandas as pd

import re

#import functions for the website extractions
from modules.crawl_process import getJSON, getArticleURLs, contentOfSource, refineData, getData

# import the classes for each news source
from modules.news_classes import Website, CBC, GlobeAndMail, Fortune, BusinessInsider, CNN, DailyMail, FinancialPost, FoxNews, NBCNews, TheNewYorkTimes

#Data required from the user
keywords_raw = input("What are you web crawling for? ")

#removes special characters and replaces spaces with hyphen
keywords = re.sub('[^a-zA-Z]+', '-',  re.sub('[^a-zA-Z]+', ' ', keywords_raw.strip()) .strip()) 
 
size_raw = int(input("How many articles do you want to extract? (minimum: 10) "))

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
cbc = CBC('cbc-news', keywords, size)
globeandmail = GlobeAndMail('the-globe-and-mail', keywords, size)
fortune = Fortune('fortune', keywords, size)
business_insider = BusinessInsider('business-insider', keywords, size)
daily_mail = DailyMail('daily-mail', keywords, size)
financial_post = FinancialPost('financial-post', keywords, size)
fox_news = FoxNews('fox-news', keywords, size)
nbc_news = NBCNews('nbc-news', keywords, size)
cnn = CNN('cnn', keywords, size)
thenewyorktimes = TheNewYorkTimes('the-new-york-times', keywords, size)

#collects data from each news outlet
cbc_data = getData(cbc)
globeandmail_data = getData(globeandmail)
fortune_data = getData(fortune)
business_insider_data = getData(business_insider)
daily_mail_data = getData(daily_mail)
financial_post_data = getData(financial_post)
fox_news_data = getData(fox_news)
nbc_news_data = getData(nbc_news)
cnn_data = getData(cnn)
thenewyorktimes_data = getData(thenewyorktimes)

print('Congrats! The data scrape has been successful! :)', flush = True)

#Concatenation of all the data collection from the news sources
articles_data = cbc_data \
                + globeandmail_data \
                + fortune_data \
                + business_insider_data \
                + daily_mail_data \
                + financial_post_data \
                + fox_news_data \
                + nbc_news_data \
                + cnn_data  \
                + thenewyorktimes_data 

#Convert the dictionary into a Dataframe for analysis
df = pd.DataFrame.from_dict(articles_data)    

#handles if the url cannot be opened, and filled content value as null
try:
    df.to_csv('Data/data.csv')
except PermissionError:
    print('Please close the data.csv file and try again!', flush = True)








