#!/usr/bin/python3
"""
the City class is defined here
it inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class definition
    """
    def __init__(self, name="", state_id="", **kwargs):
        """
        each time city is initialized
        """
        if not kwargs:
            super().__init__()
            self.name = name
            self.state_id = state_id
        else:
            super().__init__(**kwargs)
            self.name = kwargs.get("name")
            self.state_id = kwargs.get("state_id")
