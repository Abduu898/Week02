def find_longest_word(words):
    longest = words[0]
    for w in words:
        if len(w)>len(longest):
            longest=w
    return longest

print(find_longest_word(["apple","banana","cherry","kiwi"]))
