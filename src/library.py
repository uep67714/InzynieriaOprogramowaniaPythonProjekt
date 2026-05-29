from typing import List, Dict, Optional
from src.book import Book
from src.reader import Reader
from src.book_rental import BookRental
from src.author import Author

class Library:
    def __init__(self):
        self.authors: Dict[int, Author] = {}
        self.books: Dict[int, Book] = {}
        self.readers: Dict[int, Reader] = {}
        self.rentals: Dict[int, BookRental] = {}
        self._next_author_id: int = 1
        self._next_book_id: int = 1
        self._next_reader_id: int = 1
        self._next_book_rental_id: int = 1

    def add_author(self, first_name: str, last_name: str) -> Author:
        author = Author(first_name, last_name)
        self.authors[self._next_author_id] = author
        self._next_author_id += 1
        return author

    # task_1
    def add_book(self, author_id: int, isbn: str, title: str, year: int) -> Book:
        pass

    # task_1
    def add_reader(self, first_name: str, last_name: str, email: str) -> Reader:
        pass

    # task_1
    def find_reader_by_last_name(self, last_name: str) -> List[Reader]:
        pass

    # task_1
    def find_author_by_last_name(self, last_name: str) -> List[Author]:
        pass

    # task_2
    def rent_book(self, isbn: str, reader_id: int) -> BookRental:
        # find_reader, walidacja
        # find_available, walidacja
        # new BookRental(), wypożyczenie
        # oznacz książkę jako wypożyczona
        pass

    # task_2
    def _find_available_book_by_isbn(self, isbn: str) -> Optional[Book]:
        pass

    # task_2
    def find_book_by_isbn(self, isbn: str) -> List[Book]:
        pass

    # task_2
    def find_book_rental_by_isbn_and_reader_id(self, isbn: str, reader_id: int) -> Optional[BookRental]:
        pass

    # task_3
    def return_book(self, book_rental_id: int) -> None:
        pass

    # task_4
    def get_active_rentals_for_reader(self, reader_id: int) -> List[BookRental]:
        pass