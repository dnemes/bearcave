#!/usr/bin/python
# -*- coding: utf-8 -*-
# I store here all the global variables.
#
# 1. "bv_commands" dictionary, which is a dictionary  where keys are the
# "names" of the commands, and "elements" are lists of acceptable phrasings
# for those commands.

player = 0

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
        "asshole",
        "shitface",
        "assface"
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
        'not the right, the other one',
        'take left',
        'take a left',
        'take a left turn'
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
        'not the left, the other one',
        'take right',
        'take a right',
        'take a right turn'
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
    'take_torch': [
        "get torch",
        "take torch",
        "pick up torch"
    ],
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
    ],
    'go': [
        "go",
        "Go",
        "GO",
        "go ahead",
        "forward",
        "ahead",
        "continue",
        "carry on"
    ],
    'inventory': [
        "i",
        "inv",
        "inventory",
        "backpack",
        "bag",
        "check inventory",
        "open bag",
        "open backpack"
    ],
    'where_am_i': [
        "whereami",
        "where am i?",
        "where am i",
        "wai"
    ],
    'look_around': [
        "look around",
        "check room",
        "check everything",
        "check"
    ],
    'jump': [
        "jump",
        "jump out",
        "jump forward",
        "leap forward",
        "leap",
        "leap out",
        "hop out"
    ]
}
