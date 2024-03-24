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

    the_time = datetime.datetime

    def __init__(self, *args, **kwargs):
        """
        initializes the base model
        uses **kwargs if present
        """

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, self.the_time.fromisoformat(value))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.the_time.now()
            self.updated_at = self.the_time.now()


    def __str__(self):
        result = "[{}] ({}) {}".format(type(self).__name__,
                                       self.id, self.__dict__)
        return result

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = self.the_time.now()
        return (self.updated_at)

    def to_dict(self) -> dict:
        """
        adds the object attributes
        and other details required
        into a python dict
        and returns that python dict
        """
        result_dict = {}
        result_dict = self.__dict__
        result_dict["__class__"] = type(self).__name__
        result_dict["created_at"] = str(result_dict["created_at"].isoformat())
        result_dict["updated_at"] = str(result_dict["updated_at"].isoformat())

        return result_dict
