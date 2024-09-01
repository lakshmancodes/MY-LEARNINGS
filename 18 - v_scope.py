'''We have LEGB which means local, enclosing, global, built-in
were the python takes in the order of LEGB while checking the varaibles in the written code'''

'''we know that the difference between the local and global variables where we can 
acces the global variables any where in the code unlike the local variables'''

x = "This is the global variable"
print(x)

def test():
    y = "This is the local variable"
    print(y)                        # it prints the local variable
    
test()
#print(y)      # this shows the error because, since the y is the local variable, we can't print it in the outside the function

def test1():
    x = "This is the local variable"
    print(x)    # This prints the things which are being mentioned in the function named test1
test()

def test2():
    global x
    x = "this is the main thing"
test2()
print(x)# This prints above x, because we have updated it in the function by making it as a global and calling it in the main method

'''we can declare the golbal variable any where in the code not like the local variable'''

# There are many bulit-ins available for the variables where we can use it 
# To get the bulit-ins which are available we can import the bulit-in and print it using the dir 

import builtins

print(dir(builtins))

''''if we declare the same function name and the bulit-in variable it throws the error'''
def min1():
    pass

my_min = min([2, 6, 8, 3, 5])

print(my_min)


# ENCLOSING the variables

def outer():
    x = "Outer X"
    
    def inner():
        #nonlocal x
        x = "inner X"
        print(x)
        
    inner()
    print(x)
outer()


