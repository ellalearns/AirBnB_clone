#!/usr/bin/python3
"""
unittests for the base model class
"""


import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.firstbase = BaseModel()
        self.secondbase = BaseModel()

    def test_BaseModelInstanceAttributes(self):
        self.assertIsInstance(self.firstbase, BaseModel)
        self.assertIsInstance(self.secondbase, BaseModel)
        self.assertIsInstance(self.firstbase.id, str)
        self.assertIsInstance(self.firstbase.created_at, datetime.datetime)
        self.assertIsInstance(self.firstbase.updated_at, datetime.datetime)
        self.assertNotEqual(self.firstbase.id, self.secondbase.id)

    def test_save(self):
        self.assertIsInstance(self.firstbase.save(), datetime.datetime)

    def test_str(self):
        supposed_result = '[{}] ({}) {}'\
            .format(type(self.firstbase).__name__,
                    self.firstbase.id,
                    self.firstbase.__dict__)
        returned_result = self.firstbase.__str__()
        self.assertEqual(supposed_result, returned_result)

    def test_to_dict(self):

        # create custom attributes for object
        self.firstbase.name = "myBase"
        self.firstbase.number = 77

        # check if the returned dict contains all the attributes it should
        returned_dict = self.firstbase.to_dict()
        should_contain = ['id', 'created_at', 'updated_at',
                          'name', 'number', '__class__']
        for key in should_contain:
            self.assertIn(key, returned_dict)

        # check if the class key value is correct
        self.assertEqual(returned_dict['__class__'],
                         type(self.firstbase).__name__)

        # check if the dates are in correct format
        ret_created_date = returned_dict['created_at']
        ret_updated_date = returned_dict['updated_at']
        regex_p = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$'

        self.assertRegex(ret_created_date, regex_p)
        self.assertRegex(ret_updated_date, regex_p)


if __name__ == "__main__":
    unittest.main()
