'''we know on how to do the slicing for the lists and strings
'''

fruits = ["Apple", "Banana", "Cherry", "Guava", "JackFruit", "Mango", "Orange"]

print(fruits)
print(fruits[0:])       # It prints the all the elements of the list staring from the index 0 
print(fruits[:6])       # it prints the elements from the index 0 to index 5,where the last elemnst is exclusive
print(fruits[2:7])
print(fruits[-1])       # it prints the last element of the list
print(fruits[-5:-3])    # We can write it in the -ve numbers of the index were they start from last.

'''we have three things in the slicing of list[start:end:step]'''

print(fruits[2::2])     # It prints from the 2nd element to the last by skipping the every one element
print(fruits[-1::-1])   # It prints the entire list in the reverse order because the start value is -1 from last
print(fruits[-3:-7:-2]) # It prints from the last 3rd element and goes till the -ve element and prints the every 2nd element
print(fruits[:8:3])     # It prints from the starting till 7th index by printing every 3rd element

''''The same things apply for the string too'''