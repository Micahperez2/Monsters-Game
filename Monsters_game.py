#Micah Perez - Monsters_game.py
#Created October 1st, 2018

import random
Keys = False
Password = False
Remote = False

#Creating a Class for the Main Character
class character:
    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health

#Functions Used for Each Part of the Game
def Car_keys():
    user_g = character(user_name, gift(3),gift(3),strength(5))
    print("'I AM PREDATOR. I WILL DESTORY YOU AND EVERYTHING YOU'VE EVERY KNOWN AND LOVED!'\n")
    Predator = character("Predator",gift(5),strength(0), strength(5))
    result_Predator = fight(user_g,Predator)
    if result_Predator == True:
        print("AHHH THE PAIN I'VE DELIVERED TO MY CHILDREN I NOW FEEL! HERE ARE MY KEYS'\n")
        return True
    else:
        return False
def House_Password():
    user_c = character(user_name, gift(3),gift(2),strength(5))
    print("'Hello! I am DRACULA! I will Destroy everything in my sight! You either defeat me and get the password...or you DIE!'\n")
    Dracula = character("Dracula",strength(2),gift(3),strength(5))
    result_Dracula = fight(user_c,Dracula)
    if result_Dracula == True:
        print("'NOOO! YOU'VE DEFEATED ME! THE PASSWORD IS 8624 TO THE HOUSE, I WILL BE BACK THOUGH!'\n")
        return True
    else:
        return False
def Cthulhu_Remote():
    user_a = character(user_name, gift(3),gift(3),strength(5))
    print("'AY WHATS UP! I GOT CTHULHU'S REMOTE AND YOU AIN'T GETTING IT! TIME TO DIE!'\n")
    Frankenstein = character("Frankenstein",strength(1),gift(4),strength(5))
    result_Frankenstein = fight(user_a,Frankenstein)
    if result_Frankenstein == True:
        print("NAHHH, I AM DEFETED! TAKE THE REMOTE DEN!'\n")
        return True
    else:
        return False

#Functions to make Character Stronger with More Items
def strength(num):
    if (Remote == True):
        num += 2
    if (Password == True):
        num += 2
    if (Keys == True):
        num += 2
    return num


def gift(atk):
    if (Remote == True):
        atk += 1
    if (Password == True):
         atk += 1
    if (Keys == True):
        atk += 1
    return atk

#Battle Function
def fight(main, boss):
    while boss.health > 0:
        print("STATS of " + str(main.name) + ": ATTACK:" + str(main.attack) + " DEFENSE:" + str(main.defense) + " HEALTH:" + str(main.health) + "\n")
        print("STATS of " + str(boss.name) + ": ATTACK:" + str(boss.attack) + " DEFENSE:" + str(boss.defense) + " HEALTH:" + str(boss.health) + "\n")
        attack_choice = raw_input("Time to attack, will you choose 1(100% - x.5 damage), 2(75% - x1 damage), or 3(33% - x2 damage)?:")
        attack_power = hit(attack_choice, main)
        if attack_power == 0:
            print("Your attack did not hit!\n")
        elif attack_power > boss.defense:
            print("Your attack hit! It did " + str(attack_power) + " damage and " + str(attack_power - boss.defense) + " damage after defense!\n")
            boss.health -= (attack_power - boss.defense)
        else:
            print("Your attack hit but the opponent blocked it completely!\n")
        if boss.health <= 0:
            return True
        print("Now its " + str(boss.name) + "'s time to attack. Remember that they get the same attack options as you!")
        boss_choice = random.randint(1,3)
        print ("Boss Choice: " + str(boss_choice) + "\n")
        boss_power = hit(str(boss_choice), boss)
        if boss_power != 0 and boss_power > main.defense:
            print(str(boss.name) + " attacked and did " + str(boss_power - main.defense) + " damage!\n")
            main.health -= (boss_power - main.defense)
        elif boss_power < main.defense and boss_power != 0:
            print(boss_power)
            print("You blocked their attack!")
        else:
            print("Their attack didn't hit!")
        if main.health < 0:
            return False
    return True

