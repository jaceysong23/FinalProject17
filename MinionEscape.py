# Import time in order to use time.sleep() and timed responses
import time

# list of items:
items = ["banana", "3 bananas", "Freeze Ray", "Lipstick Taser", "Jelly Gun", "Cell Key", "Polkadotted Crowbar", "pencil", "crowbar"]
# List of enemies:
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

    # introduces the weapon; what it does, how much damage it does
    def intro(self):
        print(f"You have obtained the {self.name}. This item's function is {self.description} and will inflict {self.damage} damage on your opponent if used.")
    # gives the stats for how much you affected the opponent
    def shoot(self):
        print(f"You shot the minion with {self.name}, dealing {self.damage} damage!")

# the weapons that minion needs to pick up and use, plus their stats, use, description
lipsticktaser = Weapon('Lipstick Taser', '25%', "to send a streak of electricity onto your opponent, shocking him/her,")
freezeray = Weapon('Freeze Ray', '100%', "to shoot a ray of ice at your opponent, freezing him/her. This freezeray only has enough ice to shoot one time,")
jellygun = Weapon('Jelly Gun', '100%', "shoot a jelly substance that contains the antidote to the evil minions' disease! Once you shoot it at a purple minion, it will become a regular minion")

# class that introduces and describes the rooms
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    #introduces the rooms
    def intro(self):
        print(f"You are now in the {self.name}. {self.description}.")
    #if there are items are on the floor, this can be used to list them for user
    def floor_items(self):
        print(f"On the floor, you see {self.items}")
#there are two rooms and their descriptions:
diningroom = Room('Dining Room', 'This dining room is relatively small and private, closed off on all sides and painted with garish colors. On top of the wooden dining table hangs a massive, dangling chandelier.', 'a big crowbar.')
foyer = Room('Foyer', 'This entrance to his house is massive and brightly lit, with smooth, tiled floors and a grandiose staircase', 'a lipstick...could it be the lipstick taser that Gru lost??')

#Class that introduces villains
class Villain:
    def __init__(self, name, introduction, weapon, health):
        self.name = name
        self.introduction = introduction
        self.weapon = weapon
        self.health = health
    # specific intro for the first minion
    def minionintro(self):
        print(f"{self.introduction}. An {enemies[0]}!")
        print(f"It is carrying {self.weapon}. It has {self.health} health.")
    # intro for the group of minions
    def minionsintro(self):
        print(f"{self.introduction}. They are carrying {self.weapon}. They all have {self.health} health.")
    # intro for El Macho
    def elmachointro(self):
        print(f"{self.introduction}. He is carrying {self.weapon}. He has {self.health} health.")

elmacho = Villain('El Macho', "El Macho's red, skin-tight uniform barely covers his protruding stomach, and his mask stretches across his round head. His moustache curves into an evil grin as he sees you", 'a big flamethrower, aiming straight at you', '100%')
evilminion = Villain('Evil Minion', 'Down descends a purple figure with wild, frizzy hair and protruding crooked teeth', 'a crowbar', '100%')

###FUNCTIONS###

# Creating a function for the box1 or box2 choices; will keep prompting until Box 2
# .lower() allows user to type in lower case
def box_choice():
    while True:
        box_decision = input("Which box would you like to investigate: Box 1 or Box 2?\n >").lower()
        if box_decision == "box 2":
            print("You find a key in Box 2!")
            time.sleep(2)
            break
        elif box_decision == "box 1":
            print("There is nothing in the box. Try again!")
            time.sleep(1)
            print("   ")
        else:
            print("That is not an option. Try again!")

# a function that allows user to choose what item to pick up...will keep asking until you choose Freeze Ray
def dungeon_item():
    time.sleep(1)
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

#this is the fight with the first purple minion
def firstminion():
    while True:
        firstfight = input("You only have one way to escape, and that is up the stairs. Do you want to use your weapon?\n >").lower()
        if firstfight == "yes":
            print(f"You pull out the {items[2]} and jump out from your hiding spot.")
            time.sleep(3)
            start = time.perf_counter()
            print("Hurry and shoot!")
            time.sleep(1)
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
        #sends back to start cell
        elif firstfight == "no":
            print("The evil minion sees you hiding and slowly approaches. In one swift moment, it knocks you out with its crowbar.")
            time.sleep(2)
            print("You have to start over now...")
            time.sleep(4)
            firstpart()
            break
        # for any senseless answer...circles back
        else:
            print("That is not an option. Try again!")

