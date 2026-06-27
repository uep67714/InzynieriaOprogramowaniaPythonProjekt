from datetime import datetime
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
        """Wypożycza dostępny egzemplarz książki czytelnikowi.

        Czytelnik może mieć maksymalnie jedno aktywne wypożyczenie książki
        z tym samym numerem ISBN.
        """
        # find_reader, walidacja
        if reader_id not in self.readers:
            raise ValueError(f"Czytelnik o ID {reader_id} nie istnieje.")
        reader = self.readers[reader_id]

        if self.find_book_rental_by_isbn_and_reader_id(isbn, reader_id) is not None:
            raise ValueError("Czytelnik ma już aktywne wypożyczenie książki z tym ISBN.")

        # find_available, walidacja
        book = self._find_available_book_by_isbn(isbn)
        if book is None:
            raise ValueError(f"Brak dostępnego egzemplarza książki o ISBN {isbn}.")

        # new BookRental(), wypożyczenie
        rental = BookRental(book, reader, datetime.now())
        self.rentals[self._next_book_rental_id] = rental
        self._next_book_rental_id += 1

        # oznacz książkę jako wypożyczona
        book.change_availability(False)
        return rental

    # task_2
    def _find_available_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """Zwraca pierwszy dostępny egzemplarz książki o podanym ISBN."""
        for book in self.books.values():
            if book.isbn == isbn and book.is_available:
                return book
        return None

    # task_2
    def find_book_by_isbn(self, isbn: str) -> List[Book]:
        """Wyszukuje wszystkie egzemplarze książki o podanym ISBN."""
        return [book for book in self.books.values() if book.isbn == isbn]

    # task_2
    def find_book_rental_by_isbn_and_reader_id(self, isbn: str, reader_id: int) -> Optional[BookRental]:
        """Wyszukuje aktywne wypożyczenie książki po ISBN i ID czytelnika."""
        for rental in self.rentals.values():
            if rental.is_active and rental.reader.id == reader_id and rental.book.isbn == isbn:
                return rental
        return None

    # task_3
    def find_rental_id(self, reader_id: int, isbn: str) -> Optional[int]:
        """
                Wyszukuje ID aktywnego wypożyczenia na podstawie ID czytelnika i ISBN książki.

                Args:
                    reader_id: ID czytelnika.
                    isbn: Numer ISBN książki.

                Returns:
                    ID wypożyczenia (int) lub None, jeśli nie znaleziono.
                """
        rental = self.find_book_rental_by_isbn_and_reader_id(isbn, reader_id)
        if rental:
            for r_id, r_obj in self.rentals.items():
                if r_obj == rental:
                    return r_id
        return None


    # task_3
    def return_book(self, book_rental_id: int) -> None:
        """
        Rejestruje zwrot książki na podstawie ID wypożyczenia.
        Zmienia status książki na dostępną i wyłącza aktywność wypożyczenia.

        Args:
            book_rental_id: ID wypożyczenia.

        Raises:
            ValueError: Jeśli wypożyczenie nie istnieje lub książka już jest zwrócona.
        """
        if book_rental_id not in self.rentals:
            raise ValueError(f"Wypożyczenie o ID {book_rental_id} nie istnieje.")
        rental = self.rentals[book_rental_id]

        if not rental.is_active:
            raise ValueError(f"Książka z wypożyczenia o ID {book_rental_id} została już zwrócona.")

        rental.book.change_availability(True)
        rental.is_active = False

        # task_4
        def get_active_rentals_for_reader(self, reader_id: int) -> List[BookRental]:
            """Zwraca listę aktywnych wypożyczeń dla czytelnika o podanym ID."""
            if reader_id not in self.readers:
                raise ValueError(f"Czytelnik o ID {reader_id} nie istnieje.")
            return [r for r in self.rentals.values() if r.reader.id == reader_id and r.is_active]
