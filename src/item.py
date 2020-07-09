class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self, item_name):
        print(f'You have picked up {item_name}')