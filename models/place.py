#!/usr/bin/python3
"""
the Place class is defined here
it inherits from BaseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class definition
    """
    def __init__(self, **kwargs):
        """
        each time place is initialized
        """
        if not kwargs:
            super().__init__()
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = ""
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
        else:
            super().__init__(**kwargs)
            self.city_id = kwargs.get("city_id")
            self.user_id = kwargs.get("user_id")
            self.name = kwargs.get("name")
            self.description = kwargs.get("description")
            self.number_rooms = kwargs.get("number_rooms")
            self.number_bathrooms = kwargs.get("number_bathrooms")
            self.max_guest = kwargs.get("max_guest")
            self.price_by_night = kwargs.get("price_by_night")
            self.latitude = kwargs.get("latitude")
            self.longitude = kwargs.get("longitude")
            self.amenity_ids = kwargs.get("amenity_ids")
