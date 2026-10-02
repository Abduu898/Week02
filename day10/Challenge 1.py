from num2words import num2words
def count_letters(N):
    total = 0
    for i in range(1, N + 1):
        word = num2words(i)
        word = word.replace(" ", "").replace("-", "")        # Enlever les espaces et tirets

        total = total + len(word)
    return total