# function that asks if user wants to pick up a crowbar for future use
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
                #takes user to a second track, which is the same until you reach the door and need to cycle back to retrieve crowbar
                secondpartnocrowbar()
                break
            elif sure == "no":
                print("Okay, crowbar obtained.")
                break
            else:
                print("That is not an option. Try again!")
        else:
            print("That is not an option. Try again!")

# asks if user wants to use crowbar or not, then carries on to thirdpart()
# regular path if minion already has crowbar
def crowbardecision():
    print("   ")
    while True:
        usecrowbar = input("Do you want to use your crowbar?\n >").lower()
        if usecrowbar == "yes":
            print(f"Crunch! The door swings open after {minion} forces it with the crowbar.")
            break
        elif usecrowbar == "no":
            print(f"""Okay, now you're stuck here until another evil minion finds you...you don't have an option.""")
            print("   ")
        else:
            print("That is not an option. Try again!")

# second path if minion did not pick up crowbar initially
def crowbardecision2():
    print(f"Do you want to go back and retrieve the {items[8]}? If you do...")
    time.sleep(5)
    while True:
        start = time.perf_counter()
        goback = input("Type 'go back' within 5 seconds!)\n >").lower()
        if goback == "go back":
            end = time.perf_counter()
            # times the reaction...need to be within 5 seconds
            if end-start <= 5:
                print(f"Great! Now you have a {items[8]} to use.")
                time.sleep(2)
                break
            #sends back to beginning
            else:
                print("""Too late! Out of nowhere, an evil minion comes up behind you can knocks you out.""")
                firstpart()
                break

# the attack of many minions on user minion
def swarmattack():
    while True:
        attackone = input("""Type 'shoot'! (not timed)
        Keep shooting and entering until all the evil minions are normal again!\n >""").lower()
        # not timed...need to shoot and convert 5 minions
        # not possible to mess up and restart because will ask to 'shoot' continuously
        if attackone == "shoot":
            print(f"First {enemies[0]} down! Now again:")
            attacktwo = input("""   Type 'shoot'!\n >""").lower()
            if attacktwo == "shoot":
                print(f"Second {enemies[0]} down! Now again:")
                attackthree = input("""    Type 'shoot'!\n >""").lower()
                if attackthree == "shoot":
                    print(f"Third {enemies[0]} down! Now another one:")
                    attackfour = input("    Type 'shoot'!\n >").lower()
                    if attackfour == "shoot":
                        print(f"Fourth {enemies[0]} down! One more minion left!")
                        attackfive = input("    Type 'shoot'!\n >")
                        if attackfive == "shoot":
                            print(f"Success! You have converted all the {enemies[0]} back into good minions.")
                            print("   ")
                            break
                        else:
                            print("**That's not it!")
                    else:
                        print("**That's not it!")
                else:
                    print("**That's not it!")
            else:
                print("**That's not it!")
        else:
            print("**That's not it!")

# defines function that asks if you want to pick up the lipstick taser, which will come to use later
# if you do not want it, then game will continue to finalpartnolip(), which will eventually send you back because no weapon
def lipstickchoice():
    print("   ")
    while True:
        lip_decision = input(f"Do you want to pick up the {items[3]}? It can help you later in your next obstacle.\n >").lower()
        if lip_decision == "yes":
            print(f"Great! {items[3]} obtained.")
            time.sleep(2)
            finalpart()
            break
        elif lip_decision == "no":
            sure = input("You sure? It will come in handy later on....and you may have to restart if you don't have it.\n >")
            if sure == "yes":
                print("Okay then.")
                finalpartnolip()
                break
            elif sure == "no":
                print(f"Okay, {items[3]} obtained.")
                finalpart()
                break
            else:
                print("That is not an option. Try again!")
        else:
            print("That is not an option. Try again!")

