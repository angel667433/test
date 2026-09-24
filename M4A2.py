# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 4 Assignment 2

food_dict = {}

for i in range(3):
    food = input("What is good to eat? ")
    country = input("What country is that from? ")
    food_dict[food] = country

dish = input("What dish do you like? ")
print(f"{dish.title()} is from {food_dict[dish]}")