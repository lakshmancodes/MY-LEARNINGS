'''for example we have to use the particular function in this module so that
which is present in the other file, so we can import it using the import one so 
it runs all the ones from were we took it'''

'''We can also import like from the particluar file we can import the required method'''
# import my_module as mm 
# from my_module import find_index

import my_module as mm           # it imports all the variables, constants, functions from the my_module
#from my_module import find_index   # it imports only the find_index function from the my_module 

courses = ["History", "Art", "Science", "Maths", "English"]

index = mm.find_index(courses, "Maths")
print(index)
print(mm.test)

import sys              # it checks multiple locations where the file are being stored with respect to the lsit called "sys"
print(sys.path)         # it prints the file paths where it all checks for the imported file

'''The above importing the file only works if the two scripts are in the same location
if we want to import the file from different location, then we can manually add the path of the file
synatx - import sys
         sys.path.append(location of the file which we want to import)'''
# this doesn't work write because the environment variables are different

import random

rand = random.choice(courses)
print(rand)

import math

rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar

# to print today's date

today_date = datetime.date.today()
print(today_date)

leap_year = calendar.isleap(2019)
print(leap_year)

import os           # it gives us the access to the underlying operating system
print(os.getcwd())  # it prints out the current directory in which we are working on.
print(os.__file__)  # it prints out the location of os file in our system

import antigravity


