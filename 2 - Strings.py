'''# entering the input of the message
my_message = ("Hello World")
print(my_message)'''



#working with the single qoutations in the sentence
my_message = ("Welcome to my world's of experience")
print(my_message)

# We can also use the whole single quotes but instead we have to use the back slash infront of the apostrophe.
my_message = ('Welcome to my world\'s of experience')
print(my_message)

# We can use the triple double quotes to print the sentences in the new line
my_party = '" welcome you to my party.I also would like u to have the dinner."'
print(my_party)

# workin with the index and length of the string
my_message = "Hello World"
print(len(my_message))

#print(type(my_message))
print(my_message[8])
print(my_message[3:9])
print(my_message[:4])
print(my_message[2:])
print(my_message.lower()) # used to convert to lower case letters
print(my_message.upper()) # used to convert to upper case letters
print(my_message.count('l')) #used to count the number of times it have occured in the given sentence
print(my_message.find('e'))  #used to find the index of the word or letter
print(my_message.swapcase())
new_message = my_message.replace("Hello", "Welcome to the") # used to replace a word 
print(new_message)
lak=("Lakshman is the greatest of all")
laksh= "Lakshman is the goat "
print(lak)
lak.replace("Lakshman","Praveen")
laksh.replace("goat","GOAT")

# String concatenation

message = "Hello"
name = "Suneel"

Sentence = message + name
print(Sentence)

Sentence = message + ' ' + name
print(Sentence)

Sentence = '{}, {}. Welcome to the world '.format(message, name)
print(Sentence)

Sentence = f'{message}, {name.upper()}. Welcome to the world'
print(Sentence)
Sentence = '{} {} {}'.format("Today","is a","Holiday")
print(Sentence)
Sentence = '{0} {1} {2}'.format("Today","is a","Holiday")
print(Sentence)
Sentence = '{1} {2} {0}'.format("Today","is a","Holiday")
print(Sentence)
Sentence = '{t} {i} {h}'.format(t = "Today",i = "is a",h = "Holiday")
print(Sentence)

#  count the no. of chars in a string
asdd="sdajisebfjiwdfnjkewwpwiqllejfwdml"
letter_count = 0
for letters in asdd:
    if(letters == 'l'):
        letter_count += 1
print(letter_count)

# using the bulit - in function (enumerate)

my_list_enumerate = list(enumerate(Sentence))
print(my_list_enumerate)

# formatting the numbers and folat values

num1 = 12
num2 = 16

print("The binary representation of {0} is {0:b} and {1} is {1:b}".format(num1, num2))

print("The division of the two numbers of upto 3 decimal values is {0:.3f}".format(num2/num1))


ab="Lakshman"
bc="Food"
print(ab)
abc='{} loves to eat {}'.format(ab,bc)
print(abc)
c='{2} I am {1} to this {0}'.format("Me","new","Field")
print(c)


let=0
letter="aaabbbdddsbbfbwjrkeowpsd"
a=input("enter the letter you want to find :")
for i in letter :
    if(a==i):
        let+=1
print('the letter',a,'occured',let,'times')

enu=list(enumerate(letter))
print(enu)

print("""to get the binary value representation of {0} is {0:b} 
      this is the second number to get binary {1} is {1:b}""".format(10,20))