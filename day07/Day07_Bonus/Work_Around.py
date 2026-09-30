#### Task 1.1 
print("-----Task 1.1-----")
def count_types(text):
    vowels = 0
    consonants = 0
    for ch in text:
        if not ch.isalpha():
            continue
        ch = ch.lower()
        if ch in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    print(vowels,"vowels,", consonants,"consonants")
    count_types("Hello World!")

#### Task 1.2 
print("-----Task 1.2-----")

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
print(is_palindrome("Kayak"))     

#### Task 1.3 
print("-----Task 1.3-----")
def is_anagram(word1, word2):
    word1 =word1.lower()
    word2 =word2.lower()
    return sorted(word1) == sorted(word2)
print(is_anagram("listen","silent"))   
print(is_anagram("hello","world")) 

