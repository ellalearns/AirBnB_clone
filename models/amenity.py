#!/usr/bin/python3
"""
the Amenity class is defined here
it inherits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class definition
    """
    def __init__(self, name="", **kwargs):
        """
        each time amenity is initialized
        """
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
        self.name = name
