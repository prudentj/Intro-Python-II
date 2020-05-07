# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, roomName, roomDesc, n_to=None, s_to=None, e_to=None, w_to=None):
        self.roomName = roomName
        self.roomDesc = roomDesc
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to

    def dir_exists(self, dir):
        if dir == "n":
            return self.n_to != None
        elif dir == "s":
            return self.s_to != None
        elif dir == "w":
            return self.w_to != None
        elif dir == "e":
            return self.e_to != None
        else:
            return False
