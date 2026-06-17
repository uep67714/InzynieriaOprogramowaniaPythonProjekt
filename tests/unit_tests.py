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

if __name__ == '__main__':
    unittest.main()
