#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    __engine = None
    __session = None
    list = ["User", "Amenity", "Place", "City", "State", "Review"]
    def __init__(self):
        """Function Docs"""
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}",
            pool_pre_ping=True,
        )

        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        list = ["User", "Amenity", "Place", "City", "State", "Review"]
        dicti = dict()
        if cls is not None:
            if cls in list:
                clss = eval(cls)
                rows = self.__session.query(clss).all()
                for row in rows:
                    print(row)
                    instance = "{}.{}".format(cls, row.id)
                    dicti [instance] = row
            return dicti
        else:
            for class_name in list:
                rows = self.__session.query(class_name).all()
                for row in rows:
                    instance = "{}.{}".format(class_name, row.id)
                    dicti[instance] = row
            return dicti

    def get(self, cls, id):
        if cls is not None:
            if cls in self.list:
                clss = eval(cls)
                rows = self.__session.query(clss).all()
                for row in rows:
                    if row.id == id:
                        return row
        return None
    
    def count(self, cls=None):
        n = 0
        if cls is not None:
            if cls in self.list:
                clss = eval(cls)
                rows = self.__session.query(clss).all()  # 'rows' is assigned here
            for row in rows:  # Reference to 'rows' without guaranteed assignment
                n = n + 1
            return n
        else:
            for cls in self.list:
                clss = eval(cls)
                rows = self.__session.query(clss).all()  # 'rows' is assigned here
                for row in rows:  # Reference to 'rows' without guaranteed assignment
                    n = n + 1
            return n



    def new(self, obj):
        if obj is not None:
            self.__session.add(obj)
    def save(self):
        self.__session.commit()
    def delete(self, obj):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload method """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
        sessionmaker(bind=self.__engine, expire_on_commit=False)
      )
        self.__session = Session()
  
