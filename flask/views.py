from app import app
from flask import render_template, request, redirect, url_for
from get_climatechange_news import get_climatechange_news
# from example_jsondata_tester import get_naturaldisaster_news
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
    #climatechange_data = get_climatechange_news(name_of_country)

    # Line 26 works with example_jsondata_tester
    #data_to_send = get_naturaldisaster_news(name_of_country)

    # This is where the data files will get merged together into one list
    # which will be sent to the render_template.

    #data_to_send = naturaldisaster_data + climatechange_data
    data_to_send = naturaldisaster_data

    # If the returning articles list is empty then redirect it to the home search page.
    if not data_to_send:
        return redirect(url_for("search"))

    if request.method == "POST":
        country = request.form["query"]
        return redirect(url_for("country_page", name_of_country=country))
    else:
        return render_template("index.html",country=name_of_country,data=data_to_send)









# You are able to take the function call of the country name. Now you have to take the country
# and put it through the functions that you have created to return results. Once you have returned the results
# you have to find a way to display them on a html file.


# Extra code to remember in the future:

# country_check_result = country_checker(name_of_country)
