# SQLite Database Creation and Handling

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{first}.{last}@company.com'
    
    @property
    def fullname(self):
        return f'{first} {last}'

    def __repr__(self):
        return f'Employee("{first}","{last}","{pay}")'

    

