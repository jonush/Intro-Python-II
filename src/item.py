class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, item):
        print(f'You picked up the {item.name}')

    def on_drop(self, item):
        print(f'You dropped the {item.name}')

    def print_name(self):
        print(f'• {self.name}')

    def describe(self):
        print(f'• {self.name}: {self.description}')