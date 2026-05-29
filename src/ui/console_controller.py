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
            else:
                print("Nieprawidłowa opcja, spróbuj jeszcze raz")

    def _show_main_menu(self) -> None:
        print("\n=== MENU GŁÓWNE ===")
        print("1. Dodawanie")
        print("0. Wyjście")

    def _show_add_menu(self) -> None:
        while True:
            print("\n--- Dodawanie: wybierz typ rekordu ---")
            print("1. Autor")
            print("0. Powrót do menu głównego")
            choice = input("Wybierz nowy rekord: ").strip()
            if choice == "0":
                return
            elif choice == "1":
                self._add_author()
            else:
                print("Nieprawidłowa opcja w menu Dodawanie.")

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
