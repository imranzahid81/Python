# Partial functions
# You can create partial functions in python by using the partial function from the functools library.

# Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function.

# Import required:


from functools import partial


# Example: from functools import partial def multiply(x,y): return x * y

# create a new function that multiplies by 

# example 1
def multiply(x,y): return x * y

dbl = partial(multiply,2)
print dbl(4)



# exampl 2
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

p = partial(func,6,7)
print p(8, 10)


