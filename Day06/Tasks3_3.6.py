# Task 3.1
print("------ Task 3.1")
print(abs(2))          
print(abs(-2))       
print(abs(-3e4))      
print(round(3.14159, 2))
print(max([-42, 3e2, 666]))  

# Task3.2
print("------ Task 3.2")

s="Beautiful is better than ugly."
print(min(s))     
print(max(s))     

# Task3.3
print("------ Task 3.3")
print(pow(73,73))


# Task 3.4
print("------ Task 3.4")
print(any([False,False,True]))   # true 
print(any([0,0,1]))              # true


# Task 3.5
print("------ Task 3.5")
L1 = [1, 2, 3, 4]
L2 = [5, 7, 9, 32]
L3 = [23, 13, 17, 14, 16, 309]
L4 = [10, 20, 30, 40]
print(sum(L1 + L2 + L3 + L4))


# Task 3.6
print("------ Task 3.6")
names = ["Joe", "William", "Jack", "Averell"]

print(sorted(names, key=len)) #short to long
print(sorted(names, key=len, reverse=True))
