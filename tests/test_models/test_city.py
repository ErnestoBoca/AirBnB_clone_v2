#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest

class test_City(test_basemodel):
    """ """
    
    @unittest.skip("Skip test_state_id")
    def test_state_id(self):
        """ """
        new = City(state_id="3e282943-01b3-4eb1-a742-ee6615a970ca")
        self.assertEqual(type(new.state_id), str)

    @unittest.skip("Skip test_name")
    def test_name(self):
        """ """
        new = City(name="New York")
        self.assertEqual(type(new.name), str)
