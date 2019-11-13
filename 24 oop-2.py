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

print(f"Employee 1 pay before Raise : {emp_1.pay}")
emp_1.apply_raise()
print(f"Employee 1 pay After Raise : {emp_1.pay}")




