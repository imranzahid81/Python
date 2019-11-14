class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return(f'Full Name : {self.first} {self.last}')

    # applying raise value by new custom method:
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)     # 4 % Raise

    # cls variable is representing class as word class cannot be used......
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Imran', 'Zahid', 60000)
emp_2 = Employee('Talha', 'Hameed', 50000)
emp_3 = Employee('Yousuf', 'Qutubuddin', 50000)

# print(f"Previous Raise Amount : {Employee.raise_amt}")
# print(f"Raised Amount Changed from 1.04 to 1.05")
Employee.set_raise_amt(1.05)

# But this will apply to all instances as well even if single instance is raised will raise all instances in class example 2 code lines below uncomment to use :
# print(f"This affects all Instances")
# emp_1.set_raise_amt(1.06)

# print(f"All Employees Raise Amount : {Employee.raise_amt}")
# print(f"Employee 1 Raise Amount : {emp_1.raise_amt}")
# print(f"Employee 2 Raise Amount : {emp_2.raise_amt}")

##############################################################
##############################################################
##############################################################
##############################################################

# Beginning Of 2nd Class Method A


class Employee01:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employee01.num_of_emps += 1

    def fullname(self):
        return(f'Full Name : {self.first} {self.last}')

    # applying raise value by new custom method:
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)     # 4 % Raise

    # cls variable is representing class as word class cannot be used......
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee01('Imran', 'Zahid', 60000)
emp_2 = Employee01('Talha', 'Hameed', 50000)
emp_3 = Employee01('Yousuf', 'Qutubuddin', 50000)

# Passing in a string to create new Employee :
# Basic Method :

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee01(first, last, pay)
# print(new_emp_1)

# new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
print(Employee01.num_of_emps)

# Beginning Of 2nd Class Method B
# No need to parse Strings as class method wil do it


class Employee02:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employee02.num_of_emps += 1

    def fullname(self):
        return(f'Full Name : {self.first} {self.last}')

    # applying raise value by new custom method:
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)     # 4 % Raise

    # cls variable is representing class as word class cannot be used......
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # This is for Parsing string Automatically:
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee02('Imran', 'Zahid', 60000)
emp_2 = Employee02('Talha', 'Hameed', 50000)
emp_3 = Employee02('Yousuf', 'Qutubuddin', 50000)

# Passing in a string to create new Employee :
# Basic Method :

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee02.from_string(emp_str_1)
new_emp_2 = Employee02.from_string(emp_str_2)
new_emp_3 = Employee02.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_1.pay)
print(Employee02.num_of_emps)

# Static Method :


class Employee03:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employee03.num_of_emps += 1

    def fullname(self):
        return(f'Full Name : {self.first} {self.last}')

    # applying raise value by new custom method:
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)     # 4 % Raise

    # cls variable is representing class as word class cannot be used......
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # This is for Parsing string Automatically:
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee03('Imran', 'Zahid', 60000)
emp_2 = Employee03('Talha', 'Hameed', 50000)

import datetime
my_date = datetime.date(2016, 7, 11)

print(f"Is it a work Day? : {Employee03.is_workday(my_date)}")


