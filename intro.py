"""
    First task: print strings
"""
# print("Hi, I'm Peyton")
# print("I'm 16 years old")
# print("My favorite food is pizza")


"""
    Second task: use input from terminal
        --Explain types and how Python infers types
"""
print("What is your name?:")
name = input()
print("How old are you?:")
age = int(input())
print("What is your favorite food")
food = str(input())
print(
    f"You are {name} and you are {age} years old.\nYour favorite food is {food}"
)