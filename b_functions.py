#!/usr/bin/python
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
import time
import threading
from sys import exit
from b_globals import *
import random


# -----------------------------------------------------------------------------
# PLAYER CLASS for storing data of current player:
class BPlayer(object):
    """This is the player class. Please use the class methods (inv_add and
    ach_add respectively) for filling the list-attributes (inventory 'inv'
    and achievements 'ach')

    Attributes:
        name: The player's name.
        inventory: A list of strings representing the players possessions.
        health: A positive integer.
        achievements: A list of strings.
        gold: A positive integer.
        points: A positive integer (not sure if i will use it).
        visited: An empty list for storing the IDs of rooms visited.
    """

    def __init__(self, name, inv, health, ach, gold, points):
        i_list = []
        a_list = []
        if inv:
            i_list = inv.split((', ' or ',' or ' '))
        if ach:
            a_list = ach.split((', ' or ',' or ' '))
        self.name = name
        self.inventory = i_list
        self.health = health
        self.achievements = a_list
        self.gold = gold
        self.points = points
        self.visited = []
        self.attack = 6
        self.damage = 2

    def print_current_state(self):
        """Prints all data stored in the instance of the BPlayer object.
        Formatting is not perfect, requires some fixing later."""
        print "-------------------------"
        print "Inventory:\t", self.inventory
        print "Health:\t\t", self.health
        print "Achievements:\t", self.achievements
        print "Gold:\t\t", self.gold
        print "Attack:\t\t", self.attack
        print "Damage:\t\t", self.damage
        print "-------------------------"

    def inv_add(self, new_item, print_it):
        """Adds item to inventory list. If 'print_it' is set to true, a
        message is printed."""
        self.inventory.append(new_item)
        if print_it:
            print "'{}' is added to inventory.".format(new_item)

    def inv_print(self):
        """Print all the contents of the inventory."""
        print "These items are in your inventory:"
        for i in self.inventory:
            print "{},".format(i),
        print

    def ach_add(self, new_item, print_it):
        """Adds item to achievements list. If 'print_it' is set to true, a
        message is printed."""
        self.achievements.append(new_item)
        if print_it:
            print "New Achievement Achieved: '{}'".format(new_item)

    def ach_print(self):
        """Prints achievements list."""
        print "These are your achievements:"
        for i in self.achievements:
            print "{},".format(i),
        print

    def ch_health(self, change, print_it):
        """Changes the health attribute by 'change' amount of HP.
           Use integers."""
        self.health += change
        if print_it:
            print "Now you have {} health points.".format(self.health)

    def ch_gold(self, change):
        """Changes the gold attribute by 'change' amount. Use integers."""
        self.gold += change
        print "You have {} Gold.".format(self.gold)

    def ch_points(self, change):
        """Changes the points attribute by 'change' amount. Use integers."""
        self.points += change
        print "You have {} points.".format(self.points)

    def vis_add(self, new_item, print_it):
        """Add ID of visited scene to self.visited[]. Prints message, if
        print_it is set to True."""
        self.visited.append(new_item)
        if print_it:
            print "This scene also visited: {}".format(new_item)

    def vis_print(self):
        """Prints a list of scenes visited"""
        print "These are the scenes you visited:"
        for i in self.visited:
            print "{}, ".format(i)


# -----------------------------------------------------------------------------
# GAME FUNCTIONS. These are modular parts, some are used in other functions.
def b_not_ready(nextscene):
    """Prints a message, and goess back to the main menu."""
    print "\n*-----------------------*"
    print "*", nextscene, "\t\t*"
    print "* ... is not ready yet. *\n" \
          "*-----------------------*\n\n" \
          "-returning to Main Menu-\n"
    b_main_menu()


def b_printer(filename):
    """Function for printing .txt files in the texts/ folder."""
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    openfilename = os.path.join(file_dir, filename)
    text_to_print = open(openfilename)
    print text_to_print.read()
    text_to_print.close()


def b_menu_nav():
    """Function which inserts the Menu Navigation into other functions.
    Use at end of function."""
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


# -----------------------------------------------------------------------------
# MENU ITEMS. These functions make up the pages of the menu.
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
            print "'twas nice having you, great adventurer." \
                  "\nSee you next time!"
            exit(0)
        else:
            print "I didn't understand that. \n" \
                  "Please type something like the four commands up there!"


def b_disclaimer():
    """About page."""
    b_printer("texts/disclaimer.txt")
    b_menu_nav()


