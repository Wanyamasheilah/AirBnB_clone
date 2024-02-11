#!/usr/bin/python3
"""This file defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiations
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiations(unittest.TestCase):
    """Unittests for testing different instantiations of the BaseModel class"""

    def test_no_argument(self):
        b1 = BaseModel()
        self.assertEqual(BaseModel, type(b1))

    def test_new_instance_in_objectss(self):
        b1 = BaseModel()
        self.assertIn(b1, models.storage.all().values())

    def test_the_id_str(self):
        b1 = BaseModel()
        self.assertEqual(str, type(b1.id))

    def test_type_datetime(self):
        b1 = BaseModel()
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_public_datetime(self):
        b1 = BaseModel()
        self.assertEqual(datetime, type(b1.updated_at))

    def test_two_models_ids(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_two_models_different_created_at(self):
        base_1 = BaseModel()
        sleep(0.06)
        base_2 = BaseModel()
        self.assertLess(base_1.created_at, base_2.created_at)

    def test_two_models_different_updated_at(self):
        b1 = BaseModel()
        sleep(0.08)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_str_rep(self):
        dateee = datetime.today()
        dateee_repr = repr(dateee)
        bm = BaseModel()
        bm.id = "1234567890"
        bm.created_at = bm.updated_at = dateee
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (1234567890)", bmstr)
        self.assertIn("'id': '1234567890'", bmstr)
        self.assertIn("'created_at': " + dateee_repr, bmstr)
        self.assertIn("'updated_at': " + dateee_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_init_with_kwargs(self):
        dateee = datetime.today()
        dateee_iso = dateee.isoformat()
        bm = BaseModel(id="345678", created_at=dateee_iso,
                       updated_at=dateee_iso)
        self.assertEqual(bm.id, "345678")
        self.assertEqual(bm.created_at, dateee)
        self.assertEqual(bm.updated_at, dateee)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        dateee = datetime.today()
        dateee_iso = dateee.isoformat()
        bm = BaseModel("12", id="3456", created_at=dateee_iso,
                       updated_at=dateee_iso)
        self.assertEqual(bm.id, "3456")
        self.assertEqual(bm.created_at, dateee)
        self.assertEqual(bm.updated_at, dateee)


class TestBaseModel_saved(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("storage.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("storage.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "storage.json")
        except IOError:
            pass

    def test_one_save(self):
        basee_ = BaseModel()
        sleep(0.05)
        first_updated_at = basee_.updated_at
        basee_.save()
        self.assertLess(first_updated_at, basee_.updated_at)

    def test_two_saves(self):
        basee_ = BaseModel()
        sleep(0.06)
        first_updated_at = basee_.updated_at
        basee_.save()
        second_updated_at = basee_.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.06)
        basee_.save()
        self.assertLess(second_updated_at, basee_.updated_at)

    def test_save_with_arg(self):
        basee_ = BaseModel()
        with self.assertRaises(TypeError):
            basee_.save(None)

    def test_save_updates_file(self):
        basee_ = BaseModel()
        basee_.save()
        basee_id = "BaseModel." + basee_.id
        with open("storage.json", "r") as f:
            self.assertIn(basee_id, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        basee = BaseModel()
        self.assertTrue(dict, type(basee.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        basee = BaseModel()
        self.assertIn("id", basee.to_dict())
        self.assertIn("created_at", basee.to_dict())
        self.assertIn("updated_at", basee.to_dict())
        self.assertIn("__class__", basee.to_dict())

    def test_to_dict_contains_added_attributes(self):
        basee = BaseModel()
        basee.name = "Holbert"
        basee.my_number = 928
        self.assertIn("name", basee.to_dict())
        self.assertIn("my_number", basee.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        basee = BaseModel()
        basee_dict = basee.to_dict()
        self.assertEqual(str, type(basee_dict["created_at"]))
        self.assertEqual(str, type(basee_dict["updated_at"]))

    def test_to_dict_output(self):
        dateee = datetime.today()
        basee = BaseModel()
        basee.id = "123456"
        basee.created_at = basee.updated_at = dateee
        tdict = {
            "id": "123456",
            "__class__": "BaseModel",
            "created_at": dateee.isoformat(),
            "updated_at": dateee.isoformat(),
        }
        self.assertDictEqual(basee.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        basee = BaseModel()
        self.assertNotEqual(basee.to_dict(), basee.__dict__)

    def test_to_dict_with_arg(self):
        basee = BaseModel()
        with self.assertRaises(TypeError):
            basee.to_dict(None)


if __name__ == "__main__":
    unittest.main()
