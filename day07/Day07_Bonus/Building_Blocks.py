#### Task 2.1
import random
print("----- Task2.1")
from english_words import english_words_lower_set
WORDS = list(english_words_lower_set)
def words_of_length(words, n):
    result = []
    for w in words:
        if len(w) == n:
            result.append(w)
    return result


def only_letters(words):
    result = []
    for w in words:
        if w.isalpha():
            result.append(w)
    return result


def group_by_length(words):
    result = {}
    for w in words:  
        n =len(w)
        if n in result:
            result[n].append(w)
        else:                         ### KEy Value -><-
            result[n] = [w]
    return result


n = int(input("Word length: "))
candidates = words_of_length(only_letters(WORDS), n)

if candidates:
    print("Random word:", random.choice(candidates))
else:
    print("No word of that length.")