import util.menu_printer as menu_printer
from  handlers.list_handler import ListHandler

class Application:
    
    def __init__(self) -> None:
        self.list_handler = ListHandler()
        self.run()

    def run(self):
        while True: 
            menu_printer.main_menu()
            opt = int(input(">> "))
            if opt == 1:
                self.list_handler.print_shopping_lists()
                menu_printer.select_shopping_list()
                while True:
                    opt = int(input(">> "))
                    if opt == 1:
                        list_id = int(input("Podaj ID listy: "))
                        self.list_handler.select_list_by_id(list_id)
                    if opt == 2:
                        print("PLACEHOLDER FOR DELETE LIST")
                        break
            if opt == 3:
                break

if __name__ == "__main__":
    Application()

# 1. Wyświetl listy zakupów
    # super_lista (12.01.2024)
    # lista_lidl (31.02.2024)

    # 1. Wybierz listę (po ID)
        # JEŚLI LISTA ISTNIEJE
        # 1. Wyświetl prodkuty na liście
            # 1. pomidory (1kg)
            # 2. kawa (1op)
            # 3. herbata (1op)
        # 2. Dodaj produkt do listy
            # Podajemy podstwaowe informacje o produkcie, jeśli wszystkie dane są poprawne, dodajemy do listy
        # 3. Usuń produkt z listy (po ID)
            # JEŚLI PRODUKT ISTNIEJE, USUWAMY, KONIEC PRZYPADKU
    # 2. Usuń listę (po nazwie)
        # LISTA USUNIĘTA, KONIEC PRZYPADKU

# 2. Dodaj nową listę