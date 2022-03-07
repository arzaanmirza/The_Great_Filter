import json
import requests
import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb',region_name='ap-southeast-2',aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

def get_latest_news_api():

    list_of_related_articles = []

    # Get the data from dynamoDB table
    table = dynamodb.Table("News_API")
    response = table.scan()
    items = response['Items']
    
    while 'LastEvaluatedKey' in response:
        print(response['LastEvaluatedKey'])
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])

    return items


def get_personal_api_news():

    items = get_latest_news_api()

    list_of_related_articles = []

    for article in items:

        data = {

            "Media": article['Media'],
            "Article Title": article['Article Title'],
            "Description": article['Description'],
            "Article URL": article['Article URL'],
            "Image URL": article['Image URL'],

        }

        list_of_related_articles.append(data)

    return list_of_related_articles


