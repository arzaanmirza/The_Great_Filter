# This file searches for news articles which relate to Climate Change that are occuring in the world.
# It requires you to change the country inputted to which then it finds natural disasters from that country.

import json
from newsapi import NewsApiClient
from image_capture_database import image_capture_database
from image_capture import image_capture

def get_climatechange_news(country_inputted):


    #This is the news api key which you can get from https://newsapi.org/
    api = NewsApiClient(api_key='cc17316ba8b84f2eb4aa4d76a6b7d1a5')

    query_string = "("+country_inputted + ' AND ' + "climate change"+")" #+ ' OR ' + disaster_words # Query statement
    data = api.get_everything(q=query_string)

    list_of_articles = data["articles"]
    list_of_related_articles = []

    for article in list_of_articles:

        title = article["title"]         # Finds the name of the article title
        media_source = article["source"]["name"] # Finds the name of the media source
        article_description = article["description"] #Finds the description of the article
        article_url = article["url"]          #Finds the url of the article



    #This chunk of code finds the image url of the article and adds it onto the dictionary
    # The point of it is so that a photo can be attached with the article on the website.

    # Right now it only works with reuters articles.
#         if media_source == "Reuters":
#             image_inside_article_url = image_capture(article_url)
#         else: # This else statement is only there so that the next if statement works.
#             image_inside_article_url = "empty_string"

#         # Checks if image_capture() function has returned an empty_string or not.
#         if image_inside_article_url == "empty_string":
#             image_inside_article_url = image_capture_database(title)
        
        image_inside_article_url = None

    #This if-statement ensures that the country is in the description
    # of the article, this ensures that the news is from the country inputted.
        if country_inputted not in article_description:
                continue

        if "climate change" not in article_description:
            continue

    # Save the variables in a dictionary.
        data = {

            "Media": media_source,
            "Article Title": title,
            "Description": article_description,
            "Article URL": article_url,
            "Image URL": image_inside_article_url,

        }

        list_of_related_articles.append(data)

    return list_of_related_articles
