# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def get_room(self):
        return self.room.roomName

    def get_roomDesc(self):
        return self.room.roomDesc
