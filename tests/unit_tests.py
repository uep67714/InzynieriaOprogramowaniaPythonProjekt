import unittest
from src.library import Library

class LibraryUnitTests(unittest.TestCase):
    def test_add_author_stores_author(self):
        library = Library()
        author = library.add_author("Jan", "Kowalski")

        self.assertIn(1, library.authors)
        self.assertIs(library.authors[1], author)
        self.assertEqual(author.first_name, "Jan")
        self.assertEqual(author.last_name, "Kowalski")

    def test_add_multiple_authors_unique_keys(self):
        library = Library()
        a1 = library.add_author("A1", "One")
        a2 = library.add_author("A2", "Two")

        self.assertEqual(len(library.authors), 2)
        self.assertIn(1, library.authors)
        self.assertIn(2, library.authors)
        self.assertIs(library.authors[1], a1)
        self.assertIs(library.authors[2], a2)

    def test_find_author_by_last_name_success(self):
        library = Library()
        library.add_author("Adam", "Mickiewicz")
        library.add_author("Julian", "Tuwim")
        library.add_author("Jan", "Mickiewicz")

        results = library.find_author_by_last_name("mickiewicz")

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].first_name, "Adam")
        self.assertEqual(results[1].first_name, "Jan")

    def test_find_author_by_last_name_empty_if_not_found(self):
        library = Library()
        library.add_author("Adam", "Mickiewicz")

        results = library.find_author_by_last_name("Nowak")
        self.assertEqual(results, [])

    def test_add_reader_stores_reader(self):
        library = Library()
        reader = library.add_reader("Anna", "Nowak", "anna@email.com")

        self.assertIn(1, library.readers)
        self.assertIs(library.readers[1], reader)
        self.assertEqual(reader.id, 1)
        self.assertEqual(reader.first_name, "Anna")
        self.assertEqual(reader.email, "anna@email.com")

    def test_find_reader_by_last_name_success(self):
        library = Library()
        library.add_reader("Jan", "Kowalski", "jan@email.com")
        library.add_reader("Maria", "Kowalski", "maria@email.com")

        results = library.find_reader_by_last_name("Kowalski")
        self.assertEqual(len(results), 2)

    def test_add_book_success_when_author_exists(self):
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")

        book = library.add_book(author_id=author.id, isbn="123-456", title="Potop", year=1886)

        self.assertIn(1, library.books)
        self.assertIs(library.books[1], book)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Potop")
        self.assertEqual(book.author.last_name, "Sienkiewicz")

    def test_add_book_raises_value_error_if_author_missing(self):
        library = Library()

        with self.assertRaises(ValueError):
            library.add_book(author_id=999, isbn="123-456", title="Potop", year=1886)

    def test_find_book_by_isbn_returns_all_copies(self):
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")
        first_copy = library.add_book(author.id, "978-1", "Potop", 1886)
        second_copy = library.add_book(author.id, "978-1", "Potop", 1886)
        library.add_book(author.id, "978-2", "Quo vadis", 1896)

        results = library.find_book_by_isbn("978-1")

        self.assertEqual(results, [first_copy, second_copy])

    def test_rent_book_creates_rental_and_marks_book_unavailable(self):
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")
        book = library.add_book(author.id, "978-1", "Potop", 1886)
        reader = library.add_reader("Anna", "Nowak", "anna@email.com")

        rental = library.rent_book("978-1", reader.id)

        self.assertIs(rental.book, book)
        self.assertIs(rental.reader, reader)
        self.assertFalse(book.is_available)
        self.assertTrue(rental.is_active)

    def test_rent_book_uses_next_available_copy_for_same_isbn(self):
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")
        first_copy = library.add_book(author.id, "978-1", "Potop", 1886)
        second_copy = library.add_book(author.id, "978-1", "Potop", 1886)
        first_reader = library.add_reader("Anna", "Nowak", "anna@email.com")
        second_reader = library.add_reader("Jan", "Kowalski", "jan@email.com")

        first_rental = library.rent_book("978-1", first_reader.id)
        second_rental = library.rent_book("978-1", second_reader.id)

        self.assertIs(first_rental.book, first_copy)
        self.assertIs(second_rental.book, second_copy)

    def test_rent_book_raises_value_error_if_reader_missing(self):
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")
        library.add_book(author.id, "978-1", "Potop", 1886)

        with self.assertRaises(ValueError):
            library.rent_book("978-1", 999)

    def test_rent_book_raises_value_error_if_no_available_copy(self):
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")
        library.add_book(author.id, "978-1", "Potop", 1886)
        reader = library.add_reader("Anna", "Nowak", "anna@email.com")
        another_reader = library.add_reader("Jan", "Kowalski", "jan@email.com")
        library.rent_book("978-1", reader.id)

        with self.assertRaises(ValueError):
            library.rent_book("978-1", another_reader.id)

    def test_reader_cannot_rent_second_active_book_with_same_isbn(self):
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")
        library.add_book(author.id, "978-1", "Potop", 1886)
        library.add_book(author.id, "978-1", "Potop", 1886)
        reader = library.add_reader("Anna", "Nowak", "anna@email.com")
        library.rent_book("978-1", reader.id)

        with self.assertRaises(ValueError):
            library.rent_book("978-1", reader.id)

    def test_find_rental_id_success(self):
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")
        library.add_book(author.id, "978-1", "Potop", 1886)
        reader = library.add_reader("Anna", "Nowak", "anna@email.com")
        rental = library.rent_book("978-1", reader.id)
        rental_id = library.find_rental_id(reader.id, "978-1")
        self.assertIsNotNone(rental_id)

    def test_return_book_success(self):
        # 1. Przygotowanie danych
        library = Library()
        author = library.add_author("Henryk", "Sienkiewicz")
        book = library.add_book(author.id, "978-1", "Potop", 1886)
        reader = library.add_reader("Anna", "Nowak", "anna@email.com")

        # Używamy podkreślenia "_", aby uniknąć ostrzeżenia o nieużywanej zmiennej
        _ = library.rent_book("978-1", reader.id)

        # 2. Wyszukanie ID wypożyczenia
        rental_id = library.find_rental_id(reader.id, "978-1")

        # 3. Weryfikacja: sprawdzamy czy to na pewno int i czy nie jest None
        self.assertIsInstance(rental_id, int, "rental_id musi być liczbą całkowitą (int)!")

        # 4. Zwrot książki (teraz rental_id jest bezpieczne)
        library.return_book(rental_id)

        # 5. Sprawdzenie stanu końcowego
        self.assertTrue(book.is_available, "Książka powinna być dostępna po zwrocie")
        self.assertFalse(library.rentals[rental_id].is_active, "Wypożyczenie powinno być nieaktywne")


if __name__ == '__main__':
    unittest.main()
