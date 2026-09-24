# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 4 Assignment 5

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
             }
for people, food in food_dict.items():
    if food == '':
        food_dict[people] = input(f"What is {people}'s favorite food? ")
print("Here are the favorite foods:")
for people, food in food_dict.items():
    print(f"{people}'s favorite food is {food}")