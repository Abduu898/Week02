import argparse
import random
from english_words import english_words_lower_set

from firstBrick import you_lose
from secondBrick import random_item     
from thirdBrick import underscore       


def parse_args():
    parser = argparse.ArgumentParser(description="Hangman game")
    parser.add_argument("--max-penalties", type=int, default=12,help="penalties before losing (default: 12)")
    parser.add_argument("--min-length", type=int, default=5,help="minimum secret word length (default: 5)")
    parser.add_argument("--max-length", type=int, default=10,help="maximum secret word length (default: 10)")
    return parser.parse_args()



def show_word(secret, guessed):
    display = ""
    for letter in secret:
        if letter in guessed:
            display = display + letter.upper() + " "
        else:
            display = display + "_ "
    return display

def play(args):
    words = [w for w in english_words_lower_set
         if args.min_length <= len(w) <= args.max_length]
    if not words:
        print("No words match the criteria.")
        return

    secret = random.choice(words)
    guessed = []
    penalties = 0
    max_penalties = args.max_penalties

    print("Welcome to Hangman!")
    print()

    while True:
        print(show_word(secret, guessed), " || ", penalties,"penalty" if penalties == 1 else "penalties")

        won = True
        for letter in secret:
            if letter not in guessed:
                won = False
                break
        if won:
            print("You win! The word was:", secret)
            return

        if penalties >= max_penalties:
            print("You lose! The word was:", secret)
            return

        guess = input(">> ").strip().lower()
        if guess == "":
            continue

        if len(guess) == 1:
            if guess in guessed:
                print("You already tried", guess.upper())
                continue
            guessed.append(guess)

            if guess in secret:
                count = secret.count(guess)
                if count == 1:
                    print("Found one '" + guess.upper() + "'")
                else:
                    print("Found", count, "'" + guess.upper() + "'")
            else:
                penalties = penalties + 1
                print("No '" + guess.upper() + "' found")
        else:
            if guess == secret:
                print(guess.upper() + ": correct guess - " + str(penalties) + " penalties")
                print("You win! The word was:", secret)
                return
            else:
                penalties = penalties + 5
                print(guess.upper() + ": incorrect guess")


args = parse_args()
play(args)