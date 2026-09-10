# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 2 Assignment 3

uber_list = list(range(100,201,2))
start = int(input("What is the start of your slice? "))
end = int(input("What is the end of your slice? "))
data_list = uber_list[start : end]

total_int = 0

for number in data_list:
    total_int += number
average = total_int/len(data_list)
print(f"Your slice contains {len(data_list)} values and has an average value of {average}")