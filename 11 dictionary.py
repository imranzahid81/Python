# Dictionaries
# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

# For example, a database of phone numbers could be stored using a dictionary like this:

# phonebook = {}
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938377264
# phonebook["Jill"] = 947662781

# Alternatively, a dictionary can be initialized with the same values in the following notation:

phonebook = {
    "John": 93847756,
    "Jack": 93837726,
    "Jill": 94766278
}

# Iterating over dictionaries (using for & in)

for name, phNo in phonebook.items():
    print(f"Phone number of {name} is {phNo}")

# testing code 1 (For searching name(keys) in phonebook) 
if "John" in phonebook:
    print("John is listed in the phonebook.")

# testing code 2 (For searching phNo(values) in phonebook)
if 94766278 in phonebook.values():
    print ("Number found")
else:
    print("Number Not Found")
# # Removing a value 

phonebook = {
    "John": 93847756,
    "Jack": 93837726,
    "Jill": 94766278
}

del phonebook["John"]
print(f"1 Printing Phone book after del 'John' : {phonebook}")

phonebook = {
    "John": 93847756,
    "Jack": 93837726,
    "Jill": 94766278
}

phonebook.pop("Jill")
print(f"2 Printing Phone book after pop 'Jill' : {phonebook}")

# # conditinal remove

phonebook = {
    "John": 93847756,
    "Jack": 93837726,
    "Jill": 94766278
}

if "John" in phonebook:
	phonebook.pop("John")
	print(f"3 Printing Phone book after conditional pop 'John' : {phonebook}")
