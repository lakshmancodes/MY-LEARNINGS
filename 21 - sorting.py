'''we can sort the lists, tuples, dictionaries and even objects using the sorted thing'''
'''The main difference between the sorted function and sort method is that we need a 
new variable to store the function as it creates the new list so unless we assign it to the new variable 
we can't get the sorted version of the list,whereas the sort method directly applies to the given list'''

list = [3, 4, 7, 9, 1, 5, 8, 2, 6]
sorted(list)       # It provides us with the sorted version of the list
s_list = sorted(list, reverse=True)   # It prints the list in the ascending order as we have the function assigned to the new variable

print(s_list)

list.sort()             # It also prints the list in the ascending order, with the same variable being stored
print(list)

list.sort(reverse=True)
print(list)

'''We don't have the sort method unlike the sorted function in every iterables, but the sort method
is available in only list'''

tup = (3, 4, 7, 9, 1, 5, 8, 2, 6)
# tup.sort()            # This throws the error as we don't have the sort method in tuple
s_tup = sorted(tup)
print(s_tup)

dic = {"Name":"Suneel", "Age": 21, "Phone": 93927, "Job": "Developer"}
s_dic = sorted(dic)
print(s_dic)

# If we want to sort the elements based on the some criteria then we would like to use abes for the mixing of the +ve and -ve numbers

li_1 = [-7, -9, -3, -6, 3, 5, 7]
s_li = sorted(li_1, key=abs) # It prints the values without considering the -ve signs
print(s_li)

# If we want to alter based on the object attributes

class employee():
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.age}, {self.salary}'
    
e1 = employee("Suneel", 21, 90000)
e2 = employee("Sai", 22, 70000)
e3 = employee("Dileep", 20, 80000)

empl = [e1, e2, e3]

def e_sort(emp):
    return emp.age

s_empl = sorted(empl, key=e_sort)
print(s_empl)


# We have other option for getting the objects we can import atrrgetter

from operator import attrgetter

s_empl = sorted(empl, key=attrgetter("salary"), reverse=True)
print(s_empl)
