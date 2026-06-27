# System Zarządzania Biblioteką

## Opis Projektu

Celem jest stworzenie systemu wspierającego proces wypożyczania książek, zarządzania zbiorami oraz bazą czytelników.

## Funkcjonalności

- Dodawanie nowych książek, autorów i czytelników do bazy danych.
- Obsługa procesu wypożyczenia książki dla konkretnego czytelnika.
- Wyszukiwanie wypożyczeń oraz obsługa zwrotów.

## Struktura Działania

System opiera się na architekturze modularnej, gdzie poszczególne klasy odpowiadają za element systemu (Książka, Czytelnik, Wypożyczenie). Procesy walidacji są zintegrowane bezpośrednio w logice wypożyczania.

## Opis Zespołu i Podział Zadań

- **Jesika Księżniakiewicz** – Implementacja modułu zarządzania autorami i książkami.
- **Mateusz Marciniak** – Logika biznesowa systemu wypożyczeń.
- **Viktoriia Tyshchenko** – Implementacja walidacji wypożyczeń oraz wyszukiwarka czytelników.
- **Anna Wyrwał** – Rozszerzenie widoku czytelnika, testy integracyjne oraz dokumentacja projektu.
- **Maciej Gryszkiewicz** – Setup projektu, podział prac, definicja modeli.
