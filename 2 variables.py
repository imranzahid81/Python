# integer

myint = 10

# float

myfloat1 = float(myint)  # casting number to float
print("My Float 1: " + str(myfloat1))

myfloat2 = 7.0
print("My Float 2: " + str(myfloat2))



# string

mystring1 = 'Hello World'  # without Escape Character String
print("My string 1: " + mystring1)

mystring2 = 'do what ever you do, do, do double, but don\'t trouble'  # with Escape Character String
print("My string 2: " + mystring2)

mystring3 = "do what ever you do, do, do double, but don\'t trouble"  # in double quotes
print("My string 3: " + mystring3)

# Assignments can be done on more than one variable "simultaneously" on the same line like this

a, b, c = 3, 4, 5
print("Printing Value of a: " + str(a))
print("Printing Value of b: " + str(b))
print("Printing Value of c: " + str(c))

# Simple operators can be executed on numbers and strings:

one = 3
two = 5
three = one + two
print("Printing Value of three: " + str(three))

hello = "hello"
world = "world"
helloworld = hello + " " + world
print("Printing string concantination: " + str(helloworld))




# Mixing operators between numbers and strings is not supported:

# This will not work!
# print one + two + hello
