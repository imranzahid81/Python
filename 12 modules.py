# Modules and Packages

# Modules in Python are simply Python files with the .py extension, which implement a set of functions. Modules are imported from other modules using the import command.i

# Check out the full list of built-in modules in the Python standard library: https://docs.python.org/2/library/

# If we want to import the module urllib, which enables us to create read data from URLs, we simply import the module

# import the library
import urllib

# use it
#urllib.urlopen("http://www.google.com.pk")


# To use the module bar, we can import it in two ways:
# import foo.bar
# or:
# from foo import bar



# Exploring built-in modules
# Two very important functions come in handy when exploring modules in Python - the dir and help functions.

# We can look for which functions are implemented in each module by using the dir function:
print dir(urllib)

help(urllib.urlopen)