def b_help():
    """Help page."""
    b_printer("texts/help.txt")
    b_menu_nav()


# -----------------------------------------------------------------------------
# START SCREEN. Here the player gives a name, and a player object is created.
# This is basically the first scene, so visiting this has to be counted in
# player.visited[].
#
def b_start():
    """Here we ask the player for a name and create an instance of the BPlayer
    class, with that name."""
    print "What is your name?"

    name = raw_input(" > ")
    global player
    player = BPlayer(name, 0, 10, 0, 0, 0)
    player.vis_add('b_start', 0)

    print "Welcome to the game,", name, "!"
    print "These are your stats:"
    player.print_current_state()

    print "Are you ready to start the game?" \
          "\nType 'y' for Yes, 'n' for No."

    while True:
        command = raw_input(" > ")

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

    player.vis_add('b_first_room', 0)

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
    player.vis_add('b_bottom_of_the_well', 0)

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
    """Corridor. Can go ahead. That's all you can do."""
    b_printer('texts/corridor.txt')
    indecision = 0
    player.vis_add('b_corridor', 0)

    while True:
        command = raw_input(" > ")

        if command in bv_commands['go']:
            print "You start walking through the corridor..."
            b_trap()
            exit(0)
        elif command in bv_commands['take_torch']:
            print "You approach the torches..."
            b_trap()
            exit(0)
        elif command in bv_commands['turn_off_lights']:
            b_corridor_lights_out()
            exit(0)
        else:
            if indecision < 1:
                indecision += 1
                print "I didn't catch you."
            elif indecision < 2:
                indecision += 1
                print "You were saying?"
            else:
                b_dead("I have two kittens who are more determined than that.\n"
                       "You die of procrastination. (Very common nowadays.)")


def b_corridor_lights_out():
    """You can find the sword here, and see the trap."""
    player.vis_add('b_corridor_lights_out', 0)
    b_printer('texts/corridor_lights_out.txt')
    while True:
        command = raw_input(" > ")

        if command in bv_commands[
            'look_around'] and 'sword' not in player.inventory:
            print "You approach the shiny thing to your right, and you\n" \
                  "realize that it is a sword embedded into the wall. You\n" \
                  "can grab it by it's handle, and shake it free."
            player.inv_add('sword', 1)
            print "What do you do now?"
        elif command in bv_commands['go']:
            print "You start to approach the lines on the floor..."
            b_trap()
            exit(0)
        else:
            print "Sorry, I didn't catch you..."


def b_trap():
    print "The floor suddenly disappears behind your feet." \
          "You start to fall.\nWhat do you do? HURRY!"

    global isinput
    isinput = 0

    def command_listener():
        """This listens to commands, and also reacts."""
        while True:
            command = raw_input(" > ")
            if waiter.is_alive():
                if command in bv_commands["jump"] or command in bv_commands[
                    "climb"]:
                    global isinput
                    isinput += 1
                    print "We go to the next room!"
                    waiter.join()
                    player.vis_add(b_trap, 0)
                    b_dwarf_room()
                    exit(0)
                else:
                    print "Sorry, I didn't get that"
            else:
                exit(0)

    def wait_sometime():
        """Waits 5 seconds, then kill player. Also interrupts thread."""
        time.sleep(5)
        global isinput
        if isinput:
            exit(0)
        else:
            b_dead(
                "\nYou fall into the deep hole in the floor, and die when you\n"
                "hit the bottom fifty meters down. : (\n\n"
                "(Hit Return/Enter to quit!)\n")

    listener = threading.Thread(target=command_listener)
    waiter = threading.Thread(target=wait_sometime)

    waiter.start()
    listener.start()


def b_dwarf_room():
    """Dwarf Room Scene"""
    player.vis_add(b_dwarf_room, 0)
    b_printer("texts/kapanyanyimonyok.txt")
    while True:
        command = raw_input(" > ")

        if command in bv_commands['accept'] or command in bv_commands['yes']:
            b_printer('texts/kapanyanyimonyok_mission.txt')
            b_bear_room()
            exit(0)
        elif command in bv_commands['refuse'] or command in bv_commands['no']:
            b_dead("\n'I won't do your stupid mission Kapanyányimonyók!' you "
                   "say.\nThe kapanyányimonyók gets very angry, and eats his\n"
                   "mush from your stomach!"
                   )
        elif command in bv_commands['kill']:
            if 'sword' in player.inventory:
                b_dead("\nYou attack the kapanyányimonyók with your rusty\n"
                       "sword, and he dodges your attack.\n"
                       "'You anyámasszonykatonája!' you shout, and try to hit\n"
                       "him again. He dodges again, and as you turn, you lose\n"
                       "your balance, and fall. You lose the sword.\n"
                       "He takes the sword, turns you onto your back, "
                       "and\neats his mush from your stomach. You die!"
                       )
            else:
                b_dead("\nHe jumps you as you start to attack him, turns you\n"
                       "onto your back, and eats his mush from your stomach.\n"
                       "You die!"
                       )
        else:
            print "That's not an answer to this situation. : ( "


