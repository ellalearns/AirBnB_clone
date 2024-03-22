#!/usr/bin/python3
"""
this is the base model module
here the base model is defined
and needed attributes and methods
"""


import uuid
import datetime


class BaseModel():
    """
    the main class -- base model
    contains attributes that subclasses...
    ...will inherit
    """


    def __init__(self):
        """
        initializes the base model
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime
        self.updated_at = datetime.datetime


    def __str__(self):
        result = "[Base Model] ({}) {}".format(self.id, self.__dict__)
        return result


    def save(self):
        """
        updates the public instance attribute 
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime
        return (self.updated_at)


    def to_dict(self):
        result_dict = {}


        return result_dict
