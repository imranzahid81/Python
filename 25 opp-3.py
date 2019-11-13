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

print(f"Previous Raise Amount : {Employee.raise_amt}")
print(f"Raised Amount Changed from 1.04 to 1.05")
Employee.set_raise_amt(1.05)

# But this will apply to all instances as well even if single instance is raised will raise all instances in class example 2 code lines below uncomment to use :
# print(f"This affects all Instances")
# emp_1.set_raise_amt(1.06)

print(f"All Employees Raise Amount : {Employee.raise_amt}")
print(f"Employee 1 Raise Amount : {emp_1.raise_amt}")
print(f"Employee 2 Raise Amount : {emp_2.raise_amt}")
