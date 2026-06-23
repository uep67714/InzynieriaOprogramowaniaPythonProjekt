from typing import List, Optional

class Autor:
    def __init__(self, autor_id: int, imie: str, nazwisko: str):
        self.autor_id: int = autor_id
        self.imie: str = imie
        self.nazwisko: str = nazwisko

class Wypozyczenie:
    def __init__(self, wypozyczenie_id: int, czytelnik_id: int, isbn: str):
        self.wypozyczenie_id: int = wypozyczenie_id
        self.czytelnik_id: int = czytelnik_id
        self.isbn: str = isbn
        self.status: str = "aktywne"

class Czytelnik:
    def __init__(self, czytelnik_id: int, imie: str, nazwisko: str):
        self.czytelnik_id: int = czytelnik_id
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.aktywne_wypozyczenia: List[Wypozyczenie] = []

    def __str__(self) -> str:
        wypozyczenia_str = ", ".join([str(w.wypozyczenie_id) for w in self.aktywne_wypozyczenia if w.status == "aktywne"])
        return f"Czytelnik: {self.imie} {self.nazwisko} (ID: {self.czytelnik_id}) | Aktywne wypożyczenia ID: [{wypozyczenia_str}]"

class Ksiazka:
    def __init__(self, isbn: str, tytul: str, autor: Autor):
        self.isbn: str = isbn
        self.tytul: str = tytul
        self.autor: Autor = autor