from __future__ import annotations
from src.library import Library

class ConsoleController:
    def __init__(self, library: Library) -> None:
        self.library = library

    def run(self) -> None:
        print("Witaj w systemie zarządzania biblioteką!")
        while True:
            self._show_main_menu()
            choice = input("Wybierz akcję: ").strip()
            if choice == "0":
                break
            elif choice == "1":
                self._show_add_menu()
            elif choice == "2":
                self._show_search_menu()
            else:
                print("Nieprawidłowa opcja, spróbuj jeszcze raz")

    def _show_main_menu(self) -> None:
        print("\n=== MENU GŁÓWNE ===")
        print("1. Dodawanie")
        print("2. Wyszukiwanie")
        print("0. Wyjście")

    def _show_add_menu(self) -> None:
        while True:
            print("\n--- Dodawanie: wybierz typ rekordu ---")
            print("1. Autor")
            print("2. Książka")
            print("3. Czytelnik")
            print("0. Powrót do menu głównego")
            choice = input("Wybierz nowy rekord: ").strip()
            if choice == "0":
                return
            elif choice == "1":
                self._add_author()
            elif choice == "2":
                self._add_book()
            elif choice == "3":
                self._add_reader()
            else:
                print("Nieprawidłowa opcja w menu Dodawanie.")

    def _show_search_menu(self) -> None:
        while True:
            print("\n--- Wyszukiwanie: wybierz typ rekordu ---")
            print("1. Autor")
            print("2. Czytelnik")
            print("0. Powrót do menu głównego")
            choice = input("Wybierz akcję: ").strip()
            if choice == "0":
                return
            elif choice == "1":
                self._search_author()
            elif choice == "2":
                self._search_reader()
            else:
                print("Nieprawidłowa opcja w menu Wyszukiwanie.")

    def _add_author(self) -> None:
        print("\n-- Dodawanie nowego autora --")
        first_name = input("Podaj imię autora: ").strip()
        last_name = input("Podaj nazwisko autora: ").strip()
        if not first_name or not last_name:
            print("Imię i nazwisko są wymagane. Anulowano dodawanie.")
            return
        try:
            author = self.library.add_author(first_name, last_name)
            print(f"Dodano autora: {author.get_full_name()}")
        except Exception as exc:
            print("Wystąpił błąd podczas dodawania autora:", exc)

    def _add_book(self) -> None:
        print("\n-- Dodawanie nowej książki --")
        try:
            author_id_str = input("Podaj ID autora: ").strip()
            if not author_id_str:
                print("ID autora jest wymagane.")
                return
            author_id = int(author_id_str)

            title = input("Podaj tytuł książki: ").strip()
            isbn = input("Podaj numer ISBN: ").strip()
            year_str = input("Podaj rok wydania: ").strip()

            if not title or not isbn or not year_str:
                print("Wszystkie pola są wymagane. Anulowano dodawanie.")
                return

            year = int(year_str)

            book = self.library.add_book(author_id, isbn, title, year)
            print(f"Dodano książkę: '{book.title}' o numerze ISBN: {book.isbn} (ID egzemplarza: {book.id})")
        except ValueError:
            print("Błąd: ID autora oraz rok wydania muszą być liczbami całkowitymi!")
        except Exception as exc:
            print("Wystąpił błąd podczas dodawania książki:", exc)

    def _add_reader(self) -> None:
        print("\n-- Dodawanie nowego czytelnika --")
        first_name = input("Podaj imię czytelnika: ").strip()
        last_name = input("Podaj nazwisko czytelnika: ").strip()
        email = input("Podaj adres e-mail: ").strip()

        if not first_name or not last_name or not email:
            print("Wszystkie pola są wymagane. Anulowano dodawanie.")
            return
        try:
            reader = self.library.add_reader(first_name, last_name, email)
            print(f"Dodano czytelnika: {reader.get_full_name()} (ID: {reader.id})")
        except Exception as exc:
            print("Wystąpił błąd podczas dodawania czytelnika:", exc)

    def _search_author(self) -> None:
        print("\n-- Wyszukiwanie autora po nazwisku --")
        last_name = input("Podaj nazwisko autora: ").strip()
        if not last_name:
            print("Nazwisko nie może być puste.")
            return

        authors = self.library.find_author_by_last_name(last_name)
        if not authors:
            print(f"Nie znaleziono autorów o nazwisku '{last_name}'.")
        else:
            print(f"Znalezieni autorzy ({len(authors)}):")
            for author in authors:
                print(f"- ID: {author.id} | {author.get_full_name()}")

    def _search_reader(self) -> None:
        print("\n-- Wyszukiwanie czytelnika po nazwisku --")
        last_name = input("Podaj nazwisko czytelnika (lub jego część): ").strip()
        if not last_name:
            print("Nazwisko nie może być puste.")
            return

        readers = self.library.find_reader_by_last_name(last_name)
        if not readers:
            print(f"Nie znaleziono czytelników o nazwisku '{last_name}'.")
        else:
            print(f"Znalezieni czytelnicy ({len(readers)}):")
            for reader in readers:
                print(f"- ID: {reader.id} | {reader.get_full_name()} | E-mail: {reader.email}")
