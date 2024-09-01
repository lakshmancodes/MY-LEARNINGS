# Functions are nothing but the pack of instructions, that perform a specific task

# First we create a function using a def keyword along with the function name.
# Here we have created just a function but didn't use it, and to use it later we pass the keyword, so that it doesn't show any error,
# while we create a empty function.
def Function():
    print("Hello World")

print(Function())

def assign():
    print("2024")
assign()

# The main use of functions is that we can reuse it many times,
'''for example if we want to print it many times and suddenly there might be changes
in the function, so instead of printing it, we can call the function as many times we want'''

# These keeps the code 'DRY' which means don't repeat yourself

assign()
assign()
assign()
assign()

# when we execute our function the return value is the result of the function, unless we print it we can't get the return value of it
def Function():
    return "Welcome"

print(Function())

# Since in the above we have returned the result as string,we can use the methods of string for the function
def Function():
    return "Welcome"

print(Function().lower())
print(Function().find('e'))

# we can pass the arguments for the function

def Function(greeting, name = "Suneel"):
    return 'Welcome {} {}.'.format(greeting, name)

print(Function("to the college.", "Sri Hari"))

'''We have know that our required postional arguments should come first than the keyword arguments
if we try to create the inorder it shows the error
when we enter the arguments we even don't know how many postional and keyword arguments might be there
(we can differentiate it using the argument creaton like for kwargs we give the keyword,but not for the position)
to check this we will be using the *args and **kwargs for the arguments
args - forms the tuple, whereas kwargs - forms the dictionary'''
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
student_info("Math", "Art", course = "Histroy", Name = "Suneel", age = 21)

