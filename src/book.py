from src.author import Author

class Book:
    def __init__(self, isbn: str, title: str, author: Author, year: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: Author = author
        self.year: int = year
        self.is_available: bool = True

    def change_availability(self, status: bool) -> None:
        # task_2
        pass