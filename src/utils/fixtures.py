from src.library import Library

def load_initial_data(library: Library) -> None:

    sap = library.add_author("Andrzej", "Sapkowski")
    tol = library.add_author("J.R.R.", "Tolkien")
    orw = library.add_author("George", "Orwell")

    # task_1
    # library.add_book(sap.id, "9788375906592", "Ostatnie życzenie", 1993)
    # library.add_book(tol.id, "9788374805780", "Krew elfów", 1994)
    # library.add_book(orw.id, "9788324404551", "Władca Pierścieni", 1954)
    # library.add_book(orw.id, "9788328712345", "Rok 1984", 1949)

    # task_1
    # library.add_reader("Jan", "Kowalski", "jan.kowalski@email.com")
    # library.add_reader("Anna", "Nowak", "anna.nowak@email.com")
    # reader = library.add_reader("Piotr", "Zieliński", "piotr.zielinski@email.com")

    # task_2
    # library.rent_book("9788328712345", reader.id)