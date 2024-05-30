#APPLICATION MENU
def main_menu():
    print("\n1. Wyświetl listy zakupów")
    print("2. Dodaj nową listę")
    print("3. Zapisz i zakończ\n")

def list_menu():
    print("\n\t1. Wybierz listę")
    print("\t2. Usuń listę")
    print("\t3. Wstecz\n")

def list_products_menu():
    print("\n\t\t1. Wyświetl produkty na liście")
    print("\t\t2. Dodaj produkt do listy")
    print("\t\t3. Usuń produkt z listy")
    print("\t\t4. Wstecz\n")

#ADD PRODUCT ERROR MESSAGES
def add_item_failure(list_name: str):
    print("\n\t\tBłąd! Produkt nie został dodany do listy " + list_name)