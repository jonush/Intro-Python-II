# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room

        if items == None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"Name: {self.name}, Location: {self.current_room.name}"

    def list_inventory(self):
        print('Use [drop] [item] to drop items')
        print('Your inventory:')
        for i in self.items:
            i.describe()

    def move(self, direction):
        next_room = getattr(self.current_room, direction + '_to', None)
        if next_room != None:
            self.current_room = next_room
            print(f'---\nYou enter the {self.current_room.name}:')
            print(f'{self.current_room.description}')
        else:
            print('---\nThere is no path this way.') 
    
    def explore(self):
        self.current_room.list_inventory()

    def take_item(self, item):
        self.current_room.items.remove(item)
        self.items.append(item)
        action_item = [i for i in self.items if i.name == item.name]
        action_item[0].on_take(action_item[0])
    
    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.items.append(item)
        action_item = [i for i in self.items if i.name == item.name]
        action_item[0].on_drop(action_item[0])