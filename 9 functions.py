# Functions

# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.

# 'def' variable for define function


def my_function():
    print("Hello From My Function!")


my_function()


# 'def' variable for define function
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function With args!, I wish you %s" %
          (username, greeting))


my_function_with_args('imran', 'hello')


# # 'def' variable for define function
def sum_two_numbers(a, b):
    return a + b


print(sum_two_numbers(2, 7))

# # calling defined function

my_function_with_args("John Doe", "a great year!")


#
x = sum_two_numbers(1, 2)
print("after add 1 + 2 = %i" % x)

# # Multiple Function Arguments

# # *therest Means rest parameters
# # The "therest" variable is a list of variables, which receives all arguments which were given to the "foo" function after the first 3 arguments.
#


def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))


# function calling
foo("x1", "x2", "x3", "y1", "y2", "y3")


# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, using the following syntax:

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print(f"the sum is: {first + second + third}")

    print(f"Print Options : {options}")

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print(f"Result: {result}")

result = bar(1, 2, 3, action=["sum", "sub", "add"], number="first")
print("Result: %d" % result)

# ************************************************************************************
# example
# edit the functions prototype and implementation


def foo(a, b, c, *args):
    return len(args)


def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")

# ************************************************************************************
# Personal Code 1 :
# ARGS :


def addition(*nums):
    return(sum(nums))


print(f"Result : {addition(2, 3, 4, 5)}")

# ************************************************************************************
# Personal Code 2 :
# KWARGS :


def get_data(**data):
    return(data)


print(f"Result : {get_data(name = 'Imran', rollNo = 10, age = 40)}")

# ************************************************************************************
# Personal Code 3 :
# FARGS, ARGS, KWARGS all in one function :
# Fargs = formal arguments


def get_data(engine, *queries, **properties):
    return(engine, queries, properties)


print(f"Result : {get_data('Google', 'Python', 'Flask', 'Django', name = 'Imran', rollNo = 10, age = 40)}")


import sys
print(f"Printing System Paths : {sys.path}")

import os
print(f"Printing Working Directory Path {os.getcwd()}")
print(f"Printing imported File (os.py) Location : {os.__file__}") 