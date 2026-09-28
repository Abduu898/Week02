def sum_recu(n):
    if n==0:
        return 0
    result=0
    return n + sum_recu(n - 1)


print(f"{sum_recu(42)}")

### Task 2.2
print("------ Task 2.2")
## def palindrom(phrase):

 ##   new=""
  ##  for c in phrase:
   ##     if c.isalpha():
   ##         new+=c.lower()
        
        

  ##  if new==new[::-1]:
  ##      print("Its an palindrom")
 ##   else: print("Its not an palindrom")



def clean(s,i=0):
    if i>=len(s):
        return ""
    c= s[i]
    if c.isalpha():
        return c.lower() + clean(s,i+1)
    return clean(s,i+1)

def check(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return check(s[1:-1])


def is_palindrom(s):
    return check(clean(s))

s1="never odd or even"
s2="A Santa Lived As a Devil at NASA"

print(is_palindrom(s1))
print(is_palindrom(s2))