# Udacity Python Project
import time
import random
House_monsters = ["wicked", "gaint Snak", "Zombie", "Dracula", "Witch"]
Cave_weapons = ["Sword", "Dagger", "Spear", "Poleax"]
new_weapon = ""


# printing function with timer
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# The introduction Messages
def int():
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,")
    print_pause("and has been terrifying the nearby village....")
    print_pause("")


def valid_input():
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do? \n")
    response = input("Please enter 1 or 2:\n")
    if response == "1":
        monster = random.choice(House_monsters)
        global new_weapon
        print_pause("\nYou knocked on the door of the house. \n"
                    "Suddanly the dooe was oppend"
                    " and you have been attached by a " + monster + ".")
        if new_weapon in Cave_weapons:
            print_pause("But you took the " + new_weapon + " "
                        "and killed the " + monster + ".\n"
                        "Grate You Won.\n")
        else:
            print_pause("It killed you. Sorry, you lost.")
            print_pause("\nGAME OVER.")
            print_pause("")

    elif response == "2":
        new_weapon = random.choice(Cave_weapons)
        print_pause("\nYou entered into the cave."
                    " inside the cave, you found a " + new_weapon + ".\n"
                    "You took the " + new_weapon + " "
                    "and returned to the open field.\n")
    else:
        print_pause("Sorry, I don't understand. please try again\n")
        print_pause("")
        valid_input()
    play_again()


def play_again():
    response = input("Would you like to play again?\n"
                     "Please say 'yes' or 'no'.\n").lower()
    while True:
        if response == "no":
            print_pause("Ok, goodbye!")
            print_pause(" ")
            break
        elif response == "yes":
            print_pause("\nVery good, "
                        "I'm happy that you would like to play again.")
            valid_input()
            break
        else:
            print_pause("Sorry, I don't understand. please try again.\n")
            play_again()


def story():
    int()
    valid_input()


story()
