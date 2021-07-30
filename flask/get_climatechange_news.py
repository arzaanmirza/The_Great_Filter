# This file searches for news articles which relate to Climate Change that are occuring in the world.
# It requires you to change the country inputted to which then it finds natural disasters from that country.

#import requests
import json
from newsapi import NewsApiClient

def get_climatechange_news(country_inputted):

    api = NewsApiClient(api_key='cc17316ba8b84f2eb4aa4d76a6b7d1a5')
    #country_inputted = 'Mexico'    # Country chosen
    #disaster_words = '(kills OR deaths OR destruction)'#disaster words

    query_string = "("+country_inputted + ' AND ' + "climate change"+")" #+ ' OR ' + disaster_words # Query statement
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

        if "climate change" not in article_description:
            continue

    # Printing commands:
        print(media_source) # Finds the name of the media source
        print(f"Article Title: {title} ")
        print(f"Description: {article_description} ")
        print(f"Article URL: {article_url} ") #Prints the url of the article


        count = count + 1
        print("\n")

    #print(count)
