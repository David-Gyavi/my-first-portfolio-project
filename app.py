import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask (__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRECT_KEY")


mongo = PyMongo(app)



@app.route("/")
@app.route("/get_portfolio")
def get_portfolio():
    portfolio = mongo.db.portfolio.find()
    return render_template("portfolio.html", portfolio=portfolio)

@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("contact.html")  


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)    
