from room import Room
from player import Player
import random


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

room_items = ["Sword", "Fishing Pole", "Dagger",
              "Staff", "Magazine", "Computer", "Dictionary", "Cat", "Kittens", "Puppies", "Nail Filer", "Cheif Keef's dreadlocks"]

exit = False
player_name = None
current_room = None
player = None


while not exit:

    player_name = input("Enter the name of your player: ")

    if player == '':
        print("\n\n result: No name was typed for player!!\n\n")
        continue

    current_room = input(
        "\nChoose your starting room:\n\n(F)oyer\n(Ov)erlook\n(O)utside\n(E)xit\n>>>")

    current_room = current_room.lower().strip()

    if current_room == '':
        print("\n\n result: No room was selected!\n\n")
        continue
    current_room = current_room[0:2]

    if current_room == "ov":
        current_room = room["overlook"]
    elif current_room[0] == "o":
        current_room = room["outside"]
    elif current_room[0] == "f":
        current_room = room["foyer"]

    break

player = Player(player_name, current_room)


while player.current_room.name != "Treasure Chamber":

    direction = input(
        f"\n {player.current_room.description} \n\n\n which direction do you want to go?\n\n(N)orth\n(S)outh\n(E)ast\n(W)est\n(V)iew inventory\n(D)rop items\n\n>>>")

    direction = direction.lower().strip()
    print(direction)
    if direction == '':
        print(
            f"\n\n result: No direction was selected! You are still in room {player.current_room.name} \n\n")
        continue

    elif direction[0] == "n":
        player.set_room("n")
        player.set_items(random.choice(room_items))
        print(f"You found a new item: {player.items[-1]}!")
        continue
    elif direction[0] == "s":
        player.set_room("s")
        player.set_items(random.choice(room_items))
        print(f"You found a new item: {player.items[-1]}!")
        continue
    elif direction[0] == "e":
        player.set_room("e")
        player.set_items(random.choice(room_items))
        print(f"You found a new item: {player.items[-1]}!")
        continue
    elif direction[0] == "w":
        player.set_room("w")
        player.set_items(random.choice(room_items))
        print(f"You found a new item: {player.items[-1]}!")
        continue
    elif direction[0] == "v":
        print("\n----------------------------------------\n            Current Items")
        for i in player.items:
            print(f"\n{i}")
        print("\n----------------------------------------")
        continue
    elif direction[0] == "d":
        player.clear_items()
        print("\n\nYou lost all your items\n\n")
        continue


print("\n\nWOOOOOHOOOO YOU WON!!!!\n\n")

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
