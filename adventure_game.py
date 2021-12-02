import time
import random

item = []


def print_sleep(message):
    print(message)
    time.sleep(2)


def intro(enemy):
    print_sleep("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_sleep(f"Rumor has it that a wicked {enemy} is somewhere around"
                " here, and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty "
                "(but not very effective) dagger.")
    print_sleep("....")


def come_again():
    print_sleep("Sorry, i did't get that.")


def fight(enemy, weapon, injury):
    if 'weapon' in item:
        print_sleep(f"As the wicked {enemy} moves to attack, "
                    "you unsheath your new weapon.")
        print_sleep(f"The {weapon} shines brightly in your hand as you "
                    "brace yourself for the attack.")
        print_sleep(f"The wicked {enemy} attacks and you were able to"
                    "{injury} the {enemy} with your new toy")
        print_sleep(f"You have rid the town of the wicked {enemy}. "
                    "You are victorious!")
        print_sleep("....")
    else:
        print_sleep("You do your best...")
        print_sleep(f"but your dagger is no match for the {enemy}.")
        print_sleep("You have been defeated!")
        print_sleep("....")


def field(enemy, weapon, injury):
    while True:
        print_sleep("Enter 1 to knock on the door of the house. "
                    "Enter 2 to peer into the cave.")
        print_sleep("What would you like to do? ")
        choice = input("Please enter 1 or 2\n")
        if '1' in choice:
            house(enemy, weapon, injury)
            break
        elif '2' in choice:
            cave(enemy, weapon, injury)
            break
        else:
            come_again()


def house(enemy, weapon, injury):
    print_sleep("You approach the door of the house.")
    print_sleep(f"You are about to knock when the door"
                "opens and out steps a {enemy}.")
    print_sleep(f"Eep! This is the {enemy}'s house!")
    print_sleep(f"The {enemy} attacks you!")
    print_sleep("....")
    if 'weapon'not in item:
        print_sleep("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    print_sleep("...")
    while True:
        house_choice = input("Would you like to (1) fight or (2) run away?\n")
        if '1' in house_choice:
            fight(enemy, weapon, injury)
            play_again = input("Would you like to play again? (y/n) ")
            if 'y' in play_again:
                play_game()
            elif 'n' in play_again:
                print_sleep("Thanks for playing! See you next time.")
                break
            else:
                come_again()

        elif '2' in house_choice:
            print_sleep("You run back into the field. Luckily, "
                        "you don't seem to have been followed.")
            field(enemy, weapon, injury)
        else:
            come_again()


def cave(enemy, weapon, injury):
    print_sleep("You peer cautiously into the cave.")
    if 'weapon' in item:
        print_sleep("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")
        print_sleep("You walk back out to the field.")
        print_sleep("...")
        field(enemy, weapon, injury)
    else:
        item.append('weapon')
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep(f"You have found the {weapon}!")
        print_sleep(f"You discard your silly old dagger and take "
                    "the {weapon} with you.")
        print_sleep("You walk back out to the field.")
        print_sleep("...")
        field(enemy, weapon, injury)


def play_game():
    item.clear()
    enemy = random.choice(['troll', 'fairie', 'queen', 'dragon', 'vampire'])
    weapon = random.choice(['sword of truth', 'light saber', 'excalibur'])
    injury = random.choice(['behead', 'destroy', 'vanquish'])
    intro(enemy)
    field(enemy, weapon, injury)


play_game()
