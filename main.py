# Welcome to Dungeons And Dragons

# Import to allow rolling dice
import random
# Import to allow pauses
import time

# Available inputs
attack_input = ['attack', 'atk', 'a', 'fight']
defend_input = ['block', 'defend', 'evade', 'b', 'shield', 'use shield']

# Available class


class Warrior:
    ...


class Mage:
    ...


class Ranger:
    ...


# Set dice roll functions

# 100 sided dice roll
def d100():
    # Pick random number between 1 and 100
    total = random.randint(1, 100)
    return total

# 20 sided dice roll
def d20():
    # Pick random number between 1 and 20
    total = random.randint(1, 20)
    return total

# 12 sided dice roll
def d12():
    # Pick random number between 1 and 12
    total = random.randint(1, 12)
    return total

# 8 sided dice roll
def d8():
    # Pick random number between 1 and 8
    total = random.randint(1, 8)
    return total

# 6 sided dice roll
def d6():
    # Pick random number between 1 and 6
    total = random.randint(1, 6)
    return total

# 4 sided dice roll
def d4():
    # Pick random number between 1 and 4
    total = random.randint(1, 4)
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

#Define Fight Begin Function
def battle(prompt):
    # Infinite Loop
    while True:
        ...


# Start Temp Test Code
class Player:
    base_health = random.randint(18, 22)
    base_atk = random.randint(1, 20) + 1
    base_dmg = random.randint(1, 6)
    def __init__(self):
        self.health = self.base_health
        self.ac = 10
        self.atk = self.base_atk
        self.dmg = self.base_dmg

class Zombie:
    base_health = random.randint(9, 11)
    base_atk = random.randint(1, 20)
    base_dmg = random.randint(1, 4)
    def __init__(self):
        self.health = self.base_health
        self.ac = 9
        self.atk = self.base_atk
        self.dmg = self.base_dmg
        self.xp = 20

player = Player()

zombie = Zombie()

# Battle loop
while player.health > 0 and zombie.health > 0:
    # Player's turn to attack
    print("Player's turn:")
    # Let Player read
    time.sleep(1.5)
    attack(player, zombie)

    # Check if the zombie is defeated after player's attack
    if zombie.health <= 0:
        print("Zombie is defeated!")
        break

    # Zombie's turn to attack
    print("Zombie's turn:")
    # Let Player read
    time.sleep(1.5)
    attack(zombie, player)

    # Check if the player is defeated after zombie's attack
    if player.health <= 0:
        print("Player is defeated!")
        break
# End Temp Test Code
# Initialize Enemy Class
