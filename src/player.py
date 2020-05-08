# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def get_room(self):
        return self.room.roomName

    def get_roomDesc(self):
        return self.room.roomDesc

    def print_items(self):
        if len(self.items) < 1:
            print("There are no items in the player inventory.")
        else:
            print("Your items are:\n")
            for n in self.items:
                print(n.name+": "+n.desc)

    def add_item(self, item):
        # dict[key] = value
        self.items.append(item)
        print(f"you have added {item.name}")

    def remove_item(self, itemName):
        # Get the subset of the list with that name
        those_items = [s for s in self.items if s.name == itemName]
        if len(those_items) > 0:
            # don't we have to remove self.items[itemName]?
            self.items.remove(those_items[0])
            return those_items[0]
        print("Cannot drop an item that you don't have!")
        return None
