#!/usr/bin/env python

import random

def main():
    """Start a music guessing game between ."""
    print("Guess the music genre!")

    x = random.randint(1, 100)
    guess = None

    while x != guess:

        guess = int(input("Pick a number between 1 to 100: "))

        if x == guess:
            print("!!!You're a genius!!!")
        elif x > guess:
            print("Try a bigger number") 
        elif x < guess:
            print("Try a smaller number")     
main()   

    
    