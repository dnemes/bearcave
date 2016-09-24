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
#
#
# .

bv_commands = {
    'start_game': [
        "I will kick that stupid bears ass!",
        "start",
        "go",
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
    'exit_words': [
        "exit",
        "exit game",
        "quit game",
        "quit",
        "leave",
        "q",
        "x",
        "leave game"
    ],
    'back_words': [
        "b",
        "back",
        "go back",
        "go up"
    ],
    'about_words': [
        "a",
        "about",
        "disclaimer"
    ],
    'help_words': [
        "h",
        "help",
        "help me"
    ]
}


class BVPlayer(object):
    """This is the player class.

    Attributes:
        inventory: A list of unique strings representing the players possessions.
        health: A positive integer.
        achievements: A list of unique strings.
        gold: A positive integer.
        points: A positive integer (not sure if i will use it).
    """

    def __init__(self, inventory, health, achievements, gold, points):
        self.inventory = inventory
        self.health = health
        self.achievements = achievements
        self.gold = gold
        self.points = points

    def print_current_state(self):
        """Prints all data stored in the instance of the BVPlayer object."""
        print self.inventory
        print self.health
        print self.achievements
        print self.gold
        print self.points
