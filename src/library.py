from typing import List, Optional
from src.models import Autor, Ksiazka, Czytelnik, Wypozyczenie

class Biblioteka:
    def __init__(self):
        self.autorzy: List[Autor] = []
        self.ksiazki: List[Ksiazka] = []
        self.czytelnicy: List[Czytelnik] = []
        self.wypozyczenia: List[Wypozyczenie] = []
        self._nastepne_wypozyczenie_id: int = 1

    def dodaj_autora(self, autor_id: int, imie: str, nazwisko: str) -> Autor:
        autor = Autor(autor_id, imie, nazwisko)
        self.autorzy.append(autor)
        return autor

    def dodaj_ksiazke(self, isbn: str, tytul: str, autor_id: int) -> Optional[Ksiazka]:
        autor = next((a for a in self.autorzy if a.autor_id == autor_id), None)
        if not autor: return None
        ksiazka = Ksiazka(isbn, tytul, autor)
        self.ksiazki.append(ksiazka)
        return ksiazka

    def dodaj_czytelnika(self, czytelnik_id: int, imie: str, nazwisko: str) -> Czytelnik:
        czytelnik = Czytelnik(czytelnik_id, imie, nazwisko)
        self.czytelnicy.append(czytelnik)
        return czytelnik

    def wypozycz_ksiazke(self, isbn: str, czytelnik_id: int) -> Optional[Wypozyczenie]:
        czytelnik = next((c for c in self.czytelnicy if c.czytelnik_id == czytelnik_id), None)
        if not czytelnik: return None
        nowe_wyp = Wypozyczenie(self._nastepne_wypozyczenie_id, czytelnik_id, isbn)
        self._nastepne_wypozyczenie_id += 1
        self.wypozyczenia.append(nowe_wyp)
        czytelnik.aktywne_wypozyczenia.append(nowe_wyp)
        return nowe_wyp

   
    def wyszukaj_numer_wypozyczenia(self, isbn: str, czytelnik_id: int) -> Optional[int]:
        for wyp in self.wypozyczenia:
            if wyp.isbn == isbn and wyp.czytelnik_id == czytelnik_id and wyp.status == "aktywne":
                return wyp.wypozyczenie_id
        return None

    def zwroc_ksiazke(self, wypozyczenie_id: int) -> bool:
        wypozyczenie = next((w for w in self.wypozyczenia if w.wypozyczenie_id == wypozyczenie_id and w.status == "aktywne"), None)
        if not wypozyczenie: return False
        wypozyczenie.status = "zwrócono"
        czytelnik = next((c for c in self.czytelnicy if c.czytelnik_id == wypozyczenie.czytelnik_id), None)
        if czytelnik:
            czytelnik.aktywne_wypozyczenia = [w for w in czytelnik.aktywne_wypozyczenia if w.wypozyczenie_id != wypozyczenie_id]
        return True

    def wyszukaj_czytelnika_po_id(self, czytelnik_id: int) -> Optional[Czytelnik]:
        return next((c for c in self.czytelnicy if c.czytelnik_id == czytelnik_id), None)