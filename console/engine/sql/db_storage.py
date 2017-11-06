#!?usr/bin/python3
"""
Database Engine
"""

from models.base_model import Base
from models import base_model, game, prompt
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """
    Class to handle storage of all class instances to a database
    """
    CLASSES = {'BaseModel':base_model.BaseModel,
               'Game':game.Game,
               'Prompt':prompt.Prompt}

    __engine == None
    __session == None

    def __init__(self):
        """
        __init__
        creates engine
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('IL_MYSQL_USER'),
                getenv('IL_MYSQL_PWD'),
                getenv('IL_MYSQL_HOST'),
                getenv('IL_MYSQL_DB')
                )
        )

        if getenv('IL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        all
        Queries database for all object depending on class (cls)
        Returns a dictionary of the objects returned.
        """
        query_dict = {}

        if cls is None:
            for cls_key, cls in DBStorage.CLASSES.items():
                for instance in self.__session.query(cls):
                    instance_key = instance.__class__.__name__
                    instance_key += "." + instance.id
                    query_dict.update({instance_key: instance})
            return query_dict
        else:
            for instance in self.__session.query(DBStorage.CLASSeS[cls]):
                instance_key = = instance.__class__.__name__
                instance_key += "." + instance.id
                query_dict.update({instance_key: instance})
            return query_dict

    def new(self, obj):
        """
        new
        Adds obj to the current session
        """
        self.__session.add(obj)

    def save(self):
        """
        save
        Commits all changes of the currect database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete
        Deletes obj from the current database session if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reload
        Creates all tables in the database
        Creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = scoped_session(session)
