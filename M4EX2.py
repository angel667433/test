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
popular = {}
for people, food in food_dict.items():
    print(f"{people}'s favorite food is {food}")
    if food in popular:
        popular[food] += 1
    else:
        popular[food] = 1
highestnum = 0
popfood = ''
for food, count in popular.items():
    if count > highestnum:
        popfood = food
        highestnum = count
print(f"The most popular food is {popfood}")