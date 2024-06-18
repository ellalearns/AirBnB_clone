#!/usr/bin/python3
"""
defines the State class
it inherits from BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    defines the State class
    """
    def __init__(self, state="", **kwargs):
        """
        initializes the State class
        """
        if not kwargs:
            super().__init__()
            self.state = state
        else:
            super().__init__(**kwargs)
            self.state = kwargs.get("state")
