class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return(f'{self.first.capitalize()} {self.last.capitalize()}')

    # applying raise value by new custom method:
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)     # 4 % Raise

    def __repr__(self):
        return (f'Employee("{self.first}", "{self.last}", "{self.pay}")')

    def __str__(self):
        return (f'{self.fullname()} - {self.email}')


emp_1 = Employee('imran', 'Zahid', 60000)
emp_2 = Employee('Talha', 'hameed', 50000)

print(emp_1)
print(emp_2)
