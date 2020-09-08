from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape

#Create Flask
app = Flask(__name__)
#Establish Mongo COnnection

mongo=PyMongo(app, uri="mongodb://localhost:27017/mars")

@app.route("/")
def home():

    data = mongo.db.collection.find_one()

    return render_template("index.html", mars_data=data)

@app.route("/scrape")
def scrape():

    mars_info = scrape.scrape_info()

    mongo.db.collection.update({}, mars_info, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)