import pytest
from src.library import Biblioteka

@pytest.fixture
def biblio():
    b = Biblioteka()
    b.dodaj_autora(1, "H.", "Sienkiewicz")
    b.dodaj_ksiazke("123", "Potop", 1)
    b.dodaj_czytelnika(100, "Jan", "K")
    b.wypozycz_ksiazke("123", 100)
    return b

def test_wyszukaj_sukces(biblio):
    assert biblio.wyszukaj_numer_wypozyczenia("123", 100) == 1

def test_zwrot_sukces(biblio):
    assert biblio.zwroc_ksiazke(1) is True