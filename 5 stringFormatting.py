# String Formatting
# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".
# Let's say you have a variable called "name" with your user name in it, and you would then like to print out a greeting to that user.

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# To use two or more argument specifiers, use a tuple (parentheses):

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string. For example:

# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# Note:
# Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# Multiple assignments can be done in one line :
fname = "Muhammad Imran"
lname = "Zahid"
hobby = "code"
age = 40
print("%s %s is %d years old and loves to %s." % (fname, lname, age, hobby))

# Other way of Concatenation :
###   Method 1   ###
greeting = "Hello"
name = "Imran"
message = "{}, {}. Welcome!".format(greeting, name)
print(message)

###   Method 2   ###   ###   f String   Latest Method   ###
greeting = "Hello"
name = "Zahid"
message = f"{greeting}, {name.upper()}. Welcome!"
print(message)

# To check methods available to variable
fname = "Muhammad"
print(dir(fname))
