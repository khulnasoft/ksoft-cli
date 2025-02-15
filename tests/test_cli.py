import unittest
from click.testing import CliRunner
from ksoft.cli import cli
from ksoft.core.module_manager import add_module, delete_module
from ksoft.core.database import get_db

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.db = next(get_db())
        self.test_module_name = "test_module"
        self.test_module_description = "A test module"
        add_module(self.db, self.test_module_name, self.test_module_description)

    def tearDown(self):
        delete_module(self.db, self.test_module_name)
        self.db.close()

    def test_cli_init(self):
        """Test the CLI init command"""
        result = self.runner.invoke(cli, ["init"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("✅ Environment initialized successfully!", result.output)

    def test_cli_add_module(self):
        """Test adding a module via CLI"""
        result = self.runner.invoke(cli, ["add", self.test_module_name, "--description", self.test_module_description])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(f"✅ Module '{self.test_module_name}' added successfully!", result.output)

    def test_cli_list_modules(self):
        """Test listing modules via CLI"""
        result = self.runner.invoke(cli, ["list"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("📦", result.output)  # Assuming at least one module exists

if __name__ == "__main__":
    unittest.main()
