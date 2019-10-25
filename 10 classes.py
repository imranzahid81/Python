# Classes and Objects

# Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

# A very basic class would look something like this:


# class Employee:
#     def __init__(self, firstName, lastName, salary):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.salary = salary
#         self.email = f"{firstName}.{lastName}@mcc.com"

#     def fullName(self):
#         return (f'{self.firstName} {self.lastName}')


# emp_1 = Employee('Imran', 'Zahid', 50000)
# emp_2 = Employee('Talha', 'Hameed', 60000)

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullName())
# print(emp_2.fullName())

# # Second method of Printing

# print(Employee.fullName(emp_1))
# print(Employee.fullName(emp_2))

# ************************************************************************************
# now for more complicated version

class Employee2:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.email = f"{firstName}.{lastName}@mcc.com"
        Employee2.num_of_emps += 1

    def fullName(self):
        return (f'{self.firstName} {self.lastName}')

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


print(
    f"1 Number of employees before adding Employee : {Employee2.num_of_emps}")

emp_1 = Employee2('Imran', 'Zahid', 50000)
emp_2 = Employee2('Talha', 'Hameed', 60000)
emp_3 = Employee2('Salman', 'Shaikh', 10000)

print(f"2 Number of employees after adding Employee : {Employee2.num_of_emps}")

# Employee2.raise_amount = 1.05
# # emp_1.raise_amount = 1.05

# print(f"1 Pre Defined Salary : {emp_1.salary}")
# print(f"2 Pre Defined Salary : {emp_2.salary}")

# emp_1.apply_raise()
# emp_2.apply_raise()

# print(f"1 After applying for Raise : {emp_1.salary}")
# print(f"2 After applying for Raise : {emp_2.salary}")

# print(emp_1.__dict__)
# print(emp_2.__dict__)


# ************************************************************************************
# now for more complicated version
# Adding Class Method

class Employee3:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.email = f"{firstName}.{lastName}@mcc.com"
        Employee2.num_of_emps += 1

    def fullName(self):
        return (f'{self.firstName} {self.lastName}')

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        pass


print(f"1 Number of employees before adding Employee : {Employee3.num_of_emps}")

emp_1 = Employee3('Imran', 'Zahid', 50000)
emp_2 = Employee3('Talha', 'Hameed', 60000)
emp_3 = Employee3('Salman', 'Shaikh', 10000)




















# class MyClass:
#     variable = "blah"
#     print(f"This is a variable : {variable}")

#     def function(self):
#         return("This is a message inside the class.")
#         # print(f"This is varibale :{variable}")    # variable is not global

# # class initialize
# myobjectx = MyClass()

# # calling function of the class
# print(f"Printing function : {myobjectx.function()}")

# # getting/access variable from that class
# # print(myobjectx.variable)
