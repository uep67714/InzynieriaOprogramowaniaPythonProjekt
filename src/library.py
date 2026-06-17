from typing import List, Dict, Optional
from src.book import Book
from src.reader import Reader
from src.book_rental import BookRental
from src.author import Author

class Library:
    def __init__(self) -> None:
        self.authors: Dict[int, Author] = {}
        self.books: Dict[int, Book] = {}
        self.readers: Dict[int, Reader] = {}
        self.rentals: Dict[int, BookRental] = {}
        self._next_author_id: int = 1
        self._next_book_id: int = 1
        self._next_reader_id: int = 1
        self._next_book_rental_id: int = 1

    def add_author(self, first_name: str, last_name: str) -> Author:
        """ Dodaje nowego autora do biblioteki
        Args:
            first_name (str): Imię autora
            last_name (str): Nazwisko autora
        Returns:
            Author: Nowo utworzony obiekt Author
        Efekt:
            - Zapisuje autora w `self.authors` z automatycznie przypisanym identyfikatorem
            - Inkrementuje `self._next_author_id`
        """
        author_id = self._next_author_id
        author = Author(author_id, first_name, last_name)
        self.authors[self._next_author_id] = author
        self._next_author_id += 1
        return author

    # task_1
    def add_book(self, author_id: int, isbn: str, title: str, year: int) -> Book:
        """
        Dodaje nową książkę do biblioteki. Autor musi istnieć przed książką

        Raises:
            ValueError: Jeśli autor o podanym ID nie istnieje w systemie
        """
        if author_id not in self.authors:
            raise ValueError(f"Nie można dodać książki. Autor o ID {author_id} nie istnieje.")

        author_object = self.authors[author_id]
        book_id = self._next_book_id

        book = Book(book_id, isbn, title, author_object, year)
        self.books[book_id] = book
        self._next_book_id += 1
        return book

    # task_1
    def add_reader(self, first_name: str, last_name: str, email: str) -> Reader:
        """
        Dodaje nowego czytelnika do biblioteki
        """
        reader_id = self._next_reader_id
        reader = Reader(reader_id, first_name, last_name, email)

        self.readers[reader_id] = reader
        self._next_reader_id += 1
        return reader

    # task_1
    def find_reader_by_last_name(self, last_name: str) -> List[Reader]:
        """
        Wyszukuje czytelników po nazwisku (wielkość liter nie ma znaczenia).
        Może zwrócić więcej niż jednego czytelnika o tym samym nazwisku.
        """
        found_readers = []
        for reader in self.readers.values():
            if reader.last_name.lower() == last_name.lower():
                found_readers.append(reader)
        return found_readers

    # task_1
    def find_author_by_last_name(self, last_name: str) -> List[Author]:
        """
        Wyszukuje autorów po nazwisku (wielkość liter nie ma znaczenia).
        Może zwrócić więcej niż jednego autora o tym samym nazwisku.
        """
        found_authors = []
        for author in self.authors.values():
            if author.last_name.lower() == last_name.lower():
                found_authors.append(author)
        return found_authors

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