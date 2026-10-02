# Task 1.1
crazyFunction = lambda x,y: x * y
meaningOfLife = crazyFunction(6, 7)
print(meaningOfLife)
## Task 1.2
animalsCounts = [['cat', 666], ['dog', 3], ['elephant', 42]]
sortedList =sorted(animalsCounts, key=lambda x: x[1])
print(sortedList)
## Task 1.3
list(filter(lambda x: x > 10, [3.14, 101, 42, 666, -1]))
### Task 1.4
[*enumerate([42, 3, 4, 18, 3, 10])]
### Task 1.5
def check_even(number):
    return number % 2 == 0

numbers = [17,2,34,4,9,6]
even_numbers = list(filter(check_even, numbers))
print(even_numbers)

### Task 1.6
words = ['apple', 'banana', 'kiwi', 'pear']
short_words = list(filter(lambda x: len(x) <= 4, words))
print(short_words)  

## Task 1.7
celsius = [-10, 0, 17.6, 28, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print("Task 1.7:", fahrenheit)
# Task 1.8
first_names = ["Jackie", "Chuck", "Arnold", "Sylvester"]
last_names = ["Stallone", "Schwarzenegger", "Norris", "Chan"]
magic = [*zip(first_names, last_names[::-1])]
print(magic[0])
print( magic[1][0])
print(magic[1][1])

# Task 1.8 (my_sum)
def my_sum(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError("all arguments must be numbers")
        total = total + arg
    print(total)

# Task 1.9 
def my_division(a, b):
    print(a // b)
    print(a % b)

my_division(42, 4)

# Task 1.10 (my_count)
def my_count(stop, start=0):
    for i in range(start, stop):
        print(i)


my_count(5)
print("---")
my_count(10, 5)

## Task 1.11 (my_count avec step)
def my_count(stop, start=0, step=1):
    for i in range(start, stop, step):
        print(i)

# Task 1.12 
def new_division(num, den, acc=1):
    print(round(num / den, acc))
# Task 1.13
# Task 1.13 (ship)
def ship(*a1, **a2): # * for tuple ** for dictionary
    print(" ".join(a1))
    for key in a2:
        print(key + ":", a2[key])


ship("Batman", street="Mountain Drive", city="Gotham")
print("---")
ship("Superman", "The man of steel", apartment="3D", num=344, street="Clinton Street", city="Metropolis")
