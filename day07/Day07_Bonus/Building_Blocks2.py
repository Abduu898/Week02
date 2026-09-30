def frequency(word):
    result ={}
    for ch in word:
        if ch in result:
            result[ch] = result[ch] + 1
        else:
            result[ch] = 1
    return result

def most_frequent(word):
    freq = frequency(word)
    best_letter = ""
    best_count = 0

    for ch in freq:
        count = freq[ch]
        if count > best_count:
            best_count = count
            best_letter = ch

    return best_letter

print(frequency("banana"))