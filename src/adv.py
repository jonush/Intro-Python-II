import textwrap
from room import Room
from player import Player

# Declare all the rooms
# a dictionary of rooms created from the Room class
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Greetings adventurer! What is your name? ')
player = Player(name, room['outside'].name)

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    print(f'~ {player.current_room} ~')

    if player.current_room == room['outside'].name:
        print(room['outside'].description)
        choice = input(f'-\n{player.name}, Would you like to enter the cave? [y] [n] \nTo quit [q]\n')
        if choice == 'y':
            player.current_room = room['outside'].n_to.name
            print('-\nYou head into the ' + player.current_room + '.')
        elif choice == 'q':
            print(f'Thank you for playing, {player.name}!')
            break
        else:
            print('You made it all the way here! Oh well, maybe next time.')
            break
    elif player.current_room == room['foyer'].name:
        print(room['foyer'].description)
        choice = input('-\nWhich direction wold you like to move in? [n] [s] [e] [w] \nTo quit [q]\n')
        if choice == 'n':
            player.current_room = room['foyer'].n_to.name
            print('-\nYou moved into ' + player.current_room + '.')
        elif choice == 's':
            player.current_room = room['foyer'].s_to.name
            print('-\nYou head back ' + player.current_room + '.')
        elif choice == 'w':
            print('-\nThere is no entrance on this side.')
        elif choice == 'e':
            player.current_room = room['foyer'].e_to.name
            print('-\nYou squeeze into the ' + player.current_room + '.')
        elif choice == 'q':
            print(f'Thank you for playing, {player.name}!')
            break
        else:
            print('Which way would you like to go?')
    elif player.current_room == room['overlook'].name:
        print(room['overlook'].description)
        choice = input('-\nWhich direction wold you like to move in? [n] [s] [e] [w] \nTo quit [q]\n')
        if choice == 'n':
            print('-\nThere is no entrance on this side.')
        elif choice == 's':
            player.current_room = room['overlook'].s_to.name
            print('-\nYou head back ' + player.current_room + '.')
        elif choice == 'e':
            print('-\nThere is no entrance on this side.')
        elif choice == 'w':
            print('-\nThere is no entrance on this side.')
        elif choice == 'q':
            print(f'Thank you for playing, {player.name}!')
            break
        else:
            print('Which way would you like to go?')
    elif player.current_room == room['narrow'].name:
        print(room['narrow'].description)
        choice = input('-\nWhich direction wold you like to move in? [n] [s] [e] [w] \nTo quit [q]\n')
        if choice == 'n':
            player.current_room = room['narrow'].n_to.name
            print('-\nYou find yourself inside the ' + player.current_room + '.')
        elif choice == 's':
            print('-\nThere is no entrance on this side.')
        elif choice == 'e':
            print('-\nThere is no entrance on this side.')
        elif choice == 'w':
            player.current_room = room['narrow'].w_to.name
            print('You head back into the ' + player.current_room + '.')
        elif choice == 'q':
            print(f'Thank you for playing, {player.name}!')
            break
        else:
            print('Which way would you like to go?')
    elif player.current_room == room['treasure'].name:
        print(room['treasure'].description)
        choice = input('-\nYou were too slow! Head back the way you came. [s] \nTo quit [q]\n')
        if choice == 'n':
            print('-\nThere is no entrance on this side.')
        elif choice == 's':
            player.current_room = room['treasure'].s_to.name
            print('You leave the Treasure Chamber and head back into the ' + player.current_room + '.')
        elif choice == 'e':
            print('-\nThere is no entrance on this side.')
        elif choice == 'w':
            print('-\nThere is no entrance on this side.')
        elif choice == 'q':
            print(f'Thank you for playing, {player.name}!')
            break
        else:
            print('Which way would you like to go?')
    else:
        print('It seems you are located somewhere that should not exist.')
        break
