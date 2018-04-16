# -*- coding: utf-8 -*-

'''
This script has for funtionality translate one text to voice in
the International Radiotelephony Spelling Alphabet.
Project: https://github.com/deltahat/RadiotelephonySpellingAlphabet
Dependencies in linux: espeak
Dependencies in python: pyttsx3
'''

import pyttsx3

__author__ = "deltahat"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "deltahat"
__status__ = "Production"


# Translate function
def transalte(text):
    text = text.upper()
    alphabet = {
        " ": " ", "A": "Alpha", "B": "Beta", "C": "Charlie", "D": "Delta",
        "E": "Echo", "F": "Foxstrot", "G": "Golf", "H": "Hotel", "I": "India",
        "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November",
        "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra",
        "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey",
        "X": "X-Ray", "Y": "Yankee", "Z": "Zulu"
    }
    radioAlphabet = ""
    for letter in range(len(text)):
        text = list(text)
        radioAlphabet = radioAlphabet + ". " + alphabet[text[letter]]
    return radioAlphabet


# Speake function
def say(text, voiceid, velocity):
    eng = pyttsx3.init()
    listVoices = eng.getProperty('voices')
    eng.setProperty('voice', listVoices[voiceid].id)
    eng.setProperty('velocity', velocity)
    eng.say(text)
    eng.runAndWait()


string = input("Enter your text: ")
traducction = transalte(string)
say(traducction, 10, 40)
