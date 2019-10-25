
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print(f"Condition 1 : {my_list[::-1]}")
print(f"Condition 2.a : {my_list[2:-1:2]}")
print(f"Condition 2.b : {my_list[2:9:2]}")
print(f"Condition 2.c : {my_list[-2:1:-2]}")

sample_url = 'http://www.google.com'
string_1 = "Print Simple Varialble : "
print(f"{string_1} {sample_url}")

# Reverse the url
string_2 = "Print Slicing from start til last Index (Reverse the url) : "
print(f"{string_2} {sample_url[::-1]}")


# # Get the top level domain
string_3 = "Printing the top level domain : "
print(f"{string_3} {sample_url[-4:]}")

# Print the url without the http://
string_4 = "Printing the url without the http:// : "
print(f"{string_4} {sample_url[7:]}")

# # Print the url without the http:// or the top level domain
string_5 = "Printing the url without the http:// or the top level domain : "
print(f"{string_5} {sample_url[11:-4]}")
