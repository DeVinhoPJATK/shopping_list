from models.list_item import ListItem
from models.package_kind import PackageKind
import json

class Application:
    
    def __init__(self) -> None:
        while True: 
            self.display_main_menu()
            opt = int(input(">> "))
            if opt == 3:
                break

    def display_main_menu(self):
        print("1. Wyświetl listy zakupów")
        print("2. Dodaj nową listę")
        print("3. Zapisz i zakończ")

item = ListItem("Pomidor", 1.2, PackageKind.KG)
item_json = json.dumps(item.to_dict())
print(item_json)

if __name__ == "__main__":
    Application()

# 1. Wyświetl listy zakupów
    # super_lista (12.01.2024)
    # lista_lidl (31.02.2024)

    # 1. Wybierz listę (po nazwie)
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