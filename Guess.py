 -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:33:19 2020

@author: Gulshan Chandolia


"""

#This was done to check the shh key

#check amit's fork


import random

num = random.randint(1,20)

chances = 0

while chances < 5:
    
    guess = int(input("Guess a Number between 1 to 20:"))
    
    if guess == num :
        
        print("Correct Guess")
        
        break
    
    elif guess < num:
        
        print("Guess is too low Guess higher number")
        
    else:
        
        print("Guess is too high Guess lower number")
        
    chances += 1
    
if not chances < 5:
    
    print("Wrong Guesses : The Number is ")
    
    print(num)

