# -*- coding: utf-8 -*-
# About this file:
# This is the file where I define the functions which make up the game.
# I also have here the BPlayer class, which contains the current player's
# data.
#
# About naming conventions:
#   Functions
#       I will consequently add a 'b_' prefix to all function names to avoid
#       any accidental clashes with builtin functions.
#

import os
from sys import exit
from b_globals import *
import random


class BPlayer(object):
    """This is the player class.

    Attributes:
        inventory: A list of strings representing the players possessions.
        health: A positive integer.
        achievements: A list of strings.
        gold: A positive integer.
        points: A positive integer (not sure if i will use it).
    """

    def __init__(self, name, health, gold, points):
        self.name = name
        self.inventory = []
        self.health = health
        self.achievements = []
        self.gold = gold
        self.points = points

    def print_current_state(self):
        """Prints all data stored in the instance of the BVPlayer object."""
        print "-------------------------"
        print "Inventory:\t", self.inventory
        print "Health:\t\t", self.health
        print "Achievements:\t", self.achievements
        print "Gold:\t\t", self.gold
        print "Points:\t\t", self.points
        print "-------------------------"

    def inv_item(self, i):
        """Returns number 'i' item of achievement list."""
        print self.inventory[i]

    def inv_add(self, new_item, print_it):
        """Adds item to inventory list. If 'print_it' is set to true, a message is
        printed."""
        self.inventory.append(new_item)
        if print_it:
            print new_item, "is added to inventory."
        else:
            pass

    def ach_item(self, i):
        """Returns number 'i' item of achievement list."""
        print self.achievements[i]

    def ach_add(self, new_item, print_it):
        """Adds item to achievements list. If 'print_it' is set to true, a
        message is printed."""
        self.achievements.append(new_item)
        if print_it:
            print "New Achievement Achieved:", new_item
        else:
            pass

    def ch_health(self, change):
        """Changes the health attribute by 'change' amount of HP. Use integers."""
        self.health += change
        print "You have", self.health, "healt points."

    def ch_gold(self, change):
        """Changes the gold attribute by 'change' amount. Use integers."""
        self.gold += change
        print "You have", self.gold, "Gold."

    def ch_points(self, change):
        """Changes the points attribute by 'change' amount. Use integers."""
        self.points += change
        print "You have", self.points, "points."


def b_not_ready():
    """Prints a message, and exits."""
    print "*------------------------*\n" \
          "* This is not ready yet. *\n" \
          "*------------------------*\n\n" \
          "... returning to Main Menu ..."
    b_main_menu()


def b_printer(filename):
    """Function for printing .txt files in the project folder."""
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    openfilename = os.path.join(file_dir, filename)
    text_to_print = open(openfilename)
    print text_to_print.read()
    text_to_print.close()


def b_menu_nav():
    """Function which inserts the Menu Navigation into other functions. Use at end of function."""
    print "Type 'b' to get back to the Main Menu, or hit 'q' to exit the game."

    while True:
        command = raw_input(" > ")

        if command in bv_commands['back']:
            b_main_menu()
        elif command in bv_commands['exit']:
            exit(0)
        else:
            pass


def b_dead(why):
    """Function to call, when the player dies."""
    print why, "\nGood job!"
    exit(0)


def b_disclaimer():
    """About page."""
    b_printer("texts/disclaimer.txt")
    b_menu_nav()


def b_help():
    """Help page."""
    b_printer("texts/help.txt")
    b_menu_nav()


def b_main_menu():
    """This function is going to be called first, when you start the game.
    You will be able to get help, read about the background of this game,
    and start the game. This function can also respond to some swearwords
    in an interactive way."""

    b_printer('texts/main_menu.txt')

    swear_count = 0

    while True:
        command = raw_input(" > ")

        if command in bv_commands["help"]:
            b_help()
        elif command in bv_commands["about"]:
            b_disclaimer()
        elif command in bv_commands["start_game"]:
            b_start()
        elif command in bv_commands["swear_words"]:
            swear_count += 1
            if swear_count < 2:
                print "That is not a very nice thing to say."
                pass
            elif swear_count < 4:
                print "Frack you", swear_count, "times!"
                pass
            else:
                b_dead("You are especially rude, adventurer.\n"
                       "As a punishment, the bear comes out from the game,\n"
                       "rapes you and eats your face.")
        elif command in bv_commands["exit"]:
            print "'twas nice having you, great adventurer. \nSee you next time!"
            exit(0)
        else:
            print "I didn't understand that. \n" \
                  "Please type something like the four commands up there!\n"


def b_start():
    # Here we ask the player for a name and create an instance of the BVPlayer
    # class, with that name.
    print "What is your name?"

    name = raw_input(" > ")
    player = BPlayer(name, 10, 0, 0)

    print "Welcome to the game,", name, "!"
    print "These are your stats:"
    player.print_current_state()

    print "Are you ready to start the game?" \
          "\nType 'y' for Yes, 'n' for No."

    command = raw_input(" > ")

    while True:
        if command in bv_commands['yes']:
            b_first_room()
        elif command in bv_commands['no']:
            b_main_menu()
        else:
            print "Sorry, that's not a yes or a no. Try to answer again, \n" \
                  "I swear it's not that hard."


def b_first_room():
    """Start scene. Empty room, two ways to leave, two ways to die."""
    b_printer('texts/first_room.txt')
    indecision = 0
    while True:
        command = raw_input(" > ")

        if command in bv_commands['left']:
            b_bottom_of_the_well()
        elif command in bv_commands['right']:
            b_corridor()
        elif command in bv_commands['turn_off_lights']:
            b_dead("You extinguished the torch, so now you are in the dark,\n"
                   "and you die in the dark, slowly going crazy.")
        else:
            if indecision < 3:
                indecision += 1
                print "Say again?"

            else:
                b_dead("I have two kittens who are more determined than that.\n"
                       "You die of procrastination. (Very common nowadays.)")


def b_bottom_of_the_well():
    """Dead end. Go back, or die."""
    b_printer('texts/bottom_of_the_well.txt')
    stayed = 0
    albatros = "As you nap there unwitting, a huge albatros\n" \
               "shits on your head, and the 50 kilo of bird feces\n" \
               "breaks your head-brain-shoulders-everything.\n" \
               "You die a ridiculously gross death."

    while True:
        command = raw_input(" > ")

        if command in bv_commands['back']:
            print "You leave the well and the beautiful\n" \
                  "sky with an ache in your hearth."
            b_first_room()
        elif command in bv_commands['climb']:
            b_dead("You try to climb out of the hole. At first it goes\n"
                   "pretty well, but after a time you start to tire.\n\n"
                   "You are about halfway, when your foot slips, and\n"
                   "you fall down about 30 meters.\n\n"
                   "Your remains form a nice little pool, which is serves\n"
                   "as a smorgasbord for worms!")
        else:
            stayed += 1
            if command in bv_commands['stay']:
                if stayed < 2:
                    print "You decide to stay a bit more, to watch\n" \
                          "the beautiful moonlight.\n" \
                          "After a few minutes of gay wondering about\n" \
                          "the night sky nothing happens. What do you do?"
                else:
                    b_dead(albatros)
            else:
                if stayed < 2:
                    print "I didn't get that, so some time passes.\n" \
                          "The question remains, whacha gonna dú??"
                    pass
                else:
                    b_dead(albatros)


def b_corridor():
    b_not_ready()


def b_trap():
    b_not_ready()


def b_dwarf_room():
    b_not_ready()
