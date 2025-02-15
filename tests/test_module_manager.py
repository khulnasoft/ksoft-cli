import unittest
from sqlalchemy.orm import Session
from ksoft.core.module_manager import add_module, get_module, delete_module
from ksoft.core.database import get_db

class TestModuleManager(unittest.TestCase):
    def setUp(self):
        self.db = next(get_db())
        self.test_module_name = "test_module"
        self.test_module_description = "A test module"

    def tearDown(self):
        self.db.close()

    def test_add_module(self):
        module = add_module(self.db, self.test_module_name, self.test_module_description)
        self.assertIsNotNone(module)
        self.assertEqual(module.name, self.test_module_name)
        self.assertEqual(module.description, self.test_module_description)

    def test_get_module(self):
        add_module(self.db, self.test_module_name, self.test_module_description)
        module = get_module(self.db, self.test_module_name)
        self.assertIsNotNone(module)
        self.assertEqual(module.name, self.test_module_name)
        self.assertEqual(module.description, self.test_module_description)

    def test_delete_module(self):
        add_module(self.db, self.test_module_name, self.test_module_description)
        result = delete_module(self.db, self.test_module_name)
        self.assertTrue(result)
        module = get_module(self.db, self.test_module_name)
        self.assertIsNone(module)

if __name__ == "__main__":
    unittest.main()
