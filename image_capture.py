# This file captures the url of the first image from an article.
# It takes the html of the article and finds the img src to which the url
# of the image is returned


import requests
import re

def image_capture(url):

    html = requests.get(url)
    text_block = html.text

    pattern = "img src=\"(.*?)\""
    substring = re.search(pattern,text_block)

    if substring is None:
        return "empty_string"

    image_url = substring.group(1)
    return image_url
