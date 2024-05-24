

# This file contains the Project class

# importing important libraries
import sqlite3
import os


class Project:
    """
    Creates an instance of the project containing various project attributes
    for the website.
    """

    # Private data members
    __name: str = ""                    # Name of the Project
    __thumbnail: str = ""               # Thumbnail Image of the Project
    __hero: str = ""                    # Hero Image for the Project
    __categories: [str] = []            # Categories around which project revolves
    __slug: str = ""                    # Slug for the project
    __technologies_used: [str] = []     # Technologies Used in this project
    __title: str = ""                   # Title to show on the HTML Document
    __prod: str = ""                    # Production Link of the project

    # Constructor

    # Default Constructor
    def __init__(self, name: str, thumbnail: str, hero: str, categories: [str]
                 , slug: str, technologies_used: [str], title: str, prod: str = "#"):
        """
        Initializes the private variables and sets the context of the object.
        :param name: Name of the project
        :param thumbnail: path to the thumbnail of the project
        :param hero: path to the hero of the project
        :param categories: list of categories of the project
        :param slug: slug of the project
        :param technologies_used: list of technologies used in the project.
        :param title: title of the project.
        :param prod: link of the project in the production
        """
        # initializing private variables
        self.__name = name
        self.__thumbnail = thumbnail
        self.__hero = hero
        self.__categories = categories
        self.__slug = slug
        self.__technologies_used = technologies_used
        self.__title = title
        self.__prod = prod

    # Getters

    # get all
    def get(self) -> dict:
        """
        Returns the project details in a dict.
        :return: dictionary of the project details
        """

        temp: dict = {
            "name": self.__name,
            "thumbnail": self.__thumbnail,
            "hero": self.__hero,
            "categories": self.__categories,
            "slug": self.__slug,
            "technologies_used": self.__technologies_used,
            "title": self.__title,
            "prod": self.__prod
        }

        return temp

    @classmethod
    # get project slugs
    def get_project_slugs(cls, projects: []) -> {}:
        """
        Returns a dict of project slugs. {slugs: project}
        :param projects: list of dictionary containing projects.
        :return: dictionary of projects containing slugs as keys and project dictionary's as values.
        """
        return {project['slug']: project for project in projects}

    # load projects from DB
    @classmethod
    def load_projects_from_db(cls, database_filename) -> []:
        """
        Loads the projects from the SQLite database and returns a list of projects.
        :return: A list of projects.
        """

        base = os.path.abspath("databases/")
        db_path = f"{base}/{database_filename}"

        # making connection to the database.
        conn = sqlite3.connect(db_path)
        # creating cursor
        cursor = conn.cursor()
        # reading all entries from db
        query = """
        SELECT * FROM "projects"
        """
        # executing query
        cursor.execute(query)
        # fetching data
        data = cursor.fetchall()
        # closing connection to DB
        conn.close()
        # Now we need to initialize each project
        projects: [Project] = []
        for entry in data:
            # we need to insert categories as a list
            # converting from str to list
            categories_temp = [category for category in entry[3].split(", ")]
            technology_used_temp = [tech for tech in entry[7].split(", ")]
            # initializing and appending each Project object
            projects.append(Project(entry[0], entry[1], entry[2], categories_temp,
                                    entry[4], technology_used_temp, entry[8], entry[5]))

        return projects
