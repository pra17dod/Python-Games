import random
import os

os.system('clear')

print("         ~~~ Welcome to Hangman ~~~       ")
print("This is a simple version of the Hangman game")
print("- You can guess a word one letter at a time.")
print("- You have a maximum of 10 unsuccessful tries.")
print("- You can play more than one round.")


words = [
    "football",
    "hangman",
    "colorful",
    "kite",
    "science",
    "programming",
    "python",
    "mathematics",
    "videogame",
    "apple",
    "orange",
    "water",
    "github",
    "django",
]

game = True
while(game):
    res = input("\nDo you want to play hangman (Y/N)?")
    res = str(res)
    if res == 'N' or res == 'n':
        game = False
        print("Thanks for playing!")
        exit()
    elif res == 'Y' or res == 'y':
        word = random.choice(words)
        print("\nGuess the word")
        corr_guess = ""
        wrong_guess = ""

        turns = 10
        while turns > 0:
            remain = 0
            print("\nWord in progress: ")
            for char in word:
                if char in corr_guess:
                    print(char, end="")
                else:
                    print(" _ ", end="")
                    remain += 1
            
            if remain == 0: 
                print("\n\nYou Win!!")
                break

            guess = input("\n\nEnter a letter: ")

            if guess not in word:
                turns -= 1
                print("\nNot in this word:", +turns,"turns left")

                wrong_guess += guess
                if turns == 0:
                    print("\n\nYou lose!!")
                    break
            else:
                corr_guess += guess
            print("Guessed letters:",str(corr_guess)," ",str(wrong_guess))