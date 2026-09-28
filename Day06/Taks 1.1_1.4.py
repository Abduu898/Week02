###### Task 1.1
print("-----------Task 1.1")
def f1():
    return 42
def f2(x):
    return 2 * x
print(f1(), f2(5) + f1())

###### Task 1.2
print("-----------Task 1.2")
def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato():
    print("O O O O O O")
def ham():
    print("============")
bread()
lettuce()
tomato()
ham()
ham()
bread()

###### Task 1.3
print("-----------Task 1.3")

def sandwich(j):
    if not isinstance(j,int) or j<=0:
        print("I can't do this!")
    else:
        for i in range(j):
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()
            print() 

sandwich(2)
######## Task 1.4
print("---------- Task 1.4")
def sandwich_2(j, veg=False):
    if not isinstance(j,int) or j<=0:
        print("I can't do this")
        return
    for i in range(j):
        bread()
        lettuce()
        tomato()
        if veg:                
            lettuce()          
            tomato()
        else:
            ham()              
            ham()
        bread()
        print()

sandwich_2(1,True)



