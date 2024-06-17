#!/usr/bin/python3

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()


def all_classes():
    """
    return all available classes
    """
    from models.base_model import BaseModel
    return {
        "BaseModel": BaseModel
    }


all_classes = all_classes()
