import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main_output(self):
        self.assertIsNone(main())

if __name__ == "__main__":
    unittest.main()
