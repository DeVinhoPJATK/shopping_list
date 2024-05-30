from models.list import List
import handlers.file_handler as file_handler

class ListHandler:

    def __init__(self):
        self.loaded_lists = []
        self.selected_list = None

    def print_shopping_lists(self):
        lists = file_handler.load_lists()
        print()
        for i, name in enumerate(lists):
            self.loaded_lists.append({"id": i + 1, "list_name": name})
            print("\t" + str(i + 1) + ". " + name)
        print()

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