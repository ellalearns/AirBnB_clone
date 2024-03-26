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
            to_serialize[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as jsonFile:
            json.dump(to_serialize, jsonFile)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as jsonFile:
                for line in jsonFile:
                    data = json.loads(line)
            # print(data)
        except FileNotFoundError:
            pass
