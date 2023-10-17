import json
import os
import unittest

from task1 import User, load_json, save_json
from user_logger import Logger


class TestUserClass(unittest.TestCase):
    def setUp(self) -> None:
        self.the_id = 1
        self.name = 'Vasya'
        self.level = 1
        self.user_data = {str(self.the_id): {'name': self.name, 'level': self.level}}

    def tearDown(self) -> None:
        if os.path.exists('my_test_json.json'):
            os.remove('my_test_json.json')
        if os.path.exists('my_test_logger.json'):
            os.remove('my_test_logger.json')

    def test_user_creation(self):
        user = User(self.name, self.the_id, self.level)
        self.assertEqual(user.name, self.name)
        self.assertEqual(user.the_id, self.the_id)
        self.assertEqual(user.level, self.level)

    def test_invalid_user_creation(self):
        with self.assertRaises(ValueError):
            User(self.level, self.the_id, self.name)

    def test_successful_user_level_creation(self):
        new_logger = Logger('my_test_logger.json')
        new_logger.__class__.db[str(self.the_id)] = {'name': self.name, 'level': self.level}
        new_logger.__class__.users[self.the_id] = User(self.name, self.the_id, self.level)
        new_logger.authorize(self.the_id, self.name)
        new_level = self.level - 1 if self.level - 1 > 0 else 1
        new_user = new_logger.create_user('new_' + self.name, self.the_id + 1, new_level)
        self.assertEqual(new_user.level, new_level)

    def test_invalid_user_level_creation(self):
        with self.assertRaises(ValueError):
            new_logger = Logger('my_test_logger.json')
            new_logger.__class__.db[str(self.the_id)] = {'name': self.name, 'level': self.level}
            new_logger.__class__.users[self.the_id] = User(self.name, self.the_id, self.level)
            new_logger.authorize(self.the_id, self.name)
            new_level = self.level
            new_user = new_logger.create_user('new_' + self.name, self.the_id + 1, new_level)
            self.assertEqual(new_user.level, new_level)

    def test_succesfull_authorize(self):
        new_logger = Logger('my_test_logger.json')
        new_logger.__class__.db[str(self.the_id)] = {'name': self.name, 'level': self.level}
        new_logger.__class__.users[self.the_id] = User(self.name, self.the_id, self.level)
        new_logger.authorize(self.the_id, self.name)

    def test_invalid_authorize(self):
        with self.assertRaises(PermissionError):
            new_logger = Logger('my_test_logger.json')
            new_logger.authorize(self.the_id * 10, self.name)
        with self.assertRaises(PermissionError):
            new_logger = Logger('my_test_logger.json')
            new_logger.authorize(self.the_id, self.name * 10)

    def test_load_json(self):
        with open('my_test_json.json', 'w', encoding='utf-8') as file:
            json.dump(self.user_data, file)

        loaded_data = load_json('my_test_json.json')
        self.assertEqual(loaded_data, self.user_data)

    def test_save_json(self):
        user_db = self.user_data
        save_json('my_test_json.json', user_db)
        with open('my_test_json.json', 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, user_db)


if __name__ == '__mane__':
    unittest.main()












