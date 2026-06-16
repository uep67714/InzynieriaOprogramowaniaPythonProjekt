class Reader:
    """Klasa reprezentująca czytelnika biblioteki"""

    def __init__(self, reader_id: int, first_name: str, last_name: str, email: str) -> None:
        """
        Inicjalizuje obiekt czytelnika
        """
        self.id = reader_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_full_name(self) -> str:
        """Zwraca pełne imię i nazwisko czytelnika"""
        return f"{self.first_name} {self.last_name}"