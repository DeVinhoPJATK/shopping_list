from models.list import List
from models.package_kind import PackageKind
import handlers.file_handler as file_handler
from util.menu_printer import add_item_failure

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