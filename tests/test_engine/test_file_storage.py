#!usr/bin/python3
"""
unittests for the file storage class
"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):
    """
    test class cases for file storage
    """

    def setUp(self):
        self.firstStorage = FileStorage()

    def test_all(self):
        """
        tests that new objects are correctly saved
        in __objects of FileStorage
        """
        self.returned_all = self.firstStorage.all()
        self.assertEqual(dict, type(self.returned_all))

    def test_new(self):
        """
        confirms that a new object gets added
        to __objects of FileStorage
        """
        self.newbasemodel = BaseModel()
        self.newbasemodel2 = BaseModel()
        self.newbasemodel3 = BaseModel()

        self.thekey = "BaseModel." + self.newbasemodel.id
        self.thekey2 = "BaseModel." + self.newbasemodel2.id
        self.thekey3 = "BaseModel." + self.newbasemodel3.id

        self.assertIn(self.thekey, self.firstStorage.all())
        self.assertIn(self.thekey2, self.firstStorage.all())
        self.assertIn(self.thekey3, self.firstStorage.all())

    def test_save(self):
        """
        confirms that json data was correctly
        written to file
        """
        self.anotherbasemodel = BaseModel()
        self.itskey1 = "BaseModel." + self.anotherbasemodel.id

        self.anotherbasemodel2 = BaseModel()
        self.anotherbasemodel3 = BaseModel()
        self.itskey2 = "BaseModel." + self.anotherbasemodel2.id
        self.itskey3 = "BaseModel." + self.anotherbasemodel3.id

        self.firstStorage.save()
        with open("ModelObjects.json", "r", encoding="utf-8") as storageFile:
            data = json.load(storageFile)

        self.assertTrue(self.itskey1 in data)
        self.assertTrue(self.itskey2 in data)
        self.assertTrue(self.itskey3 in data)

    # def test_reload(self):
    #     """
    #     ensures that file storage is correctly loaded
    #     """
    #     self.abasemodel = BaseModel()
    #     self.akey = "BaseModel." + self.abasemodel.id


if __name__ == "__main__":
    unittest.main()
