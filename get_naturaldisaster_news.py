# This file searches for news articles which relate to Natural Disasters that are occuring in the world.
# It requires you to change the country inputted to which then it finds natural disasters from that country.

#import requests
import json
from newsapi import NewsApiClient
from image_capture_database import image_capture_database
from image_capture import image_capture

def get_naturaldisaster_news(country_inputted):

    api = NewsApiClient(api_key='cc17316ba8b84f2eb4aa4d76a6b7d1a5')
    #country_inputted = 'Japan'    # Country chosen
    natural_disasters = '(floods OR typhoon OR hurricane OR bushfires OR cyclone OR drought OR rising temperatures OR flooding OR avalanche OR earthquake OR volcano OR heatwave OR famine)' # Natural disaster
    natural_disasters_list = ["floods","typhoon","hurricane","storm","bushfires","cyclone","drought","heat","rising temperatures","flooding"]
    #disaster_words = '(kills OR deaths OR destruction)'#disaster words

    query_string = "("+country_inputted + ' AND ' + natural_disasters+")" #+ ' OR ' + disaster_words # Query statement
    #news_sources='bbc-news,reuters,abc-news,cnn,foxnews,times-of-india,the-guardian' #All the news sources where you want to search from

    data = api.get_everything(q=query_string)

    list_of_articles = data["articles"]
    list_of_related_articles = []
    count = 0
    for article in list_of_articles:

        title = article["title"]         # Finds the name of the article title
        media_source = article["source"]["name"] # Finds the name of the media source
        article_description = article["description"] #Finds the description of the article
        article_url = article["url"]          #Finds the url of the article



    #This chunk of code finds the image url of the article and adds it onto the dictionary
    # The point of it is so that a photo can be attached with the article on the website.

    # Right now it only works with reuters articles.
        if media_source == "Reuters":
            image_inside_article_url = image_capture(article_url)
        else: # This else statement is only there so that the next if statement works.
            image_inside_article_url = "empty_string"

        # Checks if image_capture() function has returned an empty_string or not.
        if image_inside_article_url == "empty_string":
            image_inside_article_url = image_capture_database(title)


    #This if-statement ensures that the country is in the description
    # of the article, this ensures that the news is from the country inputted.

        if country_inputted not in article_description:
                continue

    # This chunk of code ensures that the article that is picked up by the code actually
    # mentions a natural disaster.
        word_check=False
        for word in natural_disasters_list:
            if word in article_description:
                word_check=True

        if word_check==False:
            continue

    # Printing commands:
        # print(media_source) # Finds the name of the media source
        # print(f"Article Title: {title} ")
        # print(f"Description: {article_description} ")
        # print(f"Article URL: {article_url} ") #Prints the url of the article
        #data = "Media : "+media_source+"\n"+"Article Title: "+title+"\n"+"Description: "+article_description+"\n"+"Article URL: "+article_url
        #print(data)

        data = {

            "Media": media_source,
            "Article Title": title,
            "Description": article_description,
            "Article URL": article_url,
            "Image URL": image_inside_article_url,

        }
        # print(data)
        list_of_related_articles.append(data)

        count = count + 1
        print("\n")

    return list_of_related_articles
#print(count)
