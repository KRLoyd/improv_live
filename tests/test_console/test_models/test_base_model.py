#!/usr/bin/python3
"""
Unittest for base_model.py
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
#from models.base_model import BaseModel.__is_serializable

class TestBaseModel(unittest.TestCase):
    """
    Class for testing base_model
    """

    def setUp(self):
        """
        setUp
        Called once before each test. Creates a new instance of BaseModel
        """
        self.new_inst = BaseModel()

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
        self.assertIsNotNone(obj_dict.get("id"))
        self.assertIsNotNone(obj_dict.get("created_at"))
        self.assertIsNone(obj_dict.get("updated_at"))

        another_bs_inst = BaseModel(name="new obj")
        obj_dict = another_bs_inst.__dict__
        self.assertIsNotNone(obj_dict.get("name"))
        self.assertTrue(obj_dict.get("name") == "new obj")

    def test_add_and_update_attributes(self):
        """
        test_add_and_update_attributes
        Tests that attributes can be added and updated to an instance
        """
        obj = self.new_inst
        self.assertFalse(hasattr(obj, "number"))
        self.assertFalse(hasattr(obj, "name"))
        obj.number = 90
        obj.name = "game"
        self.assertEqual(self.new_inst.name, "game")
        self.assertTrue(hasattr(self.new_inst, "number"))
        obj.name = "fun game"
        self.assertEqual(self.new_inst.name, "fun game")
        delattr(obj, "number")
        self.assertFalse(hasattr(self.new_inst, "number"))

    def test__is_serializable(self):
        """
        test__is_serializable
        Tests method __is_serializable of BaseModel
        """
        func = BaseModel._BaseModel__is_serializable
        a_dict = {"oh":1, 3:"hey there"}
        a_set = {1, 2, 3, 4}
        a_list = ["yo", "this", "is", "a", "list"]
        a_tuple = (3, 4)
        a_datetime = datetime.now()
        a_uuid = uuid.uuid4()
        self.assertTrue(func(self, a_dict))
        self.assertTrue(func(self, 89))
        self.assertTrue(func(self, "string"))
        self.assertTrue(func(self, a_list))
        self.assertTrue(func(self, a_tuple))
        self.assertFalse(func(self, a_set))
        self.assertFalse(func(self, a_datetime))
        self.assertFalse(func(self, a_uuid))

    def test_save(self):
        """
        test_save
        Tests the BaseModel save() method
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
        Tests __str__ method of BaseModel class
        """
        correct_format = "[{}] ({}) {}".format(self.new_inst.__class__.__name__,
                                               self.new_inst.id,
                                               self.new_inst.__dict__)
        self.assertEqual(correct_format, self.new_inst.__str__())

    def test_to_dict(self):
        """
        test_to_dict
        Tests to_dict method of BaseModel class
        """
        obj_dict = BaseModel.to_dict(self.new_inst)
        self.assertEqual(type(obj_dict), dict)

if __name__ == '__main__':
    unittest.main()
