import zipfile
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# text_1 = 'This is the Basic version 1: '
# print(f"{text_1} {my_list}")

# my_list2 = [n for n in nums]
# text_2 = 'This is the Comprehension version 1: '
# print(f"{text_2} {my_list2}")

# I want 'n*n' for each 'n' in nums
# my_list3 = []
# for n in nums:
#     my_list3.append(n*n)
# text_3 = 'This is the Basic version 2: '
# print(f"{text_3} {my_list3}")

# my_list4 = [n*n for n in nums]
# text_4 = 'This is the Comprehension version 2: '
# print(f"{text_4} {my_list4}")

# Using a map + lambda doesnt work in python 3
# my_list4 = map(lambda n: n*n, nums)
# In python 3 this map will through complete filter object and not the value that we need
# In python 3 you get complete objects and in order to print you need to loop through them
# for i in my_list4:
#       text_4 = 'This is the Math version 1 : '
#       print(f"{text_4} {i}")

# I want 'n' for each 'n' in nums if 'n' is even
# my_list5 = []
# for n in nums:
#     if n % 2 == 0:
#         my_list5.append(n)
# text_5 = 'This is the Basic version 3: '
# print(f"{text_5} {my_list5}")

# my_list6 = [n for n in nums if n % 2 == 0]
# text_6 = 'This is the Comprehension version 3: '
# print(f"{text_6} {my_list6}")

# Using a filter + lambda
# my_list6 = filter(lambda n: n % 2 == 0, nums)
# # In python 3 this filter will through complete filter object and not the value that we need
# In python 3 you get complete objects and in order to print you need to loop through them
# for i in my_list6:   # this loop is to print values inside filter object in python 3
#     text_6 = 'This is the Math version 2 : '
#     print(f"{text_6} {i}")


# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list7 = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list7.append((letter, num))
# text_7 = 'This is the Basic version 4: '
# print(f"{text_7} {my_list7}")

# my_list8 = [(letter,num) for letter in 'abcd' for num in range(4)]
# text_8 = 'This is the Comprehension version 4: '
# print(f"{text_8} {my_list8}")


# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(zip(names, heros))   doesn't work in python 3

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# text_9 = 'This is the Basic version 5: '
# print(f"{text_9} {my_dict}")

# my_dict2 = {name: hero for name, hero in zip(names,heros)}
# text_10 = 'This is the Comprehension version 5: '
# print(f"{text_10} {my_dict2}")


# If name not equal to Peter means don't print Peter if present
# my_dict3 = {name: hero for name, hero in zip(names,heros) if name != "Peter"}
# text_11 = 'This is the Comprehension version 5.2: '
# print(f"{text_11} {my_dict3}")

# Set Comprehensions
nums2 = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# my_set = set()
# for n in nums2:
#     my_set.add(n)
# text_12 = 'This is the set Basic version 6: '
# print(f"{text_12}{my_set}")

# my_set2 = {n for n in nums2 if n in set(nums2)}
# print(my_set2)

# my_set2 = {n for n in nums2}
# text_13 = 'This is the Comprehension version 6: '
# print(f"{text_13}{my_set2}")

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def gen_func(nums3):
#     for n in nums3:
#         yield n*n


# my_gen = gen_func(nums3)

# for i in my_gen:
#     print(i)
