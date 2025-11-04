# This file contains the Flask app for my Portfolio Website
# Developed and maintained by Salman Ahmad.
# Created on 24-4-2024
import os.path

# importing some important libraries and classes
from flask import Flask, render_template, abort
from .project import Project

# initializing our app object
app = Flask(__name__)

# loading all projects from db
projects = Project.load_projects_from_db("project.db")

# storing dict form of our projects in a list
projects = [p.get() for p in projects]

# storing project slugs
project_slugs = Project.get_project_slugs(projects=projects)

# setting jinga2 to remove backspaces from the html code
# These two lines of code will remove extra spacing from HTML code
# when it is rendered on the webpage, to download and process it faster by the browser
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True


def create_app():
    # creating app object
    app = Flask(__name__)

    # running our app
    app.run(debug=True)


# writing ENDPOINTS for the website
# home
@app.route("/")
def home():
    return render_template("home.html", title="ZED | HOME",
                           projects=projects, enumerate=enumerate)


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
    technologies_used = project_slugs[slug]['technologies_used']
    title = f"ZED | {project_slugs[slug]['title']}"
    return render_template(
        f"projects/project_{slug}.html",
        project=project_slugs[slug],
        technologies_used=technologies_used,
        title=title)


# handling errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# running our app
if __name__ == "__main__":
    create_app()
