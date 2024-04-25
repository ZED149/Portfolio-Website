

# This file contains the Project class


class Project:
    """
    Creates an instance of the project containing various project attributes
    for the website.
    """

    # Private data members
    __name: str = ""
    __thumbnail: str = ""
    __hero: str = ""
    __categories: [str] = []
    __slug: str = ""
    __prod: str = ""

    # Constructor

    # Default Constructor
    def __init__(self, name: str, thumbnail: str, hero: str, categories: [str]
                 , slug: str, prod: str = "#"):
        """
        Initializes the private variables and sets the context of the object.
        :param name: Name of the project
        :param thumbnail: path to the thumbnail of the project
        :param hero: path to the hero of the project
        :param categories: list of categories of the project
        :param slug: slug of the project
        :param prod: link of the project in the production
        """
        # initializing private variables
        self.__name = name
        self.__thumbnail = thumbnail
        self.__hero = hero
        self.__categories = categories
        self.__slug = slug
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
            "slug": self.__slug
        }
        return temp
