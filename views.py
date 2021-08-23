from app import app
from flask import render_template, request, redirect, url_for
from get_climatechange_news import get_climatechange_news
from get_naturaldisaster_news import get_naturaldisaster_news
import json

@app.route('/', methods=["POST","GET"])
def search():
    if request.method == "POST":
        country = request.form["query"]
        return redirect(url_for("country_page", name_of_country=country))
    else:
        return render_template("home.html")


@app.route("/<name_of_country>", methods=["POST","GET"])
def country_page(name_of_country):


    # This is where you will get the data from the functions in other files.
    naturaldisaster_data = get_naturaldisaster_news(name_of_country)
    climatechange_data = get_climatechange_news(name_of_country)

    # This is where the data files will get merged together into one list
    # which will be sent to the render_template.
    data_to_send = naturaldisaster_data + climatechange_data

    # If the returning articles list is empty then redirect it to the home search page.
    if not data_to_send:
        return redirect(url_for("search"))

    if request.method == "POST":
        country = request.form["query"]
        return redirect(url_for("country_page", name_of_country=country))
    else:
        return render_template("index.html",country=name_of_country,data=data_to_send)
