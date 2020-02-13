# Write a class to hold player information, e.g. what room they are in
# currently.

from adv import room
from room import Room


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
        print("made it")
        print(self.current_room)
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
