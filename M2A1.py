# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 2 Assignment 1

g_list = []
g_list.append(input("What is your favorite game? "))
g_list.append(input("What is your second favorite game? "))
g_list.append(input("What is your third favorite game? "))
message_str = g_list.pop()
print(f"One of your favorite games is {message_str.title()}")
message_str = g_list.pop()
print(f"One of your favorite games is {message_str.title()}")
message_str = g_list.pop()
print(f"One of your favorite games is {message_str.title()}")