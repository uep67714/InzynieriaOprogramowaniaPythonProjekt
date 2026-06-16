class Author:
    """Klasa reprezentująca autora książki"""

    def __init__(self, author_id: int, first_name: str, last_name: str) -> None:
        """
        Inicjalizuje obiekt autora
        """
        self.id = author_id
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self) -> str:
        """Zwraca pełne imię i nazwisko autora"""
        return f"{self.first_name} {self.last_name}"