# Lists
# Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.

mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)

# print by indexes  "Print Index Position"
print('list print by indexes')
print("Print Index Position 0: " + str(mylist[0]))  # prints 1
print("Print Index Position 1: " + str(mylist[1]))  # prints 2
print("Print Index Position 2: " + str(mylist[2]))  # prints 3 x

# print by for loop:
print('list print by forloop')
for items in mylist:
    print("Print whole list with forloop: " + str(items))

# print List with Index number:
print('Print List with Index number')
mylist_1 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
for index, items in enumerate(mylist_1):
    print("Print whole list and index number with forloop: " +
          str(index) + " " + str(items))

# print List with My Specified Index number:
print('print List with My Specified Index number')
mylist_1 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
for index, items in enumerate(mylist_1, start=1):
    print("Print whole list and My Specified index number with forloop: " +
          str(index) + " " + str(items))

# Accessing an index which does not exist generates an exception (an error).

# mylist2 = [1,2,3]
# print(mylist2[10])

print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
# NEW MATERIAL (append, insert and extend method) :

courses = ['History', 'Math', 'Physics', 'Biology']
print('Printing List .... COURSES: ' + str(courses))

courses.append('Art')
print('Appending with "Art" .... Printing List COURSES: ' + str(courses))

courses.insert(0, 'Chemistry')
print('Inserting with "Chemistry" at index 0 .... Printing List COURSES: ' + str(courses))

# Adding 2 seperate Lists:

# Method #1
courses_1 = ['History', 'Math', 'Physics', 'Biology']
courses_2 = ['English', 'Urdu']
courses_1.insert(0, courses_2)
# List within list..... Result: [['English', 'Urdu'], 'History', 'Math', 'Physics', 'Biology']
print('Simply inserting course_2 into course_1 by insert method gives list within list: ' + str(courses_1))

# Method #2
# but we want to merge the 2 list's into 1 so we do extend :
courses_1 = ['History', 'Math', 'Physics', 'Biology']
courses_2 = ['English', 'Urdu']
courses_1.extend(courses_2)
print('Simply extending course_2 into course_1 by extend method gives complete list : ' + str(courses_1))

# Removing List items:
courses_3 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
print('Printing List : ' + str(courses_3))
courses_3.remove('Physics')
print('Printing List after removing "Physics" with remove method: ' + str(courses_3))

# Pop Method :
courses_4 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
popped = courses_4.pop()
print('Printing Popped Item : ' + str(popped))
print('Printing Remaining List : ' + str(courses_4))

print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")

# Sort and Sorted Methods :   #
############################# sort is a method #############################
# Sort method sorts the original list....
courses_5 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
courses_5.sort()
print('Printing List with sort method : ' + str(courses_5))
############################################################################
courses_5 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
courses_5.sort(reverse=True)
print('Printing List with sort method in reverse : ' + str(courses_5))

############################# Sorted is a function #############################
# Sorted method leaves the original list and can be saved in separate variable .....
courses_5 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
sorted_method = sorted(courses_5)
print('Printing List : ' + str(courses_5))
print('Printing List with sorted method : ' + str(sorted_method))

# Number list: (minimum,maximum and sum value in list)
number_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print('Printing List: ' + str(number_1))
print('Printing Smallest Number in the List: ' + str(min(number_1)))
print('Printing Largest Number in the List: ' + str(max(number_1)))
print('Printing Sum of the List: ' + str(sum(number_1)))

# Finding values in list :
courses_6 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
print("finding index no of Biology in list with index method: " +
      str(courses_6.index('Biology')))
# if value is not in the list it will through error value is not in the list
# Checking whether the value is in the list or not
print("finding Biology in list with 'in' method: " + str('Biology' in courses_6))
print("finding Art in list with 'in' method: " + str('Art' in courses_6))
# if value present wil give True if not will give False

print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
# Displaying list in My custom formats:
# Format 1:
courses_7 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
courses_7_str = ' , '.join(courses_7)
print("Printing List as string with comma separated values : " + str(courses_7_str))

# Format 2:
courses_8 = ['History', 'Math', 'Physics', 'Biology', 'English', 'Urdu']
courses_8_str = ' - '.join(courses_8)
print("Printing List as string with hyphen separated values : " + str(courses_8_str))
# In place of comma OR hyphen any symbol, letter, number or word can be used

# Going back to list from string *** from prervious code block
new_list = courses_8_str.split(' - ')
print("Printing String as list by removing hyphen from hyphen separated values : " + str(new_list))
# Result is that you get your string back as it was before

###############  TUPLES  ###############
# tuples are in round brackets rather then in square brackets
# Mutable TUPLES
print('Mutable TUPLES')
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Immutable TUPLES
print('Immutable TUPLES')
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)


# SETS
