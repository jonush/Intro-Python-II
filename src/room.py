# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        
        if items == None:
            self.items = []
        else:
            self.items = items

    def add_item(self, item):
        self.items.append(item)

    def list_inventory(self):
        if len(self.items) == 0:
            print('> There are no items here.')
        elif len(self.items) == 1:
            print('\nYou found an item in this room!')
            print('Use [get] [item] or [take] [item] to pick up items')
        else:
            print('\nYou found items in this room!')
            print('Use [get] [item] or [take] [item] to pick up items')
        for i in self.items:
            i.print_name()
        print('---')
