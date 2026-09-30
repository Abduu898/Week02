import random
import string
from hangman_bricks import show_word, max_penalties_for


def matches_pattern(word, pattern):
    if len(word) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] != "_":
            if word[i] != pattern[i]:
                return False
    return True


def filter_words(words, pattern):
    result = []
    for word in words:
        if matches_pattern(word, pattern):
            result.append(word)
    return result


def bot_guess(pattern, tried, words):
    possible = filter_words(words, pattern)

    if len(possible) == 0:
        for letter in string.ascii_lowercase:
            if letter not in tried:
                return letter
        return None

    frequency = {}
    for word in possible:
        for letter in word:
            if letter not in tried:
                if letter not in frequency:
                    frequency[letter] = 0
                frequency[letter] = frequency[letter] + 1

    if len(frequency) == 0:
        return None

    best_letter = None
    best_count = -1
    for letter in frequency:
        if frequency[letter] > best_count:
            best_count = frequency[letter]
            best_letter = letter
    return best_letter


def play_one_game(words, max_penalties=12):
    secret = random.choice(words)
    pattern = "_" * len(secret)
    tried = []
    penalties = 0

    while True:
        if "_" not in pattern:
            return True, penalties

        if penalties >= max_penalties:
            return False, penalties

        letter = bot_guess(pattern, tried, words)

        if letter is None:
            return False, penalties

        tried.append(letter)

        if letter in secret:
            new_pattern = ""
            for i in range(len(secret)):
                if secret[i] == letter:
                    new_pattern = new_pattern + letter
                else:
                    new_pattern = new_pattern + pattern[i]
            pattern = new_pattern
        else:
            penalties = penalties + 1


def run_bot_games(words, nb_games=100):
    wins = 0
    total_penalties = 0

    for i in range(nb_games):
        won, penalties = play_one_game(words)
        if won:
            wins = wins + 1
        total_penalties = total_penalties + penalties

    win_rate = wins / nb_games * 100
    avg_penalties = total_penalties / nb_games

    print("Games played:", nb_games)
    print("Wins:", wins)
    print("Losses:", nb_games - wins)
    print("Win rate:", round(win_rate, 2), "%")
    print("Average penalties:", round(avg_penalties, 2))


def load_words(filename):
    words = []
    with open(filename, "r") as f:
        for line in f:
            word = line.strip()
            if len(word) >= 3 and word.isalpha():
                words.append(word.lower())
    return words


if __name__ == "__main__":
    words = load_words("google-10000-english.txt")
    print("Total words:", len(words))
    run_bot_games(words, 100)