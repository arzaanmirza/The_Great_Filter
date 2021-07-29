from app import app
from flask import render_template, request, redirect, url_for


@app.route('/', methods=["POST","GET"])
def search():
    if request.method == "POST":
        country = request.form["query"]
        return redirect(url_for("country_page", name_of_country=country))
    else:
        return render_template("home.html")


@app.route("/<name_of_country>", methods=["POST","GET"])
def country_page(name_of_country):
    print(name_of_country)
    if request.method == "POST":
        country = request.form["query"]
        return redirect(url_for("country_page", name_of_country=country))
    else:
        return render_template("index.html")

# You are able to take the function call of the country name. Now you have to take the country
# and put it through the functions that you have created to return results. Once you have returned the results
# you have to find a way to display them on a html file. 
