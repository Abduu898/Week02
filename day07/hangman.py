import random
from english_words import english_words_lower_set

from firstBrick import you_lose
from secondBrick import random_item
from thirdBrick import underscore
history = []

WORDS = [w for w in english_words_lower_set if 5 <= len(w) <= 10]

def random_word():
    return random.choice(WORDS)

def show_word(secret, guessed):
    display = ""
    for letter in secret:
        if letter in guessed:
            display = display + letter.upper() + " "
        else:
            display = display + "_ "
    return display

def play():
    secret = random_word()
    guessed = []
    penalties = 0
    max_penalties = 12

    print("Welcome to Hangman!")
    print()

    while True:
        print(show_word(secret, guessed), " || ", penalties,
              "penalty" if penalties == 1 else "penalties")

        won = True
        for letter in secret:
            if letter not in guessed:
                won = False
                break
        if won:
            print("You win! The word was:", secret)
            return {"word": secret, "won": True, "penalties": penalties}


        you_lose(penalties)
        if penalties >= max_penalties:
            print("The word was:", secret)
            return {"word": secret, "won": False, "penalties": penalties}

        guess = input(">> ").strip().lower()

        if guess == "":
            continue
###################################
        if guess == "?":
            all_found = True
            for letter in secret:
                if letter not in guessed:
                    all_found = False
                    break
            if all_found:
                print("The word is already fully revealed.")
                continue
            if penalties + 2 >= max_penalties:
                print("Can't take a hint — it would end the game.")
                continue

            remaining = []
            for letter in secret:
                if letter not in guessed and letter not in remaining:
                    remaining.append(letter)

            chosen = random.choice(remaining)
            guessed.append(chosen)
            penalties = penalties + 2

            print("Hint: the word contains '" + chosen.upper() + "'. (+2 penalties)")
            continue
###############3
        if len(guess) == 1:
            if guess in guessed:
                print("You already tried", guess.upper())
                continue

            guessed.append(guess)

            if guess in secret:
                print("Found one '" + guess.upper() + "'")
            else:
                penalties = penalties + 1
                print("No '" + guess.upper() + "' found")

        else:
            if guess == secret:
                print(guess.upper() + ": correct guess - " + str(penalties) + " penalties")
                print("You win! The word was:", secret)
                return {"word": secret, "won": True, "penalties": penalties}
            else:
                penalties = penalties + 5
                print(guess.upper() + ": incorrect guess")

def win_rate(history):
    if not history:
        return 0.0

    wins = 0
    for game in history:
        if game["won"]:
            wins = wins + 1

    return wins / len(history) * 100


def avg_penalties_on_wins(history):
    total = 0
    count = 0

    for game in history:
        if game["won"]:
            total = total + game["penalties"]
            count = count + 1

    if count == 0:
        return 0

    return total / count


def longest_word_won(history):
    longest = ""

    for game in history:
        if game["won"] and len(game["word"]) > len(longest):
            longest = game["word"]

    return longest

while True:
    result = play()
    history.append(result)

    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        break

print()
print("----- Stats -----")
print("Games played:", len(history))
print("Win rate:", round(win_rate(history), 1), "%")
print("Average penalties on wins:", round(avg_penalties_on_wins(history), 1))
print("Longest word found:", longest_word_won(history))

