import unittest
from fastapi.testclient import TestClient
from ksoft.api.main import app
from ksoft.core.database import get_db
from ksoft.core.module_manager import add_module, delete_module

client = TestClient(app)

class TestAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.db = next(get_db())
        self.test_module_name = "test_module"
        self.test_module_description = "A test module"
        add_module(self.db, self.test_module_name, self.test_module_description)

    def tearDown(self):
        delete_module(self.db, self.test_module_name)
        self.db.close()

    def test_root_route(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to KSoft API"})

    def test_list_modules_route(self):
        response = client.get("/modules")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_module_name, [module["name"] for module in response.json()["modules"]])

if __name__ == "__main__":
    unittest.main()
