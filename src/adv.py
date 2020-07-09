import sys
import textwrap
from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance", """North of you, the cave mount beckons."""),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness.Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# MAIN -----------------------------------------------------------------------------------------
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playing = False

game_start = input('Would you like to start the adventure game? [y] [n]\n').lower()
if game_start == 'y':
    playing = True
else:
    print('Maybe next time then!')
    sys.exit()

name = input('Greetings adventurer! What is your name? ')
player = Player(name, room['outside'])
print('-\n(Press [q] at anytime to quit the game)\n-\n')
print('You are currently at the ' + player.current_room.name + '.')

sword = Item('sword', 'a shiny sword')
shield = Item('shield', 'a sturdy shield')
spear = Item('spear', 'a pointy spear')
chest = Item('chest', 'an empty chest')

room['foyer'].items.append(spear)
room['overlook'].items.append(sword)
room['overlook'].items.append(shield)
room['treasure'].items.append(chest)

def get_player_inv():
    for i in player.items:
        print(f'•{i.name}: {i.description}')
        return

def get_room_inv(r_items):
    if not r_items:
        print('> There are no items in this room.')
        return
    elif len(r_items) < 2:
        print('You found an item in this room!')
        print(f'•{r_items[0].name}')
    else:
        print('You found items in this room!')
        for i in r_items:
            print(f'•{i.name}')

def take_item(item):
    print('You picked up this item.')

while playing == True:
    action = input('Which way would you like to go? [n] [s] [e] [w]\nInteract with items using: [get] [item], [take] [item], or [drop] [item]\nCheck your inventory using: [inventory] or [i]\n').lower()

    if action == 'q':
        sys.exit()
    else:
        next_room = getattr(player.current_room, f'{action}_to', None)
        if next_room == None:
            print('\n---\nThere is no path this way. Try a different direction.\n')
        else:
            player.current_room = next_room
            print(f'\n---\nYou arrive at the {player.current_room.name}')
            get_room_inv(player.current_room.items)
            print('---\n')

## get player inventory       
    # if action == 'i' or 'inventory':
    #     print('\n---\nYour inventory:')
    #     get_player_inv()
    #     print('---\n')

# OLD ATTEMPT ----------------------------------------------------------------------------------
    # if choice == 'q':
    #     playing = False
    #     print(f'Thanks for playing, {player.name}!')
    # elif choice == 'n':
    #     if hasattr(player.current_room, 'n_to'):
    #         player.current_room = player.current_room.n_to
    #         print('\n---\n~ You enter the ' + player.current_room.name + ' ~\n---\n')
    #     else:
    #         print('[X] There is no path this way.')
    # elif choice == 's':
    #     if hasattr(player.current_room, 's_to'):
    #         player.current_room = player.current_room.s_to
    #         print('\n---\n~ You enter the ' + player.current_room.name + ' ~\n---\n')
    #     else:
    #         print('[X] There is no way to get through.')
    # elif choice == 'e':
    #     if hasattr(player.current_room, 'e_to'):
    #         player.current_room = player.current_room.e_to
    #         print('\n---\n~ You enter the ' + player.current_room.name + ' ~\n---\n')
    #     else:
    #         print('[X] There is no door this way.')
    # elif choice == 'w':
    #     if hasattr(player.current_room, 'w_to'):
    #         player.current_room = player.current_room.w_to
    #         print('\n---\n~ You enter the ' + player.current_room.name + ' ~\n---\n')
    #     else:
    #         print('[X] This is a dead end.')
    # else:
    #     print('Please enter a valid direction: [n] [s] [e] [w]\nOr press [q] to quit\n')