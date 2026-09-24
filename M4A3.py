# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 4 Assignment 3

games_dict = {}

for i in range(3):
    game = input("What is a great game? ")
    system = input("What system can I play that on? ")
    games_dict[game] = system

print("That's too many, let's get rid of one")
rgame = input("What game should we remove? ")
del games_dict[rgame]
print("The new dictionary is:")
for game, system in games_dict.items():
    print(f"You can play {game} on {system}")