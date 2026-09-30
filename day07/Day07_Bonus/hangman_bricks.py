# hangman_bricks.py

def show_word(secret, guessed):
    display = ""
    for letter in secret:
        if letter in guessed:
            display = display + letter.upper() + " "
        else:
            display = display + "_ "
    return display


def get_secret_word():
    while True:
        word = input("Enter a secret word (letters only, min 3): ").strip().lower()
        if len(word) < 3:
            print("Too short. Min 3 letters.")
            continue
        if not word.isalpha():
            print("Letters only, please.")
            continue
        return word


def clear_screen():
    print("\n" * 50)


def max_penalties_for(word):
    p = 6 + (10 - len(word))
    if p < 6:
        p = 6
    if p > 12:
        p = 12
    return p


def play_round(secret, max_penalties):
    guessed = []
    penalties = 0

    while True:
        print(show_word(secret, guessed), " || ", penalties, "penalties")

        won = True
        for letter in secret:
            if letter not in guessed:
                won = False
                break
        if won:
            print("You win! The word was:", secret)
            return penalties

        if penalties >= max_penalties:
            print("You lose! The word was:", secret)
            return penalties

        guess = input(">> ").strip().lower()

        if guess == "":
            continue

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
                print(guess.upper() + ": correct guess")
                print("You win! The word was:", secret)
                return penalties
            else:
                penalties = penalties + 5
                print(guess.upper() + ": incorrect guess")