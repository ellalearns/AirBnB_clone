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
    def __init__(self):
        """
        each time user is initialized
        """
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
