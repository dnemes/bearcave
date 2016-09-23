# -*- coding: utf-8 -*-
# About this file:
# This is the file where I define the functions which make up the game.
#
# About naming conventions:
#   ---------
#   General
#       If a name of any object is made up of several words, I will use '_' characters to separate them.
#       I will not use uppercase letters in these names.
#   ---------
#   Functions
#       I will consequently add a 'b_' prefix to all function names to avoid any accidental clashes with
#       builtin functions.
#
#   ---------
#   Variables
#       Global variables: prefix: 'g_'.
#       I plan to store certain data (like health points and inventory contents and the fulfillment of
#       certain criteria) about the game-play in global variables and make these available to other functions.
#       Local variables: i won't give locals prefixes.
#

import os
from sys import exit


def b_printer(filename):
    text_to_print = open(filename)
    print text_to_print.read()


def b_menu_nav():
    print "Type 'b' to get back to the Main Menu, or hit 'q' to exit the game."

    while True:
        command = raw_input("> ")

        if command == "b":
            b_main_menu()
        elif command == "q":
            exit(0)
        else:
            pass


def dead(why):
    print why, "Good job!"
    exit(0)

def b_disclaimer():
    b_printer("disclaimer.txt")
    b_menu_nav()


def b_help():
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
    print "If you feel ready to jump in, just write 'I will kick that stupid bears ass!'. \n\nHave fun!"

    start_game = ['I will kick that stupid bears ass!', 'start', 'go', 'kill bear', 'bear hunter', 'hunt']
    swear_words = ["fuck", "screw", "screw you" ,"fuck you", "this game is stupid", "cunt", "ass", "fucktwat"]
    exit_words = ["exit", "quit", "leave", "q", "x"]
    swear_count = 0

    while True:
        command = raw_input("> ")

        if command == "help":
            b_help()
        elif command == "about":
            b_disclaimer()
        elif command in start_game:
            b_start()
        elif command in swear_words:
            swear_count += 1
            if swear_count < 3:
                print "That is not a very nice thing to say."
                pass
            elif swear_count < 6:
                print "Fuck you", swear_count, "times!"
                pass
            else:
                dead("You are especially rude, adventurer.\nAs a punishment, the bear comes out from the game,\nrapes you and eats your face.")
        elif command in exit_words:
            print "'twas nice having you, great adventurer. \nSee you next time!"
            exit(0)
        else:
            print "I didn't understand that. \nPlease type something like the four commands up there!\n"


def b_start():
    pass


