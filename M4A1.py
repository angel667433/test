# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 4 Assignment 1

g_list = []
g_list.append(input("What is your number 1 favorite PlayStation game? "))
g_list.append(input("What is your number 2 favorite PlayStation game? "))
g_list.append(input("What is your number 3 favorite PlayStation game? "))

for num, game in enumerate(g_list,  start= 1):
    print(f"Your number {num} favorite game was {game}")
