import unittest
from click.testing import CliRunner
from ksoft.cli import cli

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_cli_init(self):
        """Test the CLI init command"""
        result = self.runner.invoke(cli, ["init"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("✅ Environment initialized successfully!", result.output)

    def test_cli_add_module(self):
        """Test adding a module via CLI"""
        result = self.runner.invoke(cli, ["add", "test_module", "--description", "A test module"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("✅ Module 'test_module' added successfully!", result.output)

    def test_cli_list_modules(self):
        """Test listing modules via CLI"""
        result = self.runner.invoke(cli, ["list"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("📦", result.output)  # Assuming at least one module exists

if __name__ == "__main__":
    unittest.main()
