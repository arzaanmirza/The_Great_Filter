from flask import render_template, request, redirect, url_for, Flask
from get_feature_news import get_feature_news
from get_personal_api_news import get_personal_api_news
import json
import os
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def search():

    feature_news = get_feature_news()

    if request.method == "POST":
        country = request.form["query"]
        return redirect(url_for("country_page", name_of_country=country))
    else:
        return render_template("home.html", feature_news=feature_news)


@app.route("/<name_of_country>", methods=["POST","GET"])
def country_page(name_of_country):


    latest_api_news_data = get_personal_api_news(name_of_country)
    # This is where the data files will get merged together into one list
    # which will be sent to the render_template.
    data_to_send = latest_api_news_data
    # If the returning articles list is empty then redirect it to the home search page.
    if not data_to_send:
        return redirect(url_for("search"))

    if request.method == "POST":
        country = request.form["query"]
        return redirect(url_for("country_page", name_of_country=country))
    else:
        return render_template("index.html",country=name_of_country,data=data_to_send)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(port=5000,debug=True)