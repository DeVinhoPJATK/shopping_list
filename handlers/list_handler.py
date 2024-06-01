from models.list import List
from models.package_kind import PackageKind
import handlers.file_handler as file_handler
from util.menu_printer import add_item_failure, remove_item_failure, remove_list_failure, create_list_failure, select_list_failure

class ListHandler:

    def __init__(self):
        self.loaded_lists = []
        self.selected_list = None

    def print_shopping_lists(self):
        lists = file_handler.load_lists()
        print("\n\tAktualnie posiadane listy:")
        for i, name in enumerate(lists):
            self.loaded_lists.append({"id": i + 1, "list_name": name})
            print("\t#" + str(i + 1) + ". " + name)

    def select_list_by_id(self, id: int):
        for shopping_list in self.loaded_lists:
            if shopping_list["id"] == id:
                list_json = file_handler.load_file_as_json(shopping_list["list_name"])
                self.selected_list = List.from_dict(list_json)
                return True
        select_list_failure()
        print("\tNie istnieje lista o podanym numerze.")
        return False
    
    def print_list_items(self):
        if self.selected_list is None:
            print("\nNIE WYBRANO ŻADNEJ LISTY\n")
            return
        self.selected_list.print_items()

    def add_item(self, item: dict):
        package_kind_values = [kind.value for kind in PackageKind]
        if item["package_kind"] not in package_kind_values:
            add_item_failure(self.selected_list.name)
            print("\t\tNiepoprawny rodzaj. Dozwolone rodzaje: " + str(package_kind_values))
            return 
        if item["package_kind"] == "kg":
            try:
                item["amount"] = float(item["amount"])
            except ValueError:
                add_item_failure(self.selected_list.name)
                print(f"\t\tDla wybranego rodzaju ({item['package_kind']}) ilość musi być wartością liczbową (całkowita lub zmiennoprzecinkowa).")
        elif item["package_kind"] == "op":
            try:
                item["amount"] = int(item["amount"])
            except ValueError:
                add_item_failure(self.selected_list.name)
                print(f"\t\tDla wybranego rodzaju ({item['package_kind']}) ilość musi być wartością liczbową całkowitą.")
        self.selected_list.add_item(item)
        file_handler.save(self.selected_list)
        print("\t\tProdukt dodany.")

    def remove_item(self, item_id: int):
        if item_id < 1 or item_id > len(self.selected_list.items):
            remove_item_failure(self.selected_list.name)
            print("\t\tNie można usunąć produktu, brak produktu o podanym numerze.")
            return
        self.selected_list.remove_item(item_id - 1)
        file_handler.save(self.selected_list)
        print("\t\tProdukt usunięty.")
    
    def remove_list(self, list_id: int):
        if list_id < 1 or list_id > len(self.loaded_lists):
            remove_list_failure()
            print("\tNie istnieje lista o podanym numerze.")
            return
        list_name = self.loaded_lists[list_id - 1]["list_name"]
        is_removed = file_handler.remove_file(list_name)
        if is_removed:
            print(f"\tList {list_name} została usunięta")
            self.loaded_lists.pop(list_id - 1)
            self.selected_list = None
        else:
            print(f"Wystąpił nieznany błąd, lista nie została usnięta")

    def create_list(self, list_name: str):
        if list_name == "":
            create_list_failure()
            print(f"Nazwa listy nie może być pusta")
            return
        list = List(list_name)
        if file_handler.exists(list.name):
            create_list_failure()
            print(f"Lista '{list_name}' już istnieje")
            return
        file_handler.create_list(list)
        print(f"Lista {list_name} została utworzona")