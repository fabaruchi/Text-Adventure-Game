# Imports a module to add a pause
import random
import time


# 1st question
def choosePath():
    # list for different animals to change in the story
    list = ("dog", "monkey", "bear")
    animals = random.choice(list)
    path = ""
    while path != "yes" and path != "no":
        path = input("Hello, do you want to play? Enter: (yes/no)")
    if path == "yes":
        displayIntro(animals)
    if path == "no":
        print("We can play another time! Bye!")


# Story Introduction
def displayIntro(animals):
    print_pause(
        "You saw a red " + str(animals) + ", You approach the " + str(animals) + ","
    )

    print_pause(
        "but he jumps off the tree and runs. "
        "The red " + str(animals) + ", ran through a bush. "
        "You followed the " + str(animals) + ", Curious to see where it went,"
    )

    print_pause(
        "you look into the bush, only to fall "
        "down a tunnel. After a rough fall, "
        "you noticed you fell into a cave."
    )

    print_pause("Reality sets in. You need to find a way out of the cave.")

    checkPath()


# 2nd story introduction
def checkPath():
    print("You walk deep in the cave and find a bundle of rope and hook.")
    time.sleep(2)
    print("While picking up the rope, a radioactive spider bites your thumb.")
    time.sleep(2)
    print("Feeling the effects soon after, you pass out.")
    print("You awaken and attempt to escape with your powers.")
    time.sleep(2)
    correctPath()


# different path choices
def correctPath():
    choice = ""
    while choice != "yes" and choice != "no":
        choice = input(
            "Would you like to use the rope and hook"
            " along with your powers to escape? "
            "Enter: (yes/no)"
        )
    if choice == "yes":
        print_pause(
            "Awakening with new powers, you attempt to escape "
            "the cave and remembered to grab the rope and hook."
            " With the assistance of your new powers and the "
            "rope and hook, you climb out of the cave!"
            " Yay! You won the game!"
        )

        playAgain()

    elif choice == "no":
        print_pause(
            "Awakening with new powers, you attempt "
            "to escape the cave by climbing the wall."
            " Mid way up the climb, your powers wear off, "
            "and you fall."
            " Sorry, you didn't win this time..."
        )
        playAgain()
    else:
        print("Invalid choice. Please try again.")
        return correctPath()


# end of the game
def playAgain():
    answer = "yes"
    while answer == "yes":
        answer = input("Would you like to play again? Enter: (yes/no)")
        if answer == "yes":
            return choosePath()
        elif answer == "no":
            print("Thanks for playing! Bye, bye!")
        else:
            print("Invalid choice. Please try again.")
            playAgain()


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


choosePath()
