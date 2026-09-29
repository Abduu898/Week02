import random
from english_words import english_words_lower_set


def scramble(word):
    letters = list(word)      
    n = len(letters)

    if len(set(letters)) <= 1: ## set stores multip items on a single var 
        return None
    # Fisher–Yates shuffle
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        letters[i], letters[j] = letters[j], letters[i]
    result = "".join(letters)   # turn list back into string

    # If by chance it's still the same as the original, reshuffle
    while result == word:
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            letters[i], letters[j] = letters[j], letters[i]
        result = "".join(letters)
    return result

def scramble_game():
    words = [w for w in english_words_lower_set if 5 <= len(w) <= 8]
    word = random.choice(words)

    scrambled = scramble(word)
    if scrambled is None:
        return
    print("Unscramble this word:", scrambled)
    attempts = 3
    while attempts > 0:
        print("Attempts left:", attempts)
        guess = input(">> ").strip().lower()
        if guess == word:
            print("Correct! The word was:", word)
            return
        attempts = attempts - 1
        print("Wrong.")

    print("Out of attempts. The word was:", word)


scramble_game()