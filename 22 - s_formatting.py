# Creating a string formatting using the list and dictionaries

student = {"name":"Suneel", "Age": 21, "State":"AP"}

student_info = "My name is {}. I am {} years old. I am from {}.".format(student["name"], student["Age"], student["State"])
print(student_info)

student_info = f'My name is {student["name"]}. I am {student["Age"]} years old. I am from {student["State"]}'
print(student_info)

student_info = "My name is {0[name]}. I am {0[Age]} years old. I am from {0[State]}.".format(student)
print(student_info)

tag = "h1"
text = "welcome"

sentence = "<{0}>{1}</{0}>".format(tag, text)
print(sentence)

student_info = "My name is {name}. I am {Age} years old. I am from {State}.".format(**student)
print(student_info)

for i in range(11):
    print("The value is {:02}".format(i))


pi = 3.141536278

print("{:.2f}".format(pi))

print("the value of 1 MB is {:,.2f}".format(1000**2))




#DATE FORMATTING

import datetime

my_required_date = datetime.datetime(2024, 12, 21, 11, 13, 53)
print(my_required_date)

my_date = "{:%B %d, %Y}".format(my_required_date)
print(my_date)

my_expand = "Today is {0:%B %d, %Y} and it fell on {0:%A} and on {0:%j} of the day year".format(my_required_date)
print(my_expand)