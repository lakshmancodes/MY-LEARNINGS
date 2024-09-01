# Conditionals are nothing but the checking of the values for the given variables.
# There are no switch-case statements,as the conditionals are much enough to deal these things

language = "Python"

if language == "Python":
    print("The Language we are studying is Python")
elif language == "Java":
    print("The Language we are studying is Java")
else:
    print("The Language we are studying is JavaScript")
    
    
age = int(input("Enter the age:"))

if age < 5 :
    print("You are too young")
elif ((age >= 5) and (age < 20)):
    print("You can go to School")
else:
    print("Go to College")

    
# Now we will see the boolean operations like not, or, not.
user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Welocme to the Site")
else:
    print("invalid credentials")
    
# Or operation
user = "Admin"
logged_in = False

if user == "Admin" or logged_in:
    print("Welocme to the Site")
else:
    print("invalid credentials") 
    
# not operation is nothing but the negotiation,like if we write true it returns false and vice-versa
logged_in = True
if not logged_in:
    print("Welcome")
else:
    print("Try Again")
    
'''Comparisons
Equal : ==
Not Equal : !=
Greater Than  : >
Less Than  : <
Greater Than or Equal to : >=
Less Than or Equal to : <=
object identity : is'''

# Now let's see the difference between the  to and object identity
#To test the two objects of same identity which means that the are in same memory
# So equal means two objects are equal but not in memory
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)


# Now let's see the when the false values arises during the use of conditonals
# if the condition is false, then it returns false
student = False
if student:
    print("Evaluation isTrue")
else:
    print("Evaluation is False") 
 
   
# if the condition is none, then it returns false
student = None
if student:
    print("Evaluation isTrue")
else:
    print("Evaluation is False")

   
# if the condition is zero of any numeric type, then it returns false
student = 0
if student:
    print("Evaluation isTrue")
else:
    print("Evaluation is False")

# if the condition is of any empty sequence like "", (), [], {}, then it returns false

student = []
if student:
    print("Evaluation isTrue")
else:
    print("Evaluation is False")
    
    
# Creation of nested if loop

num = int(input("Enter the number:"))

if num >= 0:
    if num == 0:
        print("The number is Zero")
    else:
        print("The number is +ve")
else:
    print("The number is -ve")    
