# Task 1.2
print("------ Task 1.2")
def reverse_string(text):
    if text == "":
        return ""
    return reverse_string(text[1:])+ text[0] 
print(reverse_string("Epitech"))   