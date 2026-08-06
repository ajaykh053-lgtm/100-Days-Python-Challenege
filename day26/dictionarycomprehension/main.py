# Dictionary Comprehension
# new_dict={new_key:new_vlaue for item in list or string}

# Dictionary Comprehension using exsisting dictionary
# new_dict={new_key:new_vlaue for (kay:value) in .dictitems() }

# A further step is adding condition to it
# new_dict={new_key:new_vlaue for (kay:value) in .dictitems() if test }


import random

name = ["Natalie", "Liam", "Sebastian", "Zoe", "Ivan", "Dominic"]
student_score = {students: random.randint(1, 100) for students in name}
print(student_score)
passed_student = {
    student: score for (student, score) in student_score.items() if score >= 60
}
print(passed_student)

# Dictionary Comprehension 1
# You are going to use Dictionary Comprehension to create
# a dictionary called result that takes each word in
# the given sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.  *
# *Do NOT** Create a dictionary directly.
# Try to use Dictionary Comprehension instead of a Loop.
# To keep this exercise simple, count any punctuation following
# a word with no whitespace as part of the word. Note that "Swallow?"
#  therefore has a length of 8


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
lists = sentence.split()
result = {word: len(word) for word in lists}
print(result)

# Dictionary Comprehension 2
# You are going to use Dictionary Comprehension to create
# a dictionary called weather_f that takes
# each temperature in degrees Celsius and
# converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {week: (temp_c * 9 / 5 + 32) for (week, temp_c) in weather_c.items()}
print(weather_f)


student_dict = {"Student": ["Angela", "James", "Lily"], "Score": [56, 76, 98]}
# Looping thorugh dictionary
for key, value in student_dict.items():
    print(key)
    print("\n")
    print(value)
    print("\n")
    print(f"{key} : {value}")
    print("\n")

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for key, value in student_data_frame.items():
    print(key)
    print("\n")
    print(value)
    print("\n")
    print(f"{key} : {value}")
    print("\n")

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.Student)
    print(row.Score)
    if (row.Student=="Angela"):
        print(row.Score)
