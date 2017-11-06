#!/usr/bin/python3
"""
Unittest for file_storage.py
"""

#import uuid
#from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import pep8
import unittest

class TestFileStorage(unittest.TestCase):
    """
    Class for testing FileStorage class
    """
    def test_fs_pep8(self):
        """
        Confirm filestorage.py is in PEP8 Style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def setUp(self):
        """
        setUp
        Called once before each test
        """
        self.new_fs_inst = FileStorage()

    def tearDown(self):
        """
        tearDown
        Called once after each test.
        """
        if os.path.exists("improv_live.json"):
            try:
                os.remove("improv_live.json")
            except:
                pass

    def test_all(self):
        """
        Test all() method
        """
        explicit = self.new_fs_inst._FileStorage__objects
        implicit = self.new_fs_inst.all()
        self.assertEqual(explicit, implicit)

    def test_new(self):
        """
        Test new(obj) method
        """
        dict_before = self.new_fs_inst._FileStorage__objects
        new_bm_inst = BaseModel()
        FileStorage.new(self, new_bm_inst)
        dict_after = self.new_fs_inst._FileStorage__objects
        self.assertTrue(len(dict_before) + 1, len(dict_after))

    def test_save(self):
        """
        Test save() method
        """
        # test length of ./improv_live.json before save and after
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                read_data = file.read()
                chars_before = len(read_data)
        except:
            chars_before = 0

        new_bs_obj = BaseModel()
        new_bs_obj.save()

        try:
            with open(FileStorage._FileStorage__file_path, mode="r") as file:
                read_data = file.read()
                chars_after = len(read_data)
        except Exception as e:
            print(e)

        self.assertTrue(chars_before < chars_after)

    def test_reload(self):
        """
        Test reload() method
        """
        in_dict = False
        new_bm_obj = BaseModel()
        bm_id = new_bm_obj.id
        new_bm_obj.save()
        self.new_fs_inst.reload()
        all_obj = self.new_fs_inst.all()
        for key in all_obj.keys():
            if bm_id in key:
                in_dict = True
        self.assertTrue(in_dict)

if __name__ == '__main__':
    unittest.main()
