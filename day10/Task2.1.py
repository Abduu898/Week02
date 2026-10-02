# Task 2.1
def read_file(filename):
    with open(filename, "r") as f:
        content = f.read()
        print(content)


read_file("primes.txt")

# Task 2.2
def read_line(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

read_line("zen.txt")

# Task 2.3
def read_lines(*lines):
    with open("primes.txt","r") as f:
        all_lines = f.readlines()
    for n in lines:
        if n < 1 or n > len(all_lines):
            raise ValueError("line " + str(n) + " does not exist")
        print(all_lines[n - 1].strip())

read_lines(666)
# Task 2.4
def count_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    print(len(lines))
# Task 2.5
def create_file():
    with open("toto.txt", "w") as f:
        pass
create_file()

# Task 2.6
def write():
    with open("toto.txt", "a") as f:
        f.write("I'm a new line\n")


write()

# Task 2.7
def rewrite():
    with open("zen.txt", "r") as f:
        content = f.read()
    with open("toto.txt", "w") as f:
        f.write(content)


rewrite()

## Task 2.8
def longest():
    with open("zen.txt", "r") as f:
        content =f.read()
    words =content.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)


longest()

# Task 2.9
def word_frequency():
    with open("zen.txt", "r") as f:
        content = f.read()
    words = content.split()
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 0
        frequency[word] = frequency[word] + 1
    for word in frequency:
        print(word, ":", frequency[word])
# Task 2.10
def letter_frequency():
    with open("zen.txt", "r") as f:
        content = f.read()
    content = content.lower()
    frequency = {}
    for letter in content:
        if letter.isalpha():
            if letter not in frequency:
                frequency[letter] = 0
            frequency[letter] = frequency[letter] + 1
    for letter in frequency:
        print(letter, ":", frequency[letter])


letter_frequency()