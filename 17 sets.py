# Sets
# Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:i

print(set("my name is Eric and Eric is my name".split()))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended both events, you may use the "intersection" method:
print("intersection")
print(a.intersection(b))
print(b.intersection(a))

# To find out which members attended only one event and not the other, use the "difference" method:
print("difference")
print(a.difference(b))
print(b.difference(a))

# To find out which members attended only one of the events, use the "symmetric_difference" method:
print("symmetric_difference")
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# To receive a list of all participants, use the "union" method:
print("union")
print(a.union(b))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict #### dont use as set
empty_set = set()
