import unittest
from src.library import Library

class LibraryIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.author = self.lib.add_author("Jan", "Kowalski")
        self.reader = self.lib.add_reader("Anna", "Nowak", "anna@test.pl")

    def test_full_rental_flow(self):
        # 1. Pozytywny przepływ (dodanie, wypożyczenie, zwrot)
        book = self.lib.add_book(self.author.id, "123-456", "Testowa", 2026)
        rental = self.lib.rent_book("123-456", self.reader.id)

        # Sprawdzenie czy wypożyczenie istnieje
        r_id = self.lib.find_rental_id(self.reader.id, "123-456")
        self.assertIsNotNone(r_id)

        # Zwrot
        self.lib.return_book(r_id)
        self.assertFalse(self.lib.rentals[r_id].is_active)
        self.assertTrue(self.lib.books[book.id].is_available)

    def test_rental_no_books_available(self):
        # 2. Negatywny: wypożyczenie gdy brak egzemplarzy
        with self.assertRaises(Exception):
            self.lib.rent_book("999", self.reader.id)

    def test_same_reader_same_isbn_restriction(self):
        # 3. Ograniczenie: ten sam czytelnik nie może mieć dwóch egzemplarzy tego samego ISBN
        self.lib.add_book(self.author.id, "111", "K1", 2026)
        self.lib.add_book(self.author.id, "111", "K2", 2026)

        self.lib.rent_book("111", self.reader.id)
        with self.assertRaises(Exception):
            self.lib.rent_book("111", self.reader.id)