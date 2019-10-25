sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))

print word_lengths


# Using a list comprehension, we could simplify this process to this notation:

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]

print word_lengths		# result will be same


# example

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print newlist
