# import random


# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#         yield random.randint(1, 40)

#     # returns a 7th number between 1 and 15
#     yield random.randint(1, 15)


# for random_number in lottery():
#     print(f"And the next number is... {random_number}!")


# Custom Code 1 :
# Basic Conditional Code

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5])
# print(my_nums)

# Custom Code 2 :
# Generator code version


def square_numbers(nums):
    for i in nums:
        yield (i*i)


my_nums = square_numbers([1, 2, 3, 4, 5])

# But only one result at a time is shown and it waits for nest calling
# so we call it five times as 5 items are present in the list

print(f"This is with just print 1 : {next(my_nums)}")
print(f"This is with just print 2 : {next(my_nums)}")
print(f"This is with just print 3 : {next(my_nums)}")
print(f"This is with just print 4 : {next(my_nums)}")
print(f"This is with just print 5 : {next(my_nums)}")

# print(next(my_nums))  6th input yields error as their is no 6th item in the list!
# So to complete all result we use for loop :


def square_numbers(nums):
    for i in nums:
        yield (i*i)


my_nums = square_numbers([1, 2, 3, 4, 5])

for num in my_nums:
    print(f"This is with for loop : {num}")


# Custom Code 3 :
# Generator code version
# List Comprehension Version

my_nums = (x*x for x in [1, 2, 3, 4, 5])
# print(list(my_nums))

for num in my_nums:
    print(f"This is with List Comprehension : {num}")

print(f"without saving to a variable : {list(x*x for x in [1, 2, 3, 4, 5])}")