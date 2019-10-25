"""  GENERATORS  """

# this is basic function and its execution
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result


# my_nums = square_numbers([1, 2, 3, 4, 5])
# text_1 = "This is the square of numbers in list 1 : "
# print(f'{text_1} {my_nums}')  # [1, 4, 9, 16, 25]


# now to to make Generator the above code becomes :
# def square_numbers2(nums):
#     for i in nums:
#         yield(i*i)


# my_nums2 = square_numbers2([1, 2, 3, 4, 5])
# text_2 = "This is the square of numbers in list 2 : "
# # print(f'{text_2} {my_nums2}')

# """ But this gives <generator object square_numbers2 at 0x7fb97690d570> which is not the result we want.
# So, we go through object one index at a time to get the result by using next method """
# # plz comment out line 22 before running 5 print statements below:
# print(f'{text_2} {next(my_nums2)}')
# print(f'{text_2} {next(my_nums2)}')
# print(f'{text_2} {next(my_nums2)}')
# print(f'{text_2} {next(my_nums2)}')
# print(f'{text_2} {next(my_nums2)}')
# print(f'{text_2} {next(my_nums2)}')

# If you run a sixth statement it wil through error StopIteration:
# so how do we know how many indexes does a list have (in case of very big list)
# so printing all index that are present will be done by FOR LOOP


# def square_numbers2(nums):
#     for i in nums:
#         yield(i*i)


# my_nums3 = square_numbers2([1, 2, 3, 4, 5])
# for num in my_nums3:
#     text_3 = "This is the square of numbers in list 2 : "
#     print(f'{text_3} {num}')


# Comprehension way:
my_nums4 = [x*x for x in [1, 2, 3, 4, 5]]
for num in my_nums4:
    text_4 = "This is the square of numbers in Comprehension style : "
    print(f'{text_4} {num}')

# Making Generator:
# Replacing square barckets with round brackets makes it a GENERATOR
my_nums4 = (x*x for x in [1, 2, 3, 4, 5])
for num in my_nums4:
    text_4 = "This is the Generator : "
    print(f'{text_4} {num}')
""" This provides perfomance boost as no memory is used """

# But what if we want output also as list so with just a addition of list:
my_nums5 = (x*x for x in [1, 2, 3, 4, 5])
text_5 = "This is the Generator in the form of LIST : "
print(f'{text_5} {list(my_nums5)}') 
""" tHIS method LOSES performance due to holding so many list items in variable """
