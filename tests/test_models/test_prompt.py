#!/usr/bin/python3
"""
Unittest for prompt.py
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.prompt import Prompt

class TestPrompt(unittest.TestCase):
    """
    Class for testing Prompt class
    """

    def setUp(self):
        """
        setUp
        Called once before each test. Creates a new instance of BaseModel
        """
        self.new_inst = Prompt()

    def tearDown(self):
        """
        tearDown
        Called once after each test.
        """
        pass

    def test_init(self):
        """
        test_init
        Tests that the id, created_at, and updated_at are all instantiated
        """
        obj_dict = self.new_inst.__dict__
        self.assertIsInstance(self.new_inst, Prompt)

        another_prompt_inst = Prompt(name="Farmer", p_type="Occupation")
        obj_dict = another_prompt_inst.__dict__
        self.assertIsNotNone(obj_dict.get("name"))
        self.assertTrue(obj_dict.get("name") =="Farmer")
        self.assertIsNotNone(obj_dict.get("p_type"))
        self.assertTrue(obj_dict.get("p_type") == "Occupation")

    def test_add_and_update_attributes(self):
        """
        test_add_and_update_attributes
        Tests that attributes can be added and updated to an instance
        """
        obj = self.new_inst
        self.assertFalse(hasattr(obj, "number"))
        obj.number = 90
        obj.name = "game"
        self.assertEqual(self.new_inst.name, "game")
        self.assertTrue(hasattr(self.new_inst, "number"))
        obj.name = "fun game"
        self.assertEqual(self.new_inst.name, "fun game")
        delattr(obj, "number")
        self.assertFalse(hasattr(self.new_inst, "number"))


    def test_save(self):
        """
        test_save
        Tests that BaseModel save() works for Prompt
        """
        obj_dict = self.new_inst.__dict__
        before = obj_dict.get("updated_at")
        self.new_inst.save()
        obj_dict = self.new_inst.__dict__
        after = obj_dict.get("updated_at")
        self.assertNotEqual(before, after)

    def test__str__(self):
        """
        test__str__
        Tests __str__ method of BaseModel class on Prompt
        """
        correct_format = "[{}] ({}) {}".format(self.new_inst.__class__.__name__,
                                               self.new_inst.id,
                                               self.new_inst.__dict__)
        self.assertEqual(correct_format, self.new_inst.__str__())

    def test_to_dict(self):
        """
        test_to_dict
        Tests to_dict method of BaseModel class for Prompt
        """
        obj_dict = BaseModel.to_dict(self.new_inst)
        self.assertEqual(type(obj_dict), dict)

if __name__ == '__main__':
    unittest.main()
