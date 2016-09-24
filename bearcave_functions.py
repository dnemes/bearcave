# -*- coding: utf-8 -*-
# About this file:
# This is the file where I define the functions which make up the game.
#
# About naming conventions:
#   Functions
#       I will consequently add a 'b_' prefix to all function names to avoid any accidental clashes with
#       builtin functions.
#

import os
from sys import exit
from bearcave_globals import *


def b_printer(filename):
    """Function for printing .txt files in the project folder."""
    text_to_print = open(filename)
    print text_to_print.read()


def b_menu_nav():
    """Function which inserts the Menu Navigation into other functions. Use at end of function."""
    print "Type 'b' to get back to the Main Menu, or hit 'q' to exit the game."

    while True:
        command = raw_input("> ")

        if command in bv_commands['back_words']:
            b_main_menu()
        elif command in bv_commands['exit_words']:
            exit(0)
        else:
            pass


def b_dead(why):
    """Function to call, when the player dies."""
    print why, "Good job!"
    exit(0)


def b_disclaimer():
    """About page."""
    b_printer("disclaimer.txt")
    b_menu_nav()


def b_help():
    """Help page."""
    b_printer("help.txt")
    b_menu_nav()


def b_main_menu():
    # This function is going to be called first, when you start the game.
    # You will be able to get help, read about the background of this game,
    # and start the game. This function can also respond to some swearwords
    # in an interactive way.

    print "\nWelcome to The Bear Cave! \n"
    print "If you need help navigating the game, type 'help' next to the prompt."
    print "To find out what is this game, type 'about'."
    print "For leaving the game, type 'exit' !"
    print "If you feel ready to jump in, just write 'I will kick that stupid bear's ass!'. \n\nHave fun!"

    swear_count = 0

    while True:
        command = raw_input("> ")

        if command in bv_commands["help_words"]:
            b_help()
        elif command in bv_commands["about_words"]:
            b_disclaimer()
        elif command in bv_commands["start_game"]:
            b_start()
        elif command in bv_commands["swear_words"]:
            swear_count += 1
            if swear_count < 3:
                print "That is not a very nice thing to say."
                pass
            elif swear_count < 6:
                print "Frack you", swear_count, "times!"
                pass
            else:
                b_dead("You are especially rude, adventurer.\n"
                       "As a punishment, the bear comes out from the game,\n"
                       "rapes you and eats your face.")
        elif command in bv_commands["exit_words"]:
            print "'twas nice having you, great adventurer. \nSee you next time!"
            exit(0)
        else:
            print "I didn't understand that. \n" \
                  "Please type something like the four commands up there!\n"


def b_start():
    print "This is not ready yet."
    pass
