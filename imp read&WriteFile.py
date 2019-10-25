# Reading and Write files
# 'r' means read
# 'w' means write

# To Read a simple txt file
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line, end='')

# to Read Single Line
# with open('test.txt', 'r') as f:
#     f_contents = f.readline()
#     print(f_contents, end='')

# to Write to Single file
# with open('test2.txt', 'w') as f:
#     f.write('Fuck You All')

# To Overwrite On file
# with open('test2.txt', 'w') as f:
#     f.write('Fuck You All')
#     f.seek(0)
#     f.write(' Twice')

# Read file content 10 chunks(character) at a time
# with open('test.txt', 'r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#  to Read file content 10 chunks at a time but till the end
# with open('test.txt', 'r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#         print(f_contents, end='')
#         f_contents = f.read(size_to_read)

#  To Read file content 10 chunksat a time and insert * after every loop till the end
# with open('test.txt', 'r') as f:
#     size_to_read = 50
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)


# tells start of new loop line and total chars till the end of its execution
# print(f.tell())

# To copy 1 file to another new file which will be created 
# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# Whole content is replaced with new
# with open('test2.txt', 'r') as rf:
#     with open('test_copy2.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

"""*********************************************"""

# with open('pic1.jpeg', 'rb') as rf:
#     with open('pic1_copy.jpeg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# with open('pic1.jpeg', 'rb') as rf:
#     with open('pic1_copy.jpeg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk=rf.read(chunk_size)
