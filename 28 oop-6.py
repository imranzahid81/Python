class Employee:

    def __init__(self, first, last, pay):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

    def fullname(self):
        return(f'{self.first} {self.last}')


emp_1 = Employee('imran', 'Zahid', 60000)

emp_1.first = 'ali'

print(f"First Name : {emp_1.first}")
print(f"Last Name  : {emp_1.last}")
print(f"Full Name  : {emp_1.fullname()}")
print(f"Email      : {emp_1.email}")
print(f"Salary     : {emp_1.pay}")
'''
Output shows first name changed but not email.
Also if try to create a funtion for email like fullname function above
we wil have to change the way our classes call email like email()....
Well to much code nedds to be rewritten.
So in order to avoid unnecessary changes we use
PROPERTY Decorators: @propertyon functiion
See Below:
'''


class Employee01:

    def __init__(self, first, last, pay):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.pay = pay

    def fullname(self):
        return(f'{self.first} {self.last}')

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"


emp_1 = Employee01('talha', 'Hameed', 70000)

emp_1.first = 'Abbas'

print(f"First Name : {emp_1.first}")
print(f"Last Name  : {emp_1.last}")
print(f"Full Name  : {emp_1.fullname()}")
print(f"Email      : {emp_1.email}")
print(f"Salary     : {emp_1.pay}")


# Now For Setter and Deleter:

class Employee02:

    def __init__(self, first, last, pay):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.pay = pay

    @property
    def fullname(self):
        return(f'{self.first} {self.last}')

    @fullname.setter
    def fullname(self, name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print(f'Delete Name')
        self.first = None
        self.last = None

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"


emp_1 = Employee02('Mel', 'gibson', 80000)

emp_1.first = 'bob'

# emp_1.fullname = "Jack Sparrow"

print(f"First Name : {emp_1.first}")
print(f"Last Name  : {emp_1.last}")
print(f"Full Name  : {emp_1.fullname}")
print(f"Email      : {emp_1.email}")
print(f"Salary     : {emp_1.pay}")
del emp_1.fullname
print(f"First Name after del: {emp_1.first}")
print(f"Last Name  after del: {emp_1.last}")