#Function used in Battle, used to calculate hits
#Takes Characters current attack value and multiplies with chance to hit dependin on choice
def hit(choice, characters):
    if choice == '1':
        return (.5 * characters.attack)
    elif choice == '2':
        if random.randint(0,100) < 75:
            return characters.attack
        else:
            return 0
    elif choice == '3':
        if random.randint(0,100) < 33:
            return (2 * characters.attack)
        else:
            return 0
    else:
        return (.5 * characters.attack)

#Main Function (Where everything runs)
print("Welcome to the Monster simulation, where you play as yourself and go through a wild adventure! Prepare yourself!")
raw_input("Press Enter to continue...\n")
answer = "no"
while answer != 'yes':
    user_name = raw_input("What is your name?: ")
    answer = raw_input("Are you sure? (type yes for yes) ")
print("\n")
print("Hello " + user_name + ", its nice meeting you!\n")
print("Well lets get to the rules, you start off with 3 points of attack and 3 points of defense, with 5 points of health. Everyturn you attack and you choose either 1,2, or 3. 1 is a sure hit and does half your attack power, 2 is 75% chance but hits at your full power, 3 is a 33% chance to hit but you will do twice your damage.  As you progress in the game you will gain attack, defense, and health. Simple as that.\n")
raw_input("Press Enter to continue...\n")
print("This is the situation: Cthulhu has captured THE PRINCESS and you have to get him back! However to do this, you must get three items - 1) Car Keys (Predators), 2) House Password (Draculas), and 3) Cthulhu's remote(Frankensteins). Once you have all 3 you can fight Cthulhu and free THE PRINCESS!\n")
#Check for Players items in order to move forward
while (Keys == False or Password == False or Remote == False):
    print ("Currently you need: ")
    if (Keys == False):
        print ("-Keys")
    if (Password == False):
        print ("-Password")
    if (Remote == False):
        print ("-Remote")
    print("\n")
    world = raw_input("What Item would you like to go for? Type k for keys, p for password, or r for remote? ")
    print ("\n")
    if (world == 'k'):
        Keys = Car_keys()
        if Keys == False:
            print("You Lost! Try Again!")
            break
    elif (world == 'p'):
        Password = House_Password()
        if Password == False:
            print("You Lost! Try Again!")
            break
    elif (world == 'r'):
        Remote = Cthulhu_Remote()
        if Remote == False:
            print("You Lost! Try Again!")
            break
    else:
        print("World not found!\n")
#If all items are found then Move on to the final boss
if Keys == True and Password == True and Remote == True:
    print("Congratulations! You've collected all the items!\n")
    password = raw_input("Now its time to fight CTHULHU! You take the keys and drive to her house! When you get out you see a password lock. Whats the Password?")
    print("\n")
    if password == '8624':
        print("That was the Password! You're in!\n")
    else:
        while (password != '8624'):
            password = raw_input("WRONG PASSWORD! TRY AGAIN!:")
            print("\n")
    raw_input("Press Enter to continue...\n")
    print("You walk in the house...there is nothing but a stand for the TV remote. You put the remote on the stand and a portal opens up. You walk into the portal and WHHHHOOOSSSSS! YOU ARE SENT INTO A REALM! YOU ARE GREETED WITH THE PRINCESS LAUGHING.....WITH Cthulhu IN A CAGE BEHIND!\n")
    print("CTHULHU yells 'I DIDN'T CAPTURE THE PRINCESS...HE CAPTURED ME!\nYou see THE PRINCESS in the background, the fight is on!\n")
    user_m = character(user_name, 10, 5, 20)
    THE PRINCESS = character("THE PRINCESS", 9, 6, 22)
    result_THE PRINCESS = fight(user_m, THE PRINCESS)
    if (result_THE PRINCESS == False):
        print("YOU HAVE BEEN DEFEATED BY THE PRINCESS! CTHULHU IS CAPTURED AND FOREVER GONE!")
    else:
        print("YOU DID IT! YOU DEFEATED THE PRINCESS AND CTHULHU IS FREE! CONGRATULATIONS, YOU HAVE WON!")
