#!/usr/bin/python3
""" This file manage all the database """

from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)

class DBSstorage:
    """Writes a DBStorage class to manage object storage in a MySQL database."""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database engine (self.__engine) and session (self.__session)."""

        envi = getenv('HBNB_ENV')
        my_user = getenv('HBNB_MYSQL_USER')
        my_psswd = getenv('HBNB_MYSQL_PWD')
        my_host = getenv('HBNB_MYSQL_HOST')
        my_datab = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(my_user, my_psswd,
                                              my_host, my_datab),
                                      pool_pre_ping=True)

        if envi == "test":
                Base.metadata.drop_all(self.__engine)