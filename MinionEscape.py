# This is me trying to make a game:

import time

# list of items
items = ["banana", "3 bananas", "Freeze Ray", "Lipstick Taser", "Jelly Gun", "Cell Key", "Polkadotted Crowbar", "pencil"]
##List of enemies
enemies = ["evil minion", "El Macho"]
##Items needed to win: Cell Key to get out of cell. Freeze Ray to defeat evil minion 1. Polkadotted Crowbar on door to living room. Jelly Gun on swarm of evil minions in living room. Lipstick Taser on El Macho.
#Path needed to win: Cell to Dungeon Floor to Upstairs Floor to Yellow Room to Living Room to Front Door.

# class that involves all weapons used in this game; names and lists its attributes
class Weapon:
    def __init__(self, name, damage, description):
        self.name = name
        self.damage = damage
        self.description = description

    def intro(self):
        print(f"You have obtained the {self.name}. This item {self.description} and inflicts {self.damage} damage on your opponent.")

    def shoot(self):
        print(f"You shot the minion with {self.name}, dealing {self.damage} damage!")

lipsticktaser = Weapon('Lipstick Taser', '25%', "sends a streak of electricity onto your opponent, shocking him/her,")
freezeray = Weapon('Freeze Ray', '100%', "shoots a ray of ice at your opponent, freezing him/her. This freezeray only has enough ice to shoot one time.")
jellygun = Weapon('Jelly Gun', '100%', "contains a jelly substance that contains the antidote to the evil minions' disease! Once you shoot it at a purple minion, it will become a regular minion")

# class that introduces and describes the rooms
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def intro(self):
        print(f"You are now in the {self.name}. {self.description}.")

    def intro2(self):
        print(f"On the floor, you see {self.items}")

diningroom = Room('Dining Room', 'This dining room is relatively small and private, closed off on all sides and painted with garish colors. On top of the wooden dining table hangs a massive, dangling chandelier.', 'a big crowbar.'.)
foyer = Room('Foyer', 'This entrance to his house is massive and brightly lit, with smooth, tiled floors and a grandiose staircase', 'a lipstick...could it be the lipstick taser that Gru lost??')

#Class that introduces villains
class Villain:
    def __init__(self, name, introduction, health):
        self.name = name
        self.introduction = introduction
        self.weapon = weapon
        self.health = health

    def minionintro(self):
        print(f"{self.introduction}. An {enemies[0]}!")
        print(f"It is carrying {self.weapon}. It has {self.health}.")

    def minionsintro(self):
        print(f"{self.introduction}. They are carrying {self.weapon}. They all have {self.health}.")

    def elmachointro(self):
        print(f"{self.introduction}. He is carrying {self.weapon}. He has {self.health}.")

    def update(self, weapon):
        self.health -= weapon.damage
        print(f"EL Macho is now at {self.health} health.")

elmacho = Villain('El Macho', 'His red, skin-tight uniform barely covers his protruding stomach, and his mask stretches across his round head. His moustache curves into an evil grin as he sees {minion}', 'a big flamethrower, aiming straight at you', '100%')
evilminion = Villain('Evil Minion', 'Down descends a purple figure with wild, frizzy hair and protruding crooked teeth', '100%')

#Machohealth.update(lipsticktaser)
#Machohealth.update(lipsticktaser)


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
            freezeray.intro()
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
print(f"""{minion} finds himself on the cold dungeon floor and sees three items sprawled in front of him: a {items[0]}, {items[2]}, {items[7]}""")
time.sleep(2)

# calls dungeon_item()
dungeon_item()
print("   ")
time.sleep(2)

print(f"""Glancing around the dark, eerie chamber, {minion} realizes that there is only one way out of the dungeon: up the stairs.
He carefully tiptoes to the base of the stairs, then dashes to the shadows when he hears footsteps.""")
time.sleep(2)
evilminion.minionintro()

print(f"It must have been converted into an evil beast by {enemies[1]} and his potion.""")
