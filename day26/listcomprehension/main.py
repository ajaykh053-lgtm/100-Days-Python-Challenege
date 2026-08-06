# List Comprehension
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_n = n + 1
    new_list.append(add_n)
print(new_list)
# Using List comprehension
new_item = [n + 1 for n in numbers]
print(new_item)
# List comprehension used for String
Name = "Latha BN"
name = [letter for letter in Name]
print(name)
# List comprehension for Doubling the number
range_list = [i * 2 for i in range(1, 5)]
print(range_list)

names = ["Natalie","Liam","Sebastian","Zoe","Ivan", "Dominic"]
short_name=[name for name in names if len(name)<5]
print(short_name)
Long_names=[name.upper() for name in names if len(name)>5]
print(Long_names)

# Squaring Numbers
# You are going to write a List Comprehension 
# to create a new list called squared_numbers. 
# This new list should contain every number in 
# the list numbers but each number should be squared. 
# e.g.
# 4 * 4 = 16
# 4 squared equals 16.
# **DO NOT** modify the List numbers directly.
#  Try to use List Comprehension instead of a Loop. 
# Target Output 
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025] 

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

# Filtering Even Numbers
# In this list comprehension exercise you will practice 
# using list comprehension to filter out the even numbers from a series of numbers.   
# First, use list comprehension to convert the list_of_strings
#  to a list of integers called numbers.   
# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers. 
# Again, try to use Python's List Comprehension instead of a Loop. 

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string) for string in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)


# Data Overlap
# 💪 This exercise is HARD 💪 
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
# You are going to create a list called result which contains the numbers that are common in both files. 
# e.g. if file1.txt contained: 
# 1 
# 2 
# 3
# and file2.txt contained: 
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop. 

with open("day26/file1.txt") as file1:
   nums1= file1.readlines()
   print(nums1)
with open("day26/file2.txt") as file2:
   nums2 = file2.readlines()
   print(nums2)
result = [int(num1) for num1 in nums1 for num2 in nums2 if num1==num2]
print(result)