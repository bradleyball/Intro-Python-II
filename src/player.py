# Write a class to hold player information, e.g. what room they are in
# currently.


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

    def set_room_helper(self, direction, room, print):
        self.current_room = room
        self.print = f"\n\n\n{print}"

    def set_room(self, direction):
        print("made it")
        print(self.current_room)
        if self.current_room == "outside":
            print(direction)
            if direction == "n":
                self.set_room_helper(
                    "n", "outside", "There is no room north of outside, try again!\nYou are in room outside")
            if direction == "s":
                self.set_room_helper(
                    "s", "foyer", "You are now in room foyer")
            if direction == "e":
                self.set_room_helper(
                    "e", "outside", "There is no room east of outside, try again!\nYou are in room outside")
            if direction == "w":
                self.set_room_helper(
                    "w", "outside", "There is no room west of outside, try again!\nYou are in room outside")

        elif self.current_room == "foyer":
            if direction == "n":
                self.set_room_helper(
                    "n", "outside", f"You are now in the outside room ")
            if direction == "s":
                self.set_room_helper(
                    "s", "overlook", f"You are now in room overlook")
            if direction == "e":
                self.set_room_helper(
                    "e", "narrow", f"You are now in the NARROW room")
            if direction == "w":
                self.set_room_helper(
                    "w", "foyer", f"There is no room west of foyer\nYou are still in the foyer room")
        elif self.current_room == "overlook":
            if direction == "n":
                self.set_room_helper(
                    "n", "foyer", f"You are in the foyer")
            if direction == "s":
                self.set_room_helper(
                    "s", "overlook", "There is no room south of overlook\nYou are still in the overlook room!")
            if direction == "e":
                self.set_room_helper(
                    "e", "overlook", "There is no room east of overlook\nYou are still in the overlook room!")
            if direction == "w":
                self.set_room_helper(
                    "w", "overlook", "There is no room west of overlook\nYou are still in the overlook room!")
        elif self.current_room == "narrow":
            if direction == "n":
                self.set_room_helper(
                    "n", "treasure", "HURRRRAYYYYY YOU FOUND THE TREASURE ROOM, You Won!")
            if direction == "s":
                self.set_room_helper(
                    "s", "narrow", f"There is no room south of narrow. \n You are still in room {self.current_room}")
            if direction == "e":
                self.set_room_helper(
                    "e", "narrow", f"There is no room east of narrow. \n You are still in room {self.current_room}")
            if direction == "w":
                self.set_room_helper(
                    "w", "narrow", f"There is no room west of narrow. \n You are still in room {self.current_room}")
