import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.database as database
from src.repository import LibraryRepository

class TestLibraryRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        database.DB_NAME = "test_library.db"
        database.create_tables()
        cls.repo = LibraryRepository()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("test_library.db"):
            os.remove("test_library.db")

    def test_a_add_and_get_book(self):
        success = self.repo.add_book("Nutuk", "Mustafa Kemal Ataturk", "9781111111111")
        self.assertTrue(success)
        books = self.repo.get_all_books()
        self.assertEqual(len(books), 1)

    def test_b_add_member(self):
        success = self.repo.add_member("Ahmet Yilmaz", "ahmet@email.com")
        self.assertTrue(success)

    def test_c_loan_and_return_book(self):
        loan_success = self.repo.loan_book(1, 1)
        self.assertTrue(loan_success)
        return_success = self.repo.return_book(1)
        self.assertTrue(return_success)

if __name__ == "__main__":
    unittest.main()
