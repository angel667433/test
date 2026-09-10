# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']
print("Here are the top Sega games:")
for game in g_list:
    print(game)
g_list.remove(input("Which one do you think should be removed? "))
print("Here are the new top Sega games:")
for game in g_list:
    print(game)