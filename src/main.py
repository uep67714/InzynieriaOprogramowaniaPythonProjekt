from src.library import Biblioteka

def menu():
    biblio = Biblioteka()
    biblio.dodaj_autora(1, "Andrzej", "Sapkowski")
    biblio.dodaj_ksiazke("978-83", "Wiedźmin", 1)
    biblio.dodaj_czytelnika(10, "Adam", "Nowak")
    biblio.wypozycz_ksiazke("978-83", 10)

    while True:
        print("\n=== SYSTEM BIBLIOTECZNY ===")
        print("1. Wyszukaj numer wypożyczenia")
        print("2. Zwróć książkę")
        print("3. Wyświetl stan czytelnika")
        print("0. Wyjście")
        
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            isbn = input("Podaj ISBN: ")
            c_id = int(input("Podaj ID czytelnika: "))
            nr = biblio.wyszukaj_numer_wypozyczenia(isbn, c_id)
            print(f"Numer wypożyczenia to: {nr}" if nr else "Nie znaleziono.")
        elif wybor == "2":
            w_id = int(input("Podaj ID wypożyczenia: "))
            print("Zwrócono!" if biblio.zwroc_ksiazke(w_id) else "Błąd zwrotu.")
        elif wybor == "3":
            c_id = int(input("Podaj ID czytelnika: "))
            c = biblio.wyszukaj_czytelnika_po_id(c_id)
            print(c if c else "Brak czytelnika.")
        elif wybor == "0":
            break

if __name__ == "__main__":
    menu()