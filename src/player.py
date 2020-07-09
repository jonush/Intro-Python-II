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
        return f"Name: {self.name}, Location: {self.current_room}"