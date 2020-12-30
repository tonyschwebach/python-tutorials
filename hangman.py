# hangman.py
# tony schwebach
# 11/8/2020
# notes

import random

def hangman():
    
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    word = random.choice(["hidden","taz","kip","roxy"])
    attempts = 10
    guessmade = ""

    print(f"Hello, {name}. Try to guess the word in {attempts} attempts.")
    
    #populate hidden worded and guessed letters. 1st round is none guessed
    while len(word) > 0:
        main = ""
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main +"_ "
        if main == word:
            print(f"{word}. You win!")
            break
        print(f"Guess the word: {main}")
        
        #takes guesses from user
        guess = input("Guess a letter: ")     
        while guess not in validLetters:
            guess = input("Invalid character. Guess a letter: ")
        guessmade = guessmade + guess

    
        #if incorrect guess, draw hangman
        if guess not in word:
            attempts -= 1
            print(f"{attempts} attempts remaining")
            if attempts <= 9: 
                print("-----------")
            if attempts <= 8:
                print("     ]    |")
            if attempts <= 7:
                print("    0     |")
            if attempts == 6:
                print("    |     |")
            if attempts == 5:
                print("   \|     |")
            if attempts <= 4:
                print("   \|/    |")
            if attempts <= 3:
                print("    |     |") 
            if attempts == 2:
                print("    /     |") 
            if attempts <= 1:
                print("    /\    |")   
            if attempts ==0:
                print("          |")
                print("-----------")
                print()
                print("  x   x ")
                print("   ---   ")
                print()
                print(f"Word: {word}. You lose.")
                break

name = input("What is your name? ")
hangman()



