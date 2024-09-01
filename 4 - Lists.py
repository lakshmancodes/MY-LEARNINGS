#Lists
# Lists are mutable i.e they are prone to changes to the given list

fruits = ['Banana', 'Mango', 'Apple', 'Grapes','Watermelon']
print(fruits)

sorted(fruits)                      # it is mainly used for the purpose of storing the original data
new_fruits = sorted(fruits)     
print(new_fruits)


# to get the length we use "len" 

print(len(fruits))


# to get the index of the list items use "[]"
print(fruits[0])
print(fruits[1:])
print(fruits[1:4])
print(fruits[:2])
print(fruits[-2])
print(fruits[2:-1])


# MODIFYING THE LISTS

# to add the item to the previous list we use the "append", "insert","extend" methods

fruits.append('Papaya')        # we use the append method  just to add the item at the last to the list
print(fruits) 

fruits.insert(3, 'Straw Berry') # we use the insert method to add the item to the specific loaction to the list
print(fruits)

fruits_2 = ['Musk Melon', 'Dragon Fruit']
#fruits.insert(0, fruits_2)     # it insert the items to the list as it is to the current list without removing the brackets
#print(fruits)

fruits.extend(fruits_2)         # we adds the items to the list as a whole to the current list that the item are actually belongs to it
print(fruits)


# REMOVING FROM THE LISTS
# to remove from the lists we use the "remove" and "pop" methods

fruits.remove('Grapes')         # it removes the item which is being mentioned in the method 
print(fruits)

fruits.pop()                    # it removes the last item of the list, so it mainly uses for the stack and queue operations
print(fruits)

# CONCEPT OF ORDERING THE LISTS
# to reverse the list we use the "reverse" method 

fruits.reverse()
print(fruits)

fruits.sort()                   # it prints the list in the ascending order
print(fruits)

fruits.sort(reverse=True)       # it prints the list in the descending order or lower alphabetic order
print(fruits)

print(fruits.index("Apple"))    # provides the index of the Fruit if present in the list
print('Grapes' in fruits)       # returns the boolean value according to the item in the list

fruits_3 = ' - '.join(fruits)    # it prints the values as string with commas as represented
print(fruits_3)

fruits_3 = fruits_3.split(' - ')
print(fruits_3)

# creation of the empty list
'''empty_list = []
empty_list = list()'''



#TUPLE
# tuples are immutable
# we can't change the value of the tuple once it is being created, but we can add the values to the tuple
# tuples can be used for heterogenous datatypes

tuple_1 = ('Banana', 'Mango', 'Apple', 'Grapes','Watermelon')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

'''tuple_1[1] = "Dragon Fruit" # it doesn't support item assignment
print(tuple_1)'''


# Tuple can be created without parentheses, this is called tuple unpacking
tuple_3 = 101, "Suneel", 90000, "CSE"
print(tuple_3)

# we can't delete particular item of the tuple, but we can delete the entire tuple
del tuple_3


# creation of the empty tuple
'''empty_tuple = ()
empty_tuple = tuple()'''





# SETS

#Sets doesn't care about the order, they only provide us about the ,whether the item present in the set or not.
# Sets remove the duplicates

cs_courses = {"S/w", "H/w", "Project" }
print(cs_courses)

art_courses = {"S/w", "H/w", "Design","Art"}
print(art_courses)
print(cs_courses.intersection(art_courses)) # it prints the values which are present in both the sets
print(cs_courses.difference(art_courses))   # it prints the values which are not present in the art_courses but present in the cs_courses
print(cs_courses.union(art_courses))        # it prints the combination of both the values
 
 
# sets cannot have mutable items
'''set_1 = {1, 2, 3, [4, 5, 6] }
print(set_1)'''

# we can set from a list and also list from set
set_2 = set([1, 2, 3, 4])
print(set_2)
set_3 = list({11, 22, 33, 44})
print(set_3)
# to add a single element to the set we can use add method to the set
art_courses.add("program")
print(art_courses)

# to add multiple elements to the set we can use update method for the set,but we have enter the elements in the form of list only 
cs_courses.update(["Security", "Audit"])
print(cs_courses)

# to delete the elements we can use remove and discard methods, where the discard handles the errors, but the remove doesn't
'''cs_courses.discard("program")
print(cs_courses)

cs_courses.remove("program")
print(cs_courses)'''

art_courses.remove("program")
print(art_courses)

art_courses.discard("program")
print(art_courses)

# Frozensets are nothing but the immutable sets, i.e once they are created they can't be changed,but they can be delted
 
'''# Creation of Empty Set
empty_set = {} # this isn't a empty set.Actually, this creates a empty dictionary
empty_set = set() # this creates a empty set.''' 