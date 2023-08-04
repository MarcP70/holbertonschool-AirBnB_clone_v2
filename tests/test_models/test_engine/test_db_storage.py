#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.state import State


class InvalidClass:  # Define the class 'InvalidClass'
    pass


class InvalidObject:  # Define the class 'InvalidObject'
    pass


class TestDBStorage(unittest.TestCase):
    # Tests that a new instance of DBStorage can be created without errors
    def test_create_instance(self):
        db = storage.DBStorage()  # Correctly import DBStorage from
        'models.storage'
        self.assertIsInstance(db, storage.DBStorage)

    # Tests that all() method returns a dictionary of all objects in
    #   the database
    def test_all_method(self):
        db = storage.DBStorage()  # Correctly import DBStorage from
        # 'models.storage'
        result = db.all()
        self.assertIsInstance(result, dict)

    # Tests that new() method adds an object to the current database session
    def test_new_method(self):
        db = storage.DBStorage()
        state = State(name='California')
        db.new(state)
        result = db.all(State)
        self.assertIn(state, result.values())

    # Tests that save() method commits all changes to the current database
    #   session
    def test_save_method(self):
        db = storage.DBStorage()
        state = State(name='California')
        db.new(state)
        db.save()
        result = db.all(State)
        self.assertIn(state, result.values())

    # Tests that delete() method deletes an object from the current database
    #   session
    def test_delete_method(self):
        db = storage.DBStorage()
        state = State(name='California')
        db.new(state)
        db.save()
        db.delete(state)
        result = db.all(State)
        self.assertNotIn(state, result.values())

    # Tests that reload() method creates all tables in the database and
    #   initializes a new session
    def test_reload_method(self):
        db = storage.DBStorage()
        state = State(name='California')
        db.new(state)
        db.save()
        db.reload()
        result = db.all(State)
        self.assertNotIn(state, result.values())

    # Tests that all() method returns an empty dictionary if there are
    #   no objects in the database
    def test_all_method_empty_db(self):
        db = storage.DBStorage()
        result = db.all()
        self.assertEqual(result, {})

    # Tests that all() method raises an error if an invalid class is
    #   passed as an argument
    def test_all_method_invalid_class(self):
        db = storage.DBStorage()
        with self.assertRaises(NameError):
            db.all(InvalidClass)

    # Tests that new() method raises an error if an invalid object is
    #   passed as an argument
    def test_new_method_invalid_object(self):
        db = storage.DBStorage()
        with self.assertRaises(AttributeError):
            db.new(InvalidObject)