# the final fight that will either send you back or set you free! Must type 'tase' four times, each within 5 seconds, in order to defeat El Macho
# First asks how many times to tase El Macho with only 25% attack every time. Must answer '4'
def elmachofight():
    while True:
        print(f"You pull out your {items[3]} and face EL Macho.")
        time.sleep(3)
        math = input(f"""Since the {items[3]} only deals 25% damage, how many times do you need to tase the enemy (who has 100% health)?\n >""").lower()
        if math == "4":
            print("Good math! Now we have to attack El Macho.")
            print("   ")
            time.sleep(2)
            start = time.perf_counter()
            tase = input("Attack him! Type 'tase' within 5 seconds\n >")
            if tase == "tase":
                end = time.perf_counter()
                if end-start <=5:
                    start = time.perf_counter()
                    tase2 = input("Nice, three more times--Type 'tase' within 5 seconds\n >")
                    if tase2 == "tase":
                        end = time.perf_counter()
                        if end-start <= 5:
                            start = time.perf_counter()
                            tase3 = input("Nice, two more times--Type 'tase' within 5 seconds\n >")
                            if tase3 == "tase":
                                end = time.perf_counter()
                                if end-start <= 5:
                                    start = time.perf_counter()
                                    tase4 = input("Nice, one more time--Type 'tase' within 5 seconds\n >")
                                    if tase4 == "tase":
                                        end = time.perf_counter()
                                        if end-start <= 5:
                                            print(f"{enemies[1]} falls rigid to the ground below. You defeated El Macho!")
                                            break
                                        # sends him back to cell for every time you do not type within 5 seconds
                                        else:
                                            print("""Oh no! El Macho acted faster than you. In one swift moment, it knocks you out with his big fists.
                                            You are put to be put back in the cell!""")
                                            time.sleep(2)
                                            print("You have to start over now...")
                                            time.sleep(4)
                                            firstpart()
                                            secondpart()
                                            thirdpart()
                                            break
                                    else:
                                        print("That is not the right word.")
                                else:
                                    print("""Oh no! El Macho acted faster than you. In one swift moment, it knocks you out with his big fists.
                                    You are put to be put back in the cell!""")
                                    time.sleep(2)
                                    print("You have to start over now...")
                                    time.sleep(1)
                                    firstpart()
                                    secondpart()
                                    thirdpart()
                                    break
                            else:
                                print("""That is not the right word.""")
                        else:
                            print("""Oh no! El Macho acted faster than you. In one swift moment, it knocks you out with his big fists.
                            You are put to be put back in the cell!""")
                            time.sleep(2)
                            print("You have to start over now...")
                            time.sleep(1)
                            firstpart()
                            secondpart()
                            thirdpart()
                            break
                    else:
                        print("That is not the right word.")
                else:
                    print("""Oh no! El Macho acted faster than you. In one swift moment, it knocks you out with his big fists.
                    You are put to be put back in the cell!""")
                    time.sleep(2)
                    print("You have to start over now...")
                    time.sleep(1)
                    firstpart()
                    secondpart()
                    thirdpart()
                    break
            else:
                print("That is not the right word.")
        else:
            print("Nope that's not it...Try again.")

# This is the first part function that includes all the functions and print() commands for the game to run
# easier to call rather than typing all separate functions and spaces and time.sleep()s every time need to restart
# first function that is actually called
def firstpart():
    print("*************")
    # lets program wait 2 seconds before continuing
    time.sleep(2)
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
    print("   ")
    # introduces the first evil minion by using class
    evilminion.minionintro()

    time.sleep(5)
    print(f"It must have been converted into an evil beast by {enemies[1]} and his potion!""")
    print("   ")
    time.sleep(2)

    # calls first minion attack function
    firstminion()
    # calls crowbar()
    crowbar()

# This is the second part function that includes all the functions and print() commands for the game to run second part
# easier to call rather than typing all separate functions and spaces and time.sleep()s every time need to restart
def secondpart():
    print(f"""{minion} steps around the frozen minion's body and stealthily ascends up the stairs.
    He quietly opens the door and walks inside...""")
    print("-----------------------------------------")
    print("  ")
    time.sleep(4)

    # introduces the dining room
    diningroom.intro()
    time.sleep(5)
    print("   ")

    print(f"{minion} heads directly for a door to the side of the room.")
    print(f"It's locked! You need to use something to prop it open.")
    time.sleep(6)

    # calls the crowbardecision() to ask if user wants to use crowbar or not
    crowbardecision()

