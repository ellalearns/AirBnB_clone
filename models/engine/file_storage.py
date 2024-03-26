#!/usr/bin/python3
"""
a file storage engine
serializes instances to json
deserializes json to class instances
"""


import json


class FileStorage():
    """
    """
    __file_path = "ModelObjects.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
        return obj

    def save(self):
        to_serialize = {}
        for key, value in self.__objects.items():
            if type(value) is dict:
                to_serialize[key] = value
            else:
                to_serialize[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as jsonFile:
            json.dump(to_serialize, jsonFile)

    def reload(self):
        pass
        # try:
        #     with open(self.__file_path, "r") as jsonFile:
        #         data = json.load(jsonFile)
        #         print("data loaded -> ", data)
        #         print("objs before ->", self.__objects)
        #         self.__objects = data.copy()
        #         print("objects now ->", self.__objects)
        #     print("point ->", self.__objects)
        # except FileNotFoundError:
        #     pass
