#!/usr/bin/python3

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()


def all_classes():
    """
    return all available classes
    """
    from models.base_model import BaseModel
    from models.user import User
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.review import Review

    return {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }


all_classes = all_classes()
