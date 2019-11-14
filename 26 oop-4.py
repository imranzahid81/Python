# Creating Subclasses :


class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first.lower()}.{last.lower()}@company.com'
        # As email is in lower so .lower() will keep output in lower case

        Employee.num_of_emps += 1

    def fullname(self):
        return(f'{self.first.capitalize()} {self.last.capitalize()}')
        # To keep first letter in full name capital we used .capitalize()

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            print(f'Employees Added : {emp.fullname()}')

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print(f'Employees Removed : {emp.fullname()}')

    def print_emps(self):
        for emp in self.employees:
            print(f'Employees under Manager\'s Supervision : {emp.fullname()}')


emp_1 = Developer('imran', 'Zahid', 50000, 'Python')
emp_2 = Developer('Talha', 'hameed', 60000, 'React')
emp_3 = Employee('Saqib', 'Raza', 20000)
emp_4 = Employee('Hassam', 'Ahmed', 30000)
mgr_1 = Manager('Sami', 'Hamza', 80000, [emp_1])
emp_5 = Manager('Ghani', 'Shahid', 90000)


print(f"Total No Of Employees : {Employee.num_of_emps}")

print(f"Employee 1 Full Name : {emp_1.fullname()}")
print(f"Programming Language : {emp_1.prog_lang}")
print(f"Employee 1 Email     : {emp_1.email}")

print(f"Employee 2 Full Name : {emp_2.fullname()}")
print(f"Programming Language : {emp_2.prog_lang}")
print(f"Employee 2 Email     : {emp_2.email}")

# comment out code below to see code path and inheritence
# print(help(Developer))

print(f"Employee 1 Pay Before Raise : {emp_1.pay}")
emp_1.apply_raise()
print(f"Employee 1 Pay After Raise : {emp_1.pay}")

print(f"Employee 2 Pay Before Raise : {emp_2.pay}")
emp_2.apply_raise()
print(f"Employee 2 Pay After Raise : {emp_2.pay}")

mgr_1.print_emps()
print(f"Manager 1 Email : {mgr_1.email}")
mgr_1.add_emp(emp_3)
mgr_1.add_emp(emp_4)
mgr_1.print_emps()
mgr_1.remove_emp(emp_1)
mgr_1.print_emps()
