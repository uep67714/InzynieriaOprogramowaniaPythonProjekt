from src.author import Author

class Book:
    """Klasa reprezentująca książkę w bibliotece"""

    def __init__(self, book_id: int, isbn: str, title: str, author: Author, year: int) -> None:
        """
        Inicjalizuje obiekt książki
        """
        self.id = book_id
        self.isbn = isbn
        self.title = title
        self.author: Author = author
        self.year = year
        self.is_available = True

    def change_availability(self, status: bool) -> None:
        # task_2
        """Ustawia dostępność egzemplarza książki."""
        self.is_available = status