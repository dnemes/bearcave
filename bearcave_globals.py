# # -*- coding: utf-8 -*-
# I store here all the global variables.
#
# 1. "bv_commands" dictionary, which is a dictionary  where keys are the
# "names" of the commands, and "elements" are lists of acceptable phrasings
# for those commands.
#
# 2. "bv_player (object)" is a class, which contains the following:
#  - "inventory" is a list, where I store the things in the player's
# possession. This list is empty by default, and can be modified with
# the builtin list methods.
#  - "health" is a positive int. Starting value is 10. It can be
# modified during the game.
#  - "achievements" is also a list, containing the achievements of the
# player.
#  - "gold" is the amount of gold.
#  - "points" is the amount of points (I'm not sure i will use it.)
#
#
#

bv_commands = {
    'start_game': [
        "I will kick that stupid bears ass!",
        "kick",
        "go",
        "start",
        "kill bear",
        "bear hunter",
        "hunt",
        "kill",
        "play game",
        "start game"
    ],
    'swear_words': [
        "fuck",
        "screw",
        "screw you",
        "fuck you",
        "this game is stupid",
        "cunt",
        "ass",
        "fucktwat",
        "you ass",
        "dick",
        "you dick",
        "asshole"
    ],
    'exit': [
        "exit",
        "exit game",
        "quit game",
        "quit",
        "leave",
        "q",
        "x",
        "leave game"
    ],
    'back': [
        "b",
        "back",
        "go back",
        "go up"
    ],
    'about': [
        "a",
        "about",
        "disclaimer"
    ],
    'help': [
        "h",
        "help",
        "help me"
    ],
    'yes': [
        "y",
        "Y",
        "YES",
        "yes",
        "Yes"
    ],
    'no': [
        "n",
        "N",
        "no",
        "NO",
        "No"
    ],
    'left': [
        'l',
        'L',
        'left',
        'Left',
        'LEFT',
        'go l',
        'GO L',
        'go left',
        'Go Left',
        'GO LEFT',
        "let's take a leftie",
        'leftie',
        'not the right, the other one'
    ],
    'right': [
        'r',
        'R',
        'right',
        'Right',
        'RIGTH',
        'go r',
        'GO R',
        'go right',
        'Go Right',
        'GO RIGTH',
        "let's take a rightie",
        'not the left, the other one'
    ],
    'turn_off_lights': [
        "turn of",
        "Lights off!",
        "put out light",
        "turn off the light",
        "turn light off",
        "put torch out",
        "extinguish torch",
        "kill lights"
    ],
    'take_torch': [],
    'stay': [
        "s",
        "stay",
        "sit down",
        "don't go",
        "dont go"
    ],
    'climb': [
        "climb",
        "climb walls",
        "climb up",
        "climb out"
    ]
}


class BVPlayer(object):
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
