from models.list_item import ListItem
import datetime

class List:

    def __init__(self, name: str) -> None:
        self.name = name
        self.created_at = datetime.datetime.now()
        self.items = []

    def add_item(self, item: ListItem):
        self.items.append(item)

    def remove_item(self, item: ListItem):
        try:
            self.items.remove(item)
        except ValueError:
            print("Taki element nie istnieje")

    def to_dict(self):
        return {
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "items": [item.to_dict() for item in self.items]
        }
    
    @staticmethod
    def from_dict(data):
        list_obj = List(name=data["name"])
        list_obj.created_at = datetime.datetime.fromisoformat(data["created_at"])
        list_obj.items = [ListItem.from_dict(item) for item in data["items"]]
        return list_obj