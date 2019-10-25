# Basic Operators

# Arithmetic Operators

# Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

number = 1 + 2 * 3 / 4.0
print('Print Number: ' + str(number))

remainder = 11 % 3
print('Print Remainder: ' + str(remainder))

squared = 7 ** 2
print('Print Squared: ' + str(squared))

cubed = 2 ** 3
print('Print Cubed: ' + str(cubed))

# Operators with Strings

# Python supports concatenating strings using the addition operator:
helloworld = "hello" + " " + "world"
print('Printing HelloWorld with Space: ' + str(helloworld))




# Python also supports multiplying strings to form a string with a repeating sequence:
lotsofhellos = "hello " * 10
print('Print Hello 10 times: ' + str(lotsofhellos))




# Operators with Lists
# Lists can be joined with the addition operators:

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print('Combined List of Even and Odd Numbers: ' + str(all_numbers))
all_numbers.sort()
print('Sorted List Alphabetically: ' + str(all_numbers))




# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:

print("Printing List in repeating sequence: " + str([1, 2, 3] * 3))