# second option for secondpart() but this time if minion does not have crowbar
def secondpartnocrowbar():
    print(f"""{minion} steps around the frozen minion's body and stealthily ascends up the stairs.
    He quietly opens the door and walks inside...""")
    print("-----------------------------------------")
    print("  ")
    time.sleep(4)

    #same...introduces dining room
    diningroom.intro()
    time.sleep(5)

    print(f"{minion} heads directly for a door to the side of the room.")
    time.sleep(2)
    print(f"It's locked! You need to use something to prop it open.")
    time.sleep(4)
    print(f"Well, looks like you're stuck here until another {enemies[0]} finds you.")

    #second crowbardecision function that asks whether you want to go back to retieve...if not, will send you back to beginning
    crowbardecision2()

# This is the first part function that includes all the functions and print() commands for the game to run
# easier to call rather than typing all separate functions and spaces and time.sleep()s every time need to restart
def thirdpart():
    print("-----------------------------------------------")
    time.sleep(5)
    #introduces foyer
    foyer.intro()
    time.sleep(6)
    print("   ")
    print(f"""Looking down, {minion} sees a {items[4]} on the floor nearby. It must have been left by a good minion trying to
    escape beforehand!""")
    time.sleep(7)
    print("   ")

    print(f"{minion} bends down to retrieve the jelly gun.")
    # introduces jellygun
    jellygun.intro()
    time.sleep(10)
    print("   ")

    print(f"""Right after {minion} picks up the {items[4]}, he hears a rumbling sound. A group of angry purple minions
    have spotted him and are stampeding towards {minion}!""")
    time.sleep(4)

    #calls the attack with a group of minions
    swarmattack()
    print("   ")
    time.sleep(2)
    print(f"""Good job! {minion} doesn't stop to celebrate, though, for he heads straight for the front door.
    But just as he was about to reach it, something catches his eye...""")
    time.sleep(6)
    print(f"""Out of the corner of his eyes, he sees a shiny, red object laying about three feet to the right.""")
    time.sleep(3)
    print("Could it be the Lipstick Taser that Gru left...?")

    #calls lipstickchoice() to pick up lipstick taser or not...if not, goes to finalpartnolip()
    lipstickchoice()
    print("   ")

#final part of game, which includes the fight with El Macho
# is accessed within thirdpart()
def finalpart():
    # introduces lipsticktaser
    lipsticktaser.intro()
    time.sleep(6)
    print(f"Just as {minion} gets up after picking it up, a large, booming voice rings out from in front.")
    time.sleep(2)
    print("   ")
    print('"Well well well, what do we have here? An escaping minion, is it?"')
    time.sleep(2)

    print("   ")
    print(f"{minion} grows cold as he realizes who it is...El Macho, the villain who trapped him!")
    time.sleep(3)

    #introduces el macho
    elmacho.elmachointro()
    time.sleep(7)

    print("   ")
    print(f"{minion} realizes that his jelly gun doesn't work on {enemies[1]} because El Macho is not purple!")
    time.sleep(3)
    print(f"...and because he didn't TURN evil; he IS evil")
    print("   ")

    time.sleep(3)
    print(f"You have to use your {items[3]}!")
    time.sleep(2)

    # the final fight with el macho!
    elmachofight()

def finalpartnolip():
    print(f"Just as {minion} looks up again, a large, booming voice rings out from in front.")
    time.sleep(3)
    print("   ")
    print('"Well well well, what do we have here? An escaping minion, is it?"')
    time.sleep(3)
    print("   ")
    print(f"{minion} grows cold as he realizes who it is...El Macho, the villain who trapped him!")
    time.sleep(5)
    elmacho.elmachointro()
    time.sleep(7)

    print("   ")
    print(f"Panicking, {minion} realizes that his jelly gun doesn't work on {enemies[1]} because El Macho is not purple!")
    time.sleep(4)
    print("But he doesn't have any other weapon to use...")
    time.sleep(2)
    print("   ")
    print(f"El Macho activates his Flamethrower and knocks {minion} out with one blow.")
    time.sleep(2)
    print("   ")
    print("You have to start over now...")
    time.sleep(4)
    print("   ")

    # has no weapont to defeat El Macho, so needs to go through firstpart(), secondpart(), and thirdpart()
    # basically restart everything
    firstpart()
    secondpart()
    thirdpart()

###START OF GAME###
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
time.sleep(5)

# these are the only functions that are called, and within these parts are more functions and descriptions
firstpart()
secondpart()
thirdpart()

##THE ENDING##
print(f"{minion} opens the front door and finally escapes!")
time.sleep(2)
print(f"Congradulations {player_name}, you completed the game! Thanks for playing :)")
