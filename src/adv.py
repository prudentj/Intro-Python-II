from room import Room
from player import Player
from item import Item
import textwrap
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

room['outside'].doors['n'] = room['foyer']
room['foyer'].doors['s'] = room['outside']
room['foyer'].doors['n'] = room['overlook']
room['foyer'].doors['e'] = room['narrow']
room['overlook'].doors['s'] = room['foyer']
room['narrow'].doors['w'] = room['foyer']
room['narrow'].doors['n'] = room['treasure']
room['treasure'].doors['s'] = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Is
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
# Every option maps to a function that performs the aciton

player1 = Player(name="John", room=room["outside"])
sword = Item("Sting", "Pointy")
player1.room.add_item(sword)
itemNameHolder = ""
runProgram = True
choices = []


def killProgram():
    global runProgram
    runProgram = False
    print("Thanks for playing!")
# , "n":travel("n"), "s":travel("s"), "e":travel("e"), "w":travel("w"), "q": killProgram(), "sword":player1.add_item(sword)


def print_commands():
    commands = ["\ni: inventory\nn: Go North\ns: Go South\ne: Go East\nw: Go West\nq: Quit Game\nlook: See Items Inside Room\ninteract: Interact\ntake [itemName]: Picks up and item\ndrop [itemName]: Drops the item in the room"]
    for key in commands:
        print(key)


def travel(dir):
    try:
        if(player1.room.dir_exists(dir)):
            player1.room = player1.room.doors[dir]
        else:
            print("You can't go that way")
    except ValueError:
        print("Invalid Response")


def look():
    # Prints the current description (the textwrap module might be useful here).
    print("Room Description: ", textwrap.fill(player1.get_roomDesc()))
    player1.room.print_items()


def interact():
    input("Type `get [item]` or drop your item by typing `drop [item]`: \n")
# , "drop":drop_item(itemNameHolder)
# , "take":take_item(itemNameHolder)
#commands={"i":player1.print_items(), "n":travel("n"), "s":travel("s"), "e":travel("e"), "w":travel("w"), "q": killProgram(), "sword":player1.add_item(sword) }


def command(command):
    if command == "i":
        player1.print_items()
    elif command == "c":
        print_commands()
    elif command == "n":
        travel("n")
    elif command == "s":
        travel("s")
    elif command == "e":
        travel("e")
    elif command == "w":
        travel("w")
    elif command == "q":
        killProgram()
    elif command == "look":
        look()
    elif command == "interact":
        interact()
    # elif command =="l":
    #     player1.room.print_items()
    elif command == "sword":
        player1.add_item(sword)


def longCommand(command, itemName):
    if command == "take":
        rem_room_item = player1.room.remove_item(itemName)
        player1.add_item(rem_room_item)

    elif command == "drop":
        rem_player_item = player1.remove_item(itemName)
        player1.room.add_item(rem_player_item)
        print(f"you have dropped {itemName}")


while runProgram:
    ''' REPL '''
    # print current room name
    print(f"\n\033[1m{player1.get_room()}\033[0m")
   # Asks user input for which room to move to next
    stringIn = input(
        "\x1B[3mPlease enter a command. Press c for commands\x1B[23m\n")
    choices = stringIn.split(" ")

    if len(choices) == 1:
        command(stringIn)
    elif len(choices) == 2:
        longCommand(choices[0], choices[1])
    else:
        print("You use many big words. Me no understand!")
