# Iterator and Iterable

nums = [1, 2, 3]

i_nums = iter(nums)

# print(i_nums)
# print(dir(i_nums))

print(f"1st Iterator : {next(i_nums)}")
print(f"2nd Iterator : {next(i_nums)}")
print(f"3rd Iterator : {next(i_nums)}")