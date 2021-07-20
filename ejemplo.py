# -*- coding: utf-8 -*-

from rsa import *

string = input("Enter your text: ")
voice = 8
velocity = 10
traduction = translate(string)
say(traduction, voice, velocity)

