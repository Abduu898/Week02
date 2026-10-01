import sys
import random  
from hangman_bricks import show_word, max_penalties_for
import datetime

def get_today_date():
    today =datetime.date.today()
    return today.isoformat()

def load_best_score(filename):
    try:
        with open(filename, "r") as f:
            line = f.readline().strip()
            if line == "":
                return None
            parts = line.split()
            if len(parts)!=3:
                return None
            word = parts[0]
            attempts = int(parts[1])
            date = parts[2]
            return word, attempts, date
    except FileNotFoundError:
        return None
    except Exception:
        return None

def save_score(filename, word, attempts, date):
    try:
        with open(filename, "w") as f:
            f.write(word + " " + str(attempts) + " " + date + "\n")
    except Exception as e:
        print("Error: could not save score:", e, file=sys.stderr)

def load_words(filename):
    words =[]
    try:
        with open(filename,"r") as f:
            for line in f:
                word =line.strip()
                if len(word) >= 3 and word.isalpha():
                    words.append(word.lower())
    except FileNotFoundError:
        print("Error: file not found:",filename,file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print("Error: permission denied:",filename,file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("Error: could not read file:",e,file=sys.stderr)
        sys.exit(1)
    return words


def play_game(secret):
    max_penalties = max_penalties_for(secret)
    guessed = []
    penalties = 0
    print("Max penalties:", max_penalties)
    print()

    while True:
        print(show_word(secret,guessed), " || ", penalties,"penalties")
        won = True
        for letter in secret:
            if letter not in guessed:
                won = False
                break
        if won:
            print("You win! The word was:", secret)
            return True, penalties
        if penalties >= max_penalties:
            print("You lose! The word was:", secret)
            return False, penalties
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
                return True, penalties
            else:
                penalties = penalties + 5
                print(guess.upper() + ": incorrect guess")
def main():
    if len(sys.argv) < 2:
        print("Error: missing argument", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    words = load_words(filename)
    if len(words) == 0:
        print("Error: no valid words in file", file=sys.stderr)
        sys.exit(1)
    secret = random.choice(words)
    won, penalties = play_game(secret)

    best = load_best_score("scores.txt") ####
    today = get_today_date()

    if best is None:
        save_score("scores.txt", secret, penalties, today)
        print("Best ever! You guessed '" + secret + "' in", penalties, "attempts..")
    else:
        best_word, best_attempts, best_date = best
        if penalties < best_attempts:
            save_score("scores.txt", secret, penalties, today)
            print("Best ever! You guessed '" + secret + "' in", penalties, "attempts..")
        else:
            print("You guessed '" + secret + "' in", penalties, "attempts, but the record from", best_date, "is", best_attempts, "attempts .")







if __name__ == "__main__":
    main()