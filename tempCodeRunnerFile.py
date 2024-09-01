
from multiprocessing import Value


student = {"Name":"Suneel", "Age": 21, "Address":"Gudur"} # it is the representation of the dictionary, where we declare it in key,value pairs
print(student)

# to get the particular value of the key we used to place the key in the square brackets of the defined dictionary in the print statement
print(student["Name"])

# instead of declaring the strings as key to the vlaues we can declare any things like numbers, integers etc.
art = {1 : "Kumar", 2: 22}
print(art)

'''if we want to get the key that doesn't exist, then it throws key error
    to resolve this we can use the get method were it returns the value as "none" if the key doesn't exist in the dictionary
    we can also get this using the get method'''

#print(student["phone"])
print(student.get("Address", "Not Found"))
print(student.get("Phone", "Not Found"))