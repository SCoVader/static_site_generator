import unittest
from main import extract_title

class TestMain(unittest.TestCase):
    def test_title_extraction(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("test of a multiple line\n# TITLE EXTRACTION\nI hope it works :)"), "TITLE EXTRACTION")

if __name__ == "__main__":
    unittest.main()