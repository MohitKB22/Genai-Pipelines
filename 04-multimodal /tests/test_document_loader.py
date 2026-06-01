import os
import unittest
from src.document_loader import DocumentLoader

class TestDocumentLoader(unittest.TestCase):
    def setUp(self):
        self.loader = DocumentLoader()
        self.test_dir = 'data/sample_docs'
        os.makedirs(self.test_dir, exist_ok=True)

        # Create a sample text file for testing
        with open(os.path.join(self.test_dir, 'test.txt'), 'w') as f:
            f.write("This is a test document.")

    def tearDown(self):
        # Clean up the test directory after tests
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_load_text_file(self):
        documents = self.loader.load(self.test_dir)
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0].page_content, "This is a test document.")

    def test_load_non_existent_directory(self):
        with self.assertRaises(FileNotFoundError):
            self.loader.load('non_existent_directory')

    def test_load_empty_directory(self):
        empty_dir = 'data/empty_docs'
        os.makedirs(empty_dir, exist_ok=True)
        documents = self.loader.load(empty_dir)
        self.assertEqual(len(documents), 0)
        os.rmdir(empty_dir)

if __name__ == '__main__':
    unittest.main()