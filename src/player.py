# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def print_room(self):
        print(f"Hello {self.name}, you're {self.current_room}")
