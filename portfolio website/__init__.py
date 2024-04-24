# This file contains the Flask app for my Portfolio Website
# Developed and maintained by Salman Ahmad.
# Created on 24-4-2024


# importing some important libraries and classes
from flask import Flask, render_template

# initializing our app object
app = Flask(__name__)

# setting jinga2 to remove backspaces from the html code
# These two lines of code will remove extra spacing from HTML code
# when it is rendered on the webpage, to download and process it faster by the browser
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True


# writing ENDPOINTS for the website
# home
@app.route("/")
def home():
    return render_template("home.html", title="ZED | HOME")


# contact
@app.route("/contact/")
def contact():
    return render_template("contact.html", title="ZED | CONTACT")


# about
@app.route("/about/")
def about():
    return render_template("about.html", title="ZED | ABOUT")


# running our app
app.run()
