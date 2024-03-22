#!/usr/bin/python3
"""
unittests for the base model class
"""


import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.firstbase = BaseModel()
        self.secondbase = BaseModel()

    def test_BaseModelInstanceAttributes(self):
        self.assertIsInstance(self.firstbase, BaseModel)
        self.assertIsInstance(self.secondbase, BaseModel)
        self.assertIsInstance(self.firstbase.id, str)
        self.assertIsInstance(self.firstbase.created_at, datetime)
        self.assertIsInstance(self.firstbase.updated_at, datetime)
        self.assertNotEqual(self.firstbase.id, self.secondbase.id)
    
    def test_save(self):
        current_datetime = datetime.datetime
        self.firstbase.save()
        self.assertEqual(self.firstbase.updated_at, current_datetime)


if __name__ == "__main__":
    unittest.main()