def b_bear_room():
    """This is the scene, where you meat the bear"""

    b_printer('texts/bear_room.txt')
    while True:
        command = raw_input(" > ")

        if command in bv_commands['kill']:
            print "You prepare yourself and launch yourself on the bear."
            b_bear_fight()
            exit(0)
        elif command in bv_commands['take_honey']:
            b_dead("The bear looks at you wondering, then slaps your face\n"
                   "off. He than eats his honey.")
        elif command in bv_commands['eat_cheesecake']:
            b_dead("The bear gets pissed off at you for eating its\n"
                   "cheesecake, and takes some time chewing your legs off.")
        else:
            print "Sorry, I don't know what you mean..."


def b_bear_fight():
    """This function contains the fight mechanisms."""
    bear_hp = 8
    bear_attack = 11
    bear_damage = 3
    if 'sword' in player.inventory:
        player.attack += 3
        player.damage += 2

    player.print_current_state()

    while bear_hp > 0 and player.health > 0:
        random_index = random.randint(0, len(bv_bear_fight) - 1)
        print bv_bear_fight[random_index][0]
        player_roll = random.randint(1, player.attack)
        if bear_attack <= 1:
            bear_attack = 3
        bear_roll = random.randint(1, bear_attack)
        print 'You rolled %d and the bear rolled %d' % (player_roll, bear_roll)
        if player_roll >= bear_roll:
            print bv_bear_fight[random_index][1]
            bear_hp += -player.damage
            print '  Bear hp:', bear_hp
            bear_attack += bv_bear_fight[random_index][2]
            print '  Bear attack', bear_attack
            print '*You win this attack.'
            print '----------------'
        else:
            player.ch_health(-bear_damage, 0)
            print 'Your attack fails, you loose', bear_damage, 'health.'
            print '  Now your health is', player.health
            print '*The bear wins this attack.'
            print '----------------'

    if bear_hp <= 0:
        print "You killed the bear, and you collected the honey."
        player.inv_add('honey', 1)
        if player.health == 10:
            player.ach_add("The Mighty Bearslayer", 1)
        else:
            player.ach_add("Survived the bear", 1)
        b_gold_chest()
        exit(0)
    else:
        b_dead("The bear kills you.")


def b_gold_chest():

    print "You also find a small chest, full of gold behind the corpse"
    print "of the big animal."
    print "How much gold do you take?"

    how_much = None
    while how_much is None:
        command = raw_input("> ")
        try:
            how_much = int(command)
        except ValueError:
            b_dead("You die. Type a number next time.")

    if how_much < 50:
        print "Nice, you're not greedy, you can keep the gold!"
        player.ch_gold(how_much)
        player.ach_add("Especially decent guy, who is not greedy at all.", 1)
        b_final_scene()
        exit(0)
    else:
        b_dead("You greedy bastard! You should have taken less. A demon\n"
               "takes your soul to the Nether, you die.")


def b_final_scene():
    """I think the title is pretty descriptive."""
    b_printer('texts/final.txt')

    while True:
        command = raw_input(" > ")

        if command in (bv_commands['keep_honey'] or bv_commands['refuse']):
            b_dead("You refuse to give the honey to the kapanyányimonyók,\n"
                   "so he takes it from you while tying you up, and eating\n"
                   "his now honey flavoured mush from your stomach : ( ")
        elif command in (bv_commands['give_back'] or bv_commands['accept']):
            player.inventory.remove('honey')
            print "The kapanyányimonyók eats the honey, and you kill it in"
            print "the meantime.\nYou win!"
            player.ach_add("Sneaky backstabber", 0)
            player.ach_add("Winner", 0)
            print "Your stats: "
            player.print_current_state()
            exit(0)
        else:
            print "Pls. decide already."
