# This is me trying to make a game:

import time

# list of items
items = ["banana", "3 bananas", "Freeze Ray", "Lipstick Taser", "Jelly Gun", "Cell Key", "Polkadotted Crowbar", "pencil", "crowbar"]
##List of enemies
enemies = ["evil minion", "El Macho"]
##Items needed to win: Cell Key to get out of cell. Freeze Ray to defeat evil minion 1. Polkadotted Crowbar on door to living room. Jelly Gun on swarm of evil minions in living room. Lipstick Taser on El Macho.
#Path needed to win: Cell to Dungeon Floor to Upstairs Floor to Yellow Room to Living Room to Front Door.

###CLASSES###
# class that involves all weapons used in this game; names and lists its attributes
class Weapon:
    def __init__(self, name, damage, description):
        self.name = name
        self.damage = damage
        self.description = description

    def intro(self):
        print(f"You have obtained the {self.name}. This item's function is {self.description} and will inflict {self.damage} damage on your opponent if used.")

    def shoot(self):
        print(f"You shot the minion with {self.name}, dealing {self.damage} damage!")

lipsticktaser = Weapon('Lipstick Taser', '25%', "to send a streak of electricity onto your opponent, shocking him/her,")
freezeray = Weapon('Freeze Ray', '100%', "to shoot a ray of ice at your opponent, freezing him/her. This freezeray only has enough ice to shoot one time,")
jellygun = Weapon('Jelly Gun', '100%', "shoot a jelly substance that contains the antidote to the evil minions' disease! Once you shoot it at a purple minion, it will become a regular minion")

# class that introduces and describes the rooms
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def intro(self):
        print(f"You are now in the {self.name}. {self.description}.")

    def floor_items(self):
        print(f"On the floor, you see {self.items}")

diningroom = Room('Dining Room', 'This dining room is relatively small and private, closed off on all sides and painted with garish colors. On top of the wooden dining table hangs a massive, dangling chandelier.', 'a big crowbar.')
foyer = Room('Foyer', 'This entrance to his house is massive and brightly lit, with smooth, tiled floors and a grandiose staircase', 'a lipstick...could it be the lipstick taser that Gru lost??')

#Class that introduces villains
class Villain:
    def __init__(self, name, introduction, weapon, health):
        self.name = name
        self.introduction = introduction
        self.weapon = weapon
        self.health = health

    def minionintro(self):
        print(f"{self.introduction}. An {enemies[0]}!")
        print(f"It is carrying {self.weapon}. It has {self.health} health.")

    def minionsintro(self):
        print(f"{self.introduction}. They are carrying {self.weapon}. They all have {self.health} health.")

    def elmachointro(self):
        print(f"{self.introduction}. He is carrying {self.weapon}. He has {self.health} health.")

    def update(self, weapon):
        self.health -= weapon.damage
        print(f"EL Macho is now at {self.health} health.")

elmacho = Villain('El Macho', 'His red, skin-tight uniform barely covers his protruding stomach, and his mask stretches across his round head. His moustache curves into an evil grin as he sees {minion}', 'a big flamethrower, aiming straight at you', '100%')
evilminion = Villain('Evil Minion', 'Down descends a purple figure with wild, frizzy hair and protruding crooked teeth', 'a crowbar', '100%')

#Machohealth.update(lipsticktaser)
#Machohealth.update(lipsticktaser)

###FUNCTIONS###

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

# a function that allows user to choose what item to pick up
def dungeon_item():
    while True:
        item_decision = input(f"Which object would you like to pick up for future use?\n >").lower()
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

def firstminion():
    while True:
        firstfight = input("You only have one way to escape, and that is up the stairs. Do you want to use your weapon?\n >").lower()
        if firstfight == "yes":
            print(f"You pull out the {items[2]} and jump out from your hiding spot.")
            time.sleep(3)
            start = time.perf_counter()
            print("Hurry and shoot!")
            time.sleep(2)
            shoot = input("""(type 'shoot' within 5 seconds!)\n >""").lower()
            if shoot == "shoot":
                end = time.perf_counter()
                if end-start <= 5:
                    print("The purple minion is now frozen!")
                    time.sleep(2)
                    break
                else:
                    print("""Oh no! The evil minion acted faster than you. In one swift moment, it knocks you out with its crowbar.
                    You are put back in the cell!""")
                    time.sleep(2)
                    print("You have to start over now...")
                    time.sleep(4)
                    firstpart()
                    break
        elif firstfight == "no":
            print("The evil minion sees you hiding and slowly approaches. In one swift moment, it knocks you out with its crowbar.")
            time.sleep(2)
            print("You have to start over now...")
            time.sleep(4)
            firstpart()
            break
        else:
            print("That is not an option. Try again!")

