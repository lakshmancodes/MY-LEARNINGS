# we will be seeing the loops, mainly of for and while loop
#First we will create a list and to loop through the list we will be using the for loop

courses = ["Art", "Maths", "Science", "English"]
for i in courses:           # here we have created a variable i, where we loop through each value of the list
    print(i)

# Now let's see two important keywords when we are using the loops. They are the break and continue
# The BREAK keyword completely break the loop, where as the continue keyword moves to the next iteration

for i in courses:
    if i == "Science":
        print("Found the required the course")
        break
    print(i)
    
for i in courses:
    if i == "Science":
        print("Found the required the course")
        continue
    print(i)


# Now let's see the nested loops

language = "Telugu"
for i in courses:           # here first it reads the art and then moves to the next loop
    for j in language[0]:   # Now it reads the each element of for loop of the language until it reaches the end of string 
        print(i, j)
        
# to loop through for a particular time the we use the range method to print the elements for a particular range
for i in range(12):
    print(i)            # we can it prints from 0 to 11

#if we want to print from 1 we give the start value and increment the range by 1, because the range is exclusive for 12
for i in range(1, 13,2):  # for i in range(start value, end value, increment)
    print(i)            # here it prints from 1 to 12
    
    
    
'''WHILE LOOP'''
# The main us eof while loop is that it loops through until a certain condition is met., where as for loop is for certain values

x = 2
while x <= 10:          # checkc the condition whether it is false or True
    print(x)            # It rpints the values until the condition is True and then it break itself
    x += 1              # it increments the value by 1
    
# The same use of the break keyword in the while loop also
x = 0
while x <= 6:
    if x == 3:
        break         
    print(x)            
    x += 1   


# To create a infinite loop, we should give True in the place of conditon, and to stop the infinite loop, we press the ctrl+c
x = 0
while True:        
    print(x)            
    x += 1
