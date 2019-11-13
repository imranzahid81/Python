# OOP-1 finished code with salary bonus code


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return(f'Full Name : {self.first} {self.last}')

    # applying raise value by new custom method:
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)     # 4 % Raise


emp_1 = Employee('Imran', 'Zahid', 60000)
emp_2 = Employee('Talha', 'Hameed', 50000)

# print(f"Employee 1 pay before Raise : {emp_1.pay}")
# emp_1.apply_raise()
# print(f"Employee 1 pay After Raise : {emp_1.pay}")

# But what if we can edit or see the raise amount which in above code is dispersed 


class Employee01:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return(f'Full Name : {self.first} {self.last}')

    # applying raise value by new custom method:
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)     # 4 % Raise


emp_1 = Employee01('Imran', 'Zahid', 60000)
emp_2 = Employee01('Talha', 'Hameed', 50000)
emp_1.apply_raise()

# to see what methods are available in our Class Employee :
print(f"Methods available to Class Employee01 : {Employee01.__dict__}")

# to see what methods are available in our both employee instances (emp_1,emp_2) :
print(f"Methods available in emp_1 instance : {emp_1.__dict__}")
print(f"Methods available in emp_2 instance : {emp_2.__dict__}")

print(f"Employee 1 pay before Raise : {emp_1.pay}")
print(f"Employee 2 pay before Raise : {emp_2.pay}")
emp_1.apply_raise()
print(f"All Employees Raise Amount : {Employee01.raise_amount}")
print(f"Employee 1 Raise Amount : {emp_1.raise_amount}")
print(f"Employee 2 Raise Amount : {emp_2.raise_amount}")
print(f"Employee 1 pay After Raise : {emp_1.pay}")
print(f"Employee 2 pay Remains the Same : {emp_2.pay}")
