# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 3 Assignment 3

current = int(input("What year is it now? "))
born = int(input("What year were you born? "))
age_int = current - born

if (age_int % 2) == 0 and age_int < 50:
    print("This will be a great year")
elif (age_int % 2) != 0 and age_int < 50:
    print("This year wil be tough")
elif age_int == 50:
    print("The future is unclear")
else:
    print("Death will come for you soon")
