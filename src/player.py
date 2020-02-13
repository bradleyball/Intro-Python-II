# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


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


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.print = None
        self.items = []

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return f"Room({repr(self.name)} , {repr(self.current_room)})"

    def set_items(self, new_items):
        self.items.append(new_items)

    def clear_items(self):
        self.items = []

    def set_room(self, direction):
        if self.current_room.name == "Outside Cave Entrance":
            print(direction)
            if direction == "n":
                self.current_room = room["foyer"]

        elif self.current_room.name == "Foyer":
            if direction == "n":
                self.current_room = room["overlook"]
            if direction == "s":
                self.current_room = room["outside"]
            if direction == "e":
                self.current_room = room["narrow"]

        elif self.current_room.name == "Grand Overlook":
            if direction == "s":
                self.current_room = room["foyer"]

        elif self.current_room.name == "Narrow Passage":
            if direction == "n":
                self.current_room = room['treasure']
            if direction == "w":
                self.current_room = room["foyer"]