# function that asks if user wants to
def crowbar():
    while True:
        crowbar_decision = input(f"Now, your freeze gun is useless. Would you like to take the {enemies[0]}'s crowbar?\n >").lower()
        if crowbar_decision == "yes":
            print("Great! Crowbar obtained.")
            time.sleep(2)
            break
        elif crowbar_decision == "no":
            sure = input("You sure? It might come in handy later on.\n >")
            if sure == "yes":
                print("Okay then.")
                secondpartnocrowbar()
                break
            elif sure == "no":
                print("Okay, crowbar obtained.")
                break
            else:
                print("That is not an option. Try again!")
        else:
            print("That is not an option. Try again!")

def crowbardecision():
    while True:
        usecrowbar = input("Do you want to use your crowbar?\n >").lower()
        if usecrowbar == "yes":
            print(f"Crunch! The door swings open after {minion} forces it with the crowbar.")
            break
        elif usecrowbar == "no":
            print(f"""Okay, now you're stuck here until another evil minion finds you...you don't have an option.""")
        else:
            print("That is not an option. Try again!")

def crowbardecision2():
    print(f"Do you want to go back and retrieve the {items[8]}? If you do...")
    time.sleep(5)
    while True:
        start = time.perf_counter()
        goback = input("Type 'go back' within 5 seconds!)\n >").lower()
        if goback == "go back":
            end = time.perf_counter()
            if end-start <= 5:
                print(f"Great! Now you have a {items[8]} to use.")
                time.sleep(2)
                break
            else:
                print("""Too late! Out of nowhere, an evil minion comes up behind you can knocks you out.""")
                firstpart()
                break

def firstpart():
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
    print(f"""{minion} finds himself on the cold dungeon floor and sees three items sprawled in front of him: {items[0]}, {items[2]}, {items[7]}""")
    time.sleep(2)

    # calls dungeon_item()
    dungeon_item()
    print("   ")
    time.sleep(8)

    print(f"""Glancing around the dark, eerie chamber, {minion} realizes that there is only one way out of the dungeon: up the stairs.
    He carefully tiptoes to the base of the stairs, then dashes to the shadows when he hears footsteps.""")
    time.sleep(5)

    evilminion.minionintro()

    time.sleep(4)
    print(f"It must have been converted into an evil beast by {enemies[1]} and his potion!""")
    print("   ")
    time.sleep(2)

    firstminion()

    crowbar()

def secondpart():
    print(f"""{minion} steps around the frozen minion's body and stealthily ascends up the stairs.
    He quietly opens the door and walks inside...""")
    print("-----------------------------------------")
    print("  ")
    time.sleep(4)

    diningroom.intro()
    time.sleep(5)

    print(f"{minion} heads directly for a door to the side of the room.")
    time.sleep(2)
    print(f"It's locked! You need to use something to prop it open.")
    time.sleep(2)

    crowbardecision()

def secondpartnocrowbar():
    print(f"""{minion} steps around the frozen minion's body and stealthily ascends up the stairs.
    He quietly opens the door and walks inside...""")
    print("-----------------------------------------")
    print("  ")
    time.sleep(4)

    diningroom.intro()
    time.sleep(5)

    print(f"{minion} heads directly for a door to the side of the room.")
    time.sleep(2)
    print(f"It's locked! You need to use something to prop it open.")
    time.sleep(4)
    print(f"Well, looks like you're stuck here until another {enemies[0]} finds you.")

    crowbardecision2()

def thirdpart():
    time.sleep(3)
    foyer.intro()
    time.sleep(5)
    print(f"""Looking down, {minion} sees a {items[4]} on the floor nearby. It must have been left by a good minion trying to
    escape beforehand!""")
    time.sleep(3)
    jellygun.intro()
    time.sleep(5)
    print(f"""Right after {minion} picks up the {items[4]}, he hears a rumbling sound. A swarm of angry purple minions
    have spotted him and are stampeding towards {minion}!""")
    time.sleep(2)
    print("""Quick, type 'shoot'!
    Keep shooting and entering until all the evil minions are normal again!""")

###INTRODUCTION###
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

firstpart()
secondpart()

#### how to check depository/status??
