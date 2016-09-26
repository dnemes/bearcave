# -*- coding: utf-8 -*-
# About this file:
# This is the file where I define the functions which make up the game.
#
# About naming conventions:
#   Functions
#       I will consequently add a 'b_' prefix to all function names to avoid
#       any accidental clashes with builtin functions.
#

import os
from sys import exit
from bearcave_globals import *


def b_not_ready():
    # Prints a message, and exits.
    print "*------------------------*\n" \
          "* This is not ready yet. *\n" \
          "*------------------------*"
    exit(0)


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
        elif command in bv_commands["exit_words"]:
            print "'twas nice having you, great adventurer. \nSee you next time!"
            exit(0)
        else:
            print "I didn't understand that. \n" \
                  "Please type something like the four commands up there!\n"


def b_start():
    # Here we ask the player for a name and create an instance of the BVPlayer
    # class, with that name.
    print "What is your name?"

    name = raw_input("> ")
    player = BVPlayer(name, 10, 0, 0)

    print "Welcome to the game,", name, "!"
    print "These are your stats:"
    player.print_current_state()

    print "Are you ready to start the game?" \
          "\nType 'y' for Yes, 'n' for No."

    command = raw_input("> ")

    while True:
        if command in bv_commands['yes_words']:
            b_first_room()
        elif command in bv_commands['no_words']:
            b_main_menu()
        else:
            print "Sorry, that's not a yes or a no. Try to answer again, \n" \
                  "I swear it's not that hard."


# def b_yes_no(question, print_it, yes_command, no_command):
#     # This is for inserting Yes-No-Questions into other elements
#     # (like b_start()...)
#     if print_it:
#         print question, "\nType 'y' for Yes, 'n' for No."
#     else:
#         pass
#
#     command = raw_input("> ")
#
#     while True:
#         if command in bv_commands['yes_words']:
#             assert isinstance(yes_command, object)
#             exec yes_command
#         elif command in bv_commands['no_words']:
#             assert isinstance(yes_command, object)
#             exec no_command
#         else:
#             print "Sorry, that's not a yes or a no. Try to answer again, \n" \
#                   "I swear it's not that hard."


def b_first_room():
    b_not_ready()


def b_bottom_of_the_well():
    b_not_ready()


def b_corridor():
    b_not_ready()


def b_trap():
    b_not_ready()


def b_dwarf_room():
    b_not_ready()
