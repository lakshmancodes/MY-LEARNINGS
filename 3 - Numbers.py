# type of the datatype

from fractions import Fraction


num_1 = 10

print(type(10))




# Arthimetic operators

num_2 = 27

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2) # gives the quotient of the division
print(num_1 % num_2) # gives the remainder of the divsion (modulus)
print(num_2 // num_1) # gives the whole number of the quotient (floor division)
print(2 ** 4) # gives the power of the first number to the second number (exponent)

# it automatically follows the BODMAS rule in the program

print(2 * 12 + 2 * 4)
print(2 * (12 + 2) * 4)

#using the bulit function of "abs" to convert the negative number to the positive

print(abs(-22.3))

# using the built function of the "round" we can round off to the nearest integer of the value

print(round(18.51235, 3))


# Comparison of the numbers

print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

# conversion of string to the numbers

num_1 = '23'
num_2 = '27'

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)

# to check the correct type of the datatype of the varaiable used we use "isinstance"

print(isinstance(num_1,float))

# to convert the numbers from differnt types to the decimal we use these things

num_1 = 0b11011
num_2 = 0xA
num_3 = 0o20
print(num_1, num_2, num_3)

# python fractions 

num_1 = 0.12
num_2 = 0.442
print(num_1 + num_2)
print(Fraction(1.5))

#math functions

import math
print(math.pi)
print(math.cos(45))
print(math.log10(10))

