# Dictionaries are nothing but the hashmaps or associative arrays, where we deal with key-value pairs.
# Where the key is the unique indentifier and we store the data in that key.
# Dictionaries are mutuable, consits of heterogenous datatypes where it may contain int, string, list etc.


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

# to add the key-value pair or update it, we can do this using the following
student["State"] = "AP"
student["Address"] = "Nellore"
print(student)

# to add the multiple key-value pairs or update the present values we can use the update method
student.update({"Name": "Kumar", "Phone": "342436"})
print(student)

# to delete the key-value pairs we can use the del or pop method
del student["State"]
Age = student.pop("Age")
print(student)
print(Age)

# we can delete the entire dictionary elements using the clear method
art.clear()
print(art)

# to get the length of the dictionary we use the length method
print(len(student))

# to get only the keys of the dictionary
print(student.keys())

#to get the vlaues of the dictionary
print(student.values())

# to get the whole dictionary along with the keys and values we use the items
print(student.items())

# to loop through the whole dictionary, we can't get only the key because we use the items method were we use it only in the dictionary.
for key, value in student.items():
    print(key, value)

# we can also create a new dictionary using comprehension
square = {X : X*X for X in range(5)}
print(square)

# memebership test is for the key only not value
print(2 in square)
print(7 in square)

