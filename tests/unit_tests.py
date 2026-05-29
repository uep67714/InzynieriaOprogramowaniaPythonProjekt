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

if __name__ == '__main__':
    unittest.main()
