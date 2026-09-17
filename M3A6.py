# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 3 Assignment 6

name = input("What is the student name? ")
score = int(input("What is their score? "))

if score >= 90:
    print(f"{name} earned an A")
elif score < 90 and score >= 80:
    print(f"{name} earned a B")
elif score < 80 and score >= 70:
    print(f"{name} earned a C")
elif score < 70 and score >= 60:
    print(f"{name} earned a D")
else:
    print(f"{name} earned an F")
