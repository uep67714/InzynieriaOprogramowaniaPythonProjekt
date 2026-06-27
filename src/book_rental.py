from datetime import datetime
from typing import Optional
from src.book import Book
from src.reader import Reader

MAX_RENTAL_DAYS: int = 14

class BookRental:
    def __init__(self, book: Book, reader: Reader, rental_date: datetime):
        self.book: Book = book
        self.reader: Reader = reader
        self.rental_date: datetime = rental_date
        self.return_date: Optional[datetime] = None
        self.is_active: bool = True