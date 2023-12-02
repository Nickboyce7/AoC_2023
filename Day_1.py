# Advent of Code Challenge Day 1

#TODO: Attemping part 2. Parse string and look for keys in dictionary and see what appears first.
# Then possible parse backwards to find last element. Somehow have to reincorporate finding the digits again.

# Function for part 2
def reverse_string(s):
    return s[::-1]

# Read in the file
file = open('day1data.txt', 'r')
Lines = file.readlines()

# Create a list to hold all numbers
num_list = []

# Create a dictionary for part 2
num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
key_list = list(num_dict.keys())
# Testing find function
temp1 = []
for line in Lines[0:2]:
    temp2 = []
    for key in key_list:
        temp2.append(line.find(key))
    temp1.append(temp2)
print(temp1)

## BELOW IS FUNCTIONING SECTION FOR PART 1
# # Iterate through lines and characters. Find integers and place into numbers list
# for line in Lines:
#     temp = []
#     for char in line:
#         if char.isdigit():
#             temp.append(char)
#     num_list.append(temp)
#
# # Sum the end points of the number list
# total = 0
# for i in range(len(num_list)):
#     total = total + int((num_list[i][0] + num_list[i][-1]))
#
# print(total)