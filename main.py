# Welcome to Dungeons And Dragons

# Import to allow rolling dice
import random
# Import to allow pauses
import time


# Available inputs
attack_input = ['attack', 'atk', 'a', 'fight']
defend_input = ['block', 'defend', 'evade', 'b', 'shield', 'use shield']

player_name = "Jacob"
# Available class


class Warrior:
    ...


class Mage:
    ...


class Ranger:
    ...


# Set dice roll functions

# 100 sided dice roll
def d100(dice_amount):
    # Pick random number between 1 and 100
    total = dice_amount * (random.randint(1, 100))
    return total

# 20 sided dice roll
def d20(dice_amount):
    # Pick random number between 1 and 20
    total = dice_amount * random.randint(1, 20)
    return total

# 12 sided dice roll
def d12(dice_amount):
    # Pick random number between 1 and 12
    total = dice_amount * random.randint(1, 12)
    return total

# 8 sided dice roll
def d8(dice_amount):
    # Pick random number between 1 and 8
    total = dice_amount * random.randint(1, 8)
    return total

# 6 sided dice roll
def d6(dice_amount):
    # Pick random number between 1 and 6
    total = dice_amount * random.randint(1, 6)
    return total

# 4 sided dice roll
def d4(dice_amount):
    # Pick random number between 1 and 4
    total = dice_amount * random.randint(1, 4)
    return total

# Define Attack Function
def attack(self, target):

    # Roll dice based off attackers chance to atk
    attack_roll = self.atk

    # Display result
    print("rolled: " + str(attack_roll))

    # Determine if attacker hit target
    if attack_roll >= target.ac:
        print("The attack hits!")
        # Set temp variable to the damage roll so we can print the result and subtract damage from target health
        damage_dealt = self.dmg
        # Give player time to read
        time.sleep(1.5)
        # Subtract damage from target health and replace target health with new subtracted health
        target.health -= damage_dealt
        print("Attack did " + str(damage_dealt) + " damage")
        # Display successful attack
    else:
        # Display missed attack and end the function
        print("The attack missed...")
    time.sleep(1.5)

# Start Temp Test Code

class Creature():
    ...

class Player(Creature):
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.ac = 10
        self.atk = d20(1) + 2
        self.dmg = d6(1)
        self.initiative = 4



class Zombie(Creature):
    def __init__(self, name):
        self.name = name
        self.health = random.randint(9, 11)
        self.ac = 9
        self.atk = d20(1)
        self.dmg = d4(1)
        self.xp = 20
        self.initiative = (d4(1) + 3)



# Turn order list

# Amount of players in game
active_players = 1

# All creatures in vicinity
present_creatures = [Player("Jacob"), Zombie("Zombie1"), Zombie("Zombie2")]

# Sort all creatures in vicinity by initiative
sorted_turns = sorted(present_creatures, key=lambda creature: creature.initiative, reverse=True)

# Set the current turn as zero since nothing has happened yet
current_turn = 0

# Progress turn to next
def next_turn():

    # get the variable "current_turn" and allow it to be changed globally during this function
    global current_turn

    # Set turn to next turn by adding 1
    current_turn += 1

    # If the current turn has passed existing creatures (All players and creatures have had a turn) then reset it
    # to zero allowing the first person to go again
    if current_turn > len(present_creatures):
        new_turn = 0


# Function to allow a player to choose who they want to target
def choose_target_player():
    # Infinite loop to ensure we get the correct value from player
    while True:
        try:

            # Ask player who they would like to target
            chosen_target = int(input("Who do you target?"))

            # Return players input value
            return sorted_turns[chosen_target]

        except ValueError:

            # Player did not enter numerical value. Try again
            print("Please enter the number corresponding to a valid target")

        else:
            break


def attack_turn_player():
    # Declare self as the current turn corresponding to present_creatures list
    self = present_creatures[current_turn]

    # Announce who's turn it is
    print(str(self.name) + " turn")

    # Select target to attack
    target = choose_target_player()

    # Declare attacker and target to player
    print(self.name, "attacks", target.name)

    # Let Player Read
    time.sleep(1)

    # Run attack function based on self and target defined above
    attack(self, target)

    # Show target health to player
    print(target.name, "health is", target.health)

    # Let Player Read
    time.sleep(1)

    # Check if target or self died
    if self.health <= 0:
        print(str(target.name) + " has been defeated in battle")

    elif target.health <= 0:
        print(str(self.name), " has perished in their own attack.")

    # Next turn
    next_turn()

    # Temporary Function to show present creatures in order of turn
def temp_target_name_output(current_turn=current_turn):
    for i in sorted_turns:
        print(sorted_turns[current_turn].name)
        current_turn += 1

temp_target_name_output()
attack_turn_player()