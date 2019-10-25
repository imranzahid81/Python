# Exception Handling
# When programming, errors happen. It's just a fact of life. Perhaps the user gave bad input. Maybe a network resource was unavailable. Maybe the program ran out of memory. Or the programmer may have even made a mistake!

# Python's solution to errors are exceptions. You might have seen an exception before.

def do_stuff_with_number(n):
    print n

the_list = [1, 2, 3, 4, 5]


for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError: # Raised when accessing a non-existing index of a list
	print "exception block"
        do_stuff_with_number(0)




# example

actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
    return actor["name"].split()[1]

try:
	print "The actor's last name is %s" % get_last_name()
except:
	print "error"
