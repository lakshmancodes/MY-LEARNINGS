# LIST COMPREHENSION
# List comprehension is more easier way to create a list and also to read

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want to print n for each n in nums

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = [n for n in nums]     # These is the list comprehension
print(my_list)



my_list1 = []
for n in nums:
    my_list1.append(n**2)
print(my_list1)
my_list1 = [n**2 for n in nums] # These is the list comprehesion
print(my_list1)

my_list2 = []

for n in nums:
    if n%2 ==0:
        my_list2.append(n**2)
print(my_list2)

my_list2 = [n for n in nums if n%2 == 0]
print(my_list2)


list_1 = []
for letter in "ABCD":
    for n in nums[:6]:
        list_1.append((letter, n))
print(list_1)

list_1 = [(letter, n) for n in nums[:3] for letter in "ABCD"]
print(list_1)


# DICTIONARY COMPREHENSIONS

f_name = ["Suneel", "Sai", "Hari"]
l_name = ["Kumar", "Deepak", "Babu"]

#print(zip[f_name, l_name])

my_dic = {}

for f, l in zip(f_name, l_name):
    if f != "Sai":
        my_dic[f] = l
    
print(my_dic)


my_dic1 = {f:l for f, l in zip(f_name, l_name)}     # Dictionary Comprehension
print(my_dic1)



# SETS COMPREHENSION

numbers= [1, 2, 2, 1, 3, 6, 5,8, 4, 6, 3, 9, 6, 7, 8, 5, 4, 7, 8, 1]

my_set = set()

for i in numbers:
    my_set.add(i)
print(my_set)

my_set = {i for i in numbers}       # Set Comprehension
print(my_set)



# GENERATOR EXPRESSIONS

def generator(nums):
    for i in nums:
        yield i*i

my_gen = generator(nums)

for j in my_gen:
    print(j)
    
my_gen = (k**3 for k in nums)

for k in my_gen:
    print(k)
        
    
    


