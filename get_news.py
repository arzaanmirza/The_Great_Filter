#import requests
import json
from newsapi import NewsApiClient

api = NewsApiClient(api_key='cc17316ba8b84f2eb4aa4d76a6b7d1a5')

country_inputted = 'Pakistan'    # Country chosen
natural_disasters = '(floods OR typhoon OR hurricane OR "tropical storm" OR bushfires OR cyclone OR drought OR rising temperatures OR flooding)' # Natural disaster
natural_disasters_list = ["floods","typhoon","hurricane","storm","bushfires","cyclone","drought","heat","rising temperatures","flooding"]
#disaster_words = '(kills OR deaths OR destruction)'#disaster words

query_string = "("+country_inputted + ' AND ' + natural_disasters+")" #+ ' OR ' + disaster_words # Query statement
#news_sources='bbc-news,reuters,abc-news,cnn,foxnews,times-of-india,the-guardian' #All the news sources where you want to search from

data = api.get_everything(q=query_string)

list_of_articles = data["articles"]

count = 0
for article in list_of_articles:

    title = article["title"]         # Finds the name of the article title
    media_source = article["source"]["name"] # Finds the name of the media source
    article_description = article["description"] #Finds the description of the article
    article_url = article["url"]          #Finds the url of the article


#This if-statement ensures that the country is in the description
# of the article, this ensures that the news is from the country inputted.

    if country_inputted not in article_description:
            continue
    check=0
    for word in natural_disasters_list:
        if word in article_description:
            check=1

    if check==0:
        continue




    print(media_source) # Finds the name of the media source
    print(f"Article Title: {title} ")
    print(f"Description: {article_description} ")
    print(f"Article URL: {article_url} ") #Prints the url of the article


    count = count + 1
    print("\n")

print(count)
