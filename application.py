import util.menu_printer as menu_printer
from  handlers.list_handler import ListHandler

class Application:
    
    def __init__(self) -> None:
        self.list_handler = ListHandler()
        self.run()

    def run(self):
        while True: 
            menu_printer.main_menu()
            opt = read_input()
            if opt == 1:
                self.list_handler.print_shopping_lists()
                while True:
                    menu_printer.list_menu()
                    list_menu_opt = read_input(indent=1)
                    if list_menu_opt == 1:
                        list_id = read_input("Podaj ID listy: ", 1)
                        self.list_handler.select_list_by_id(list_id)
                        self.list_products_opertation()
                    if list_menu_opt == 2:
                        print("PLACEHOLDER FOR DELETE LIST")
                        break
                    if list_menu_opt == 3:
                        break
                    opt = None
            if opt == 3:
                break
    
    def list_products_opertation(self):
        while True:
            menu_printer.list_products_menu()
            list_products_opt = read_input(indent=2)
            if list_products_opt == 1:
                self.list_handler.print_list_items()
            if list_products_opt == 2:
                item = {
                    "name": read_input_str("Podaj nazwę produktu: ", 2),
                    "package_kind": read_input_str("kilogramy czy opakowania (kg/op): ", 2),
                    "amount": read_input_str("Podaj ilość: ", 2)
                }
                self.list_handler.add_item(item)
            if list_products_opt == 3:
                print("3")
            if list_products_opt == 4:
                break

def read_input(prefix = ">>", indent = 0):
    try:
        return int(input(("\t" * indent) + prefix))
    except ValueError:
        print("\nWARTOŚĆ NIEPRAWIDŁOWA!\n")
    
def read_input_str(prefix, indent = 0):
    return input(("\t" * indent) + prefix)


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