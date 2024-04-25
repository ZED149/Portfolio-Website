# This file contains the Flask app for my Portfolio Website
# Developed and maintained by Salman Ahmad.
# Created on 24-4-2024


# importing some important libraries and classes
from flask import Flask, render_template, abort
from project import Project

# initializing our app object
app = Flask(__name__)

# dummy DB for now
projects: [Project] = [Project("Habit Tracking WebApp",
                               "img/habit-tracking.png",
                               "img/habit-tracking-hero.png",
                               ['python', 'web'],
                               "habit-tracking",
                               "https://udemy.com"),
                       Project("Personal Finance Tracking app with React",
                               "img/personal-finance.png",
                               "img/personal-finance.png",
                               ['react', 'javascript'],
                               "personal-finance"),
                       Project("REST API Documentation with Postman and Swagger",
                               "img/rest-api-docs.png",
                               "img/rest-api-docs.png",
                               ['writing'],
                               "api-docs")]

# storing dict form of our projects
projects = [p.get() for p in projects]

# storing project slugs
project_slugs = {
    project["slug"]: project for project in projects
}

# setting jinga2 to remove backspaces from the html code
# These two lines of code will remove extra spacing from HTML code
# when it is rendered on the webpage, to download and process it faster by the browser
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True


# writing ENDPOINTS for the website
# home
@app.route("/")
def home():
    return render_template("home.html", title="ZED | HOME",
                           projects=projects)


# contact
@app.route("/contact/")
def contact():
    return render_template("contact.html", title="ZED | CONTACT")


# about
@app.route("/about/")
def about():
    return render_template("about.html", title="ZED | ABOUT")


# slug for each project
@app.route("/project/<string:slug>")
def project(slug):
    if slug not in project_slugs:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project=project_slugs[slug])


# handling errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# running our app
app.run()
