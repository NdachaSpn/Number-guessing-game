# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:32:35 2020

@author: Simon
"""

import random

print ("Welcome to the number guesssing game")
n= random.randint(1,25)
chances=4

print("guess any number between 1 and 25:")
while chances<=4:
    guess=int(raw_input())
        if guess<number:
            print("The number you guessed is too low.Pease try again")
        elif guess>number:
            print("The number you entered is too high.Please try again")
        elif guess==number: 
            print("Congratulations!!1you got it right")
        else:
        print ("YOU LOSE!!!!Better luck next time")
    break
print           