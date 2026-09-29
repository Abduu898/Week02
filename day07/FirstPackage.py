from english_words import english_words_lower_set
import random

def random_word():
    words = list(english_words_lower_set)
    return random.choice(words)

print(random_word())
