from src.library import Library
from src.utils.fixtures import load_initial_data
from src.ui.console_controller import ConsoleController

def main() -> None:
    library = Library()

    print("Inicjalizacja bazy danych biblioteki...")
    load_initial_data(library)
    print("-" * 30)

    controller = ConsoleController(library)
    try:
        controller.run()
    except KeyboardInterrupt:
        print("\nPrzerwano przez użytkownika. Do widzenia!")

if __name__ == "__main__":
    main()