#!/usr/bin/python3
"""
the Review class is defined here
it inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class definition
    """
    def __init__(self,
                 place_id="",
                 user_id="",
                 text="",
                 **kwargs):
        """
        each time review is initialized
        """
        if not kwargs:
            super().__init__()
        else:
            super().__init__(**kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
