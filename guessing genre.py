#Atur cara bagi meneka genre
#!/usr/bit/env python

import random

def main():
    """Start a genre guessing game"""
    print("Guess the genre!")

    genre = [
      "rock kapak",
      "jiwang",
      "indie",
      "galau",
      "r&b"
      ]

#Pengisytiharan pemboleh ubah
    x = random.choice(genre)
    print(x)
    guess = None

    while x != guess:

#Input
      guess = str(input("What genre do you think I am thinking of?"))

#Output
    if x == guess:
            print("You guessed{}. Congratulations you're the smartest!".format(guess))
            break
    else:
            print("You guessed {}. Unfortunately you got it wrong booo. Please try again!".format(guess))

main()