# This is me trying to make a game:

import time

# list of items
items = ["banana", "3 bananas", "Freeze Ray", "Lipstick Taser", "Jelly Gun", "Flamethrower", "Cell Key", "Polkadotted Crowbar", "pencil"]
##List of enemies
enemies = ["evil minion", "El Macho"]
##Items needed to win: Cell Key to get out of cell. Freeze Ray to defeat evil minion 1. Polkadotted Crowbar on door to living room. Jelly Gun on swarm of evil minions in living room. Lipstick Taser on El Macho.
#Path needed to win: Cell to Dungeon Floor to Upstairs Floor to Yellow Room to Living Room to Front Door.

# Creating a function for the box1 or box2 choices; will keep prompting until Box 2
def box_choice():
    while True:
        box_decision = input("Which box would you like to investigate: Box 1 or Box 2?\n >").lower()
        if box_decision == "box 2":
            print("You find a key in Box 2!")
            time.sleep(2)
            break
        elif box_decision == "box 1":
            print("There is nothing in the box. Try again!")
        else:
            print("That is not an option. Try again!")

def dungeon_item():
    while True:
        item_decision = input(f"Which object would you like to pick up for future use?\n **Tip: only one will be able to defeat opponents--use common sense**\n >").lower()
        if item_decision == "freeze ray":
            print("Nice choice!")
            time.sleep(2)
            break
        elif item_decision == "pencil":
            print("Are you sure about that?")
            time.sleep(2)
        elif item_decision == "banana":
            print(f"Oooo {minion} loves bananas, but I don't think it will help him that much.")
            time.sleep(2)
        else:
            print("That is not an option. Try again!")
            time.sleep(2)

# Asks the user for their name and saves as player_name
player_name = input("Welcome to MinionEscape! Please enter your name.\n >").title()

# Greets user with his/her name
print("Hello, {}!".format(player_name))
#print(f"Hello, {player_name}!")

# Asks for character name and saves as character_name
minion = input("Which minion would you like to be: Stuart, Kevin, or Bob?\n >").title()

# an intro for the game
print("Great! Your minion's name is {}, and {} is ready for action!".format(minion, minion))
print("   ")
print("Okay, let's start!")
print("   ")
# time.sleep(x) function tells program to wait an x amount of seconds before executing the next command
time.sleep(3)
print("""{} has just been captured by villain EL Macho.
Your objective is to manuvuer through his mansion and escape out the front door. You will meet several obstacles along the way.""".format(minion))

print("   ")
time.sleep(3)

print("*************")

time.sleep(4)

print(f"""Clang! The door of the cage slams shut behind {minion} as {minion} is thrust into the cell, locking him inside.
{minion} is trapped in the dungeons of El Macho's mansion! Looking around, {minion} sees that there are two wooden boxes in your cell.""")

# calls box_choice function
box_choice()
print("   ")

print(f"After obtaining the key, {minion} uses it to open the cell door. Hooray, you are free!")
time.sleep(2)
print(".....kinda")
print("   ")
time.sleep(2)
print(f"""{minion} finds himself on the cold dungeon floor and sees three items sprawled in front of him: a {items[0]}, {items[2]}, {items[8]}""")
time.sleep(2)

# calls dungeon_item()
dungeon_item()
print("   ")

print(f"""Glancing around the dark, eerie chamber, {minion} realizes that there is only one way out of the dungeon: up the stairs.
He carefully tiptoes to the base of the stairs, then dashes to the shadows when he hears footsteps.""")
time.sleep(2)
print(f"""Down descends a purple figure with wild, frizzy hair and protruding crooked teeth. An {enemies[0]}!
It must have been converted into an evil beast by {enemies[1]} and his potion.""")
