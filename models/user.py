#!/usr/bin/python3
"""
the User class is defined here
it inherits from the BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class definition
    """
    def __init__(self, email="", password="", first_name="", last_name="", **kwargs):
        """
        each time user is initialized
        """
        if not kwargs:
            super().__init__()
            self.email = email
            self.password = password
            self.first_name = first_name
            self.last_name = last_name
        else:
            super().__init__(**kwargs)
            self.email = kwargs.get("email")
            self.password = kwargs.get("password")
            self.first_name = kwargs.get("first_name")
            self.last_name = kwargs.get("last_name")
