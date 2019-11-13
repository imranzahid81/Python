# Objected Oriented Programming Part 1

# Manual way of doing things:

class People:
    pass

person_1 = People()
person_2 = People()

print(f"Print 01 {person_1}")
print(f"Print 02 {person_2}")

person_1.first = "Imran"
person_1.last = "Zahid"
person_1.email = "imranzahid81@company.com"
person_1.pay = 60000

person_2.first = "Talha"
person_2.last = "Hameed"
person_2.email = "talhahameed@company.com"
person_2.pay = 50000

print(f"Print 03 : {person_1.email}")
print(f"Print 04 : {person_2.email}")

# now doing it through Class:

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return(f'Full Name : {self.first} {self.last}')


emp_1 = Employee("Imran",'Zahid',60000)
emp_2 = Employee('Talha','Hameed',50000)

# Runing through Instance:
print(f"Print 05 : {emp_1.email}")
print(f"Print 06 : {emp_2.email}")
print(f"Print 07 : {emp_1.fullname()}")
print(f"Print 08 : {emp_2.fullname()}")

# Runing through Class name:
print(f"Print 09 : {Employee.fullname(emp_1)}")
print(f"Print 10 : {Employee.fullname(emp_2)}")
