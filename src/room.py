# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, roomName, roomDesc, n_to=None, s_to=None, e_to=None, w_to=None, items=[]):
        self.roomName = roomName
        self.roomDesc = roomDesc
        self.doors = {'n': n_to, 's': s_to, 'e': e_to, 'w': w_to}
        self.items = items
    # Expects a string

    def dir_exists(self, direction):
        return self.doors[direction] != None
    # NEEDS FIXED

    def print_items(self):
        if len(self.items) < 1:
            print("There are no items in the room.")
        else:
            print("Items in the room:\n")
            for n in self.items:
                print(n.name+": "+n.desc)

    def add_item(self, item):
        # dict[key] = value
        if item.name:
            self.items.append(item)

    def remove_item(self, itemName):
        # Get the subset of the list with that name
        those_items = [s for s in self.items if s.name == itemName]
        if len(those_items) > 0:
            self.items.remove(those_items[0])
            return those_items[0]
        print("Sorry, item is not in the room!")
        return None

    # def item_exists(self, item):
    #     if item in items:
    #         return True
    #     else:
    #     return    any(x.name == "t2" for x in l)
    #     return self.doors[direction] != None
