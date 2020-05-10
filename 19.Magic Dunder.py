class Employee:

    raise_amount = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def raises(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee({},{},{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay+other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Shivam', 'Sharan', 50000)
emp2 = Employee('Griffolyon', 'Newz', 60000)

print(emp1)  # Prints <__main__.Employee object at 0x0000014683608888> without __repr__
print(emp1)  # Prints Shivam Sharan  - Shivam.Sharan@company.com when both __repr__ and __str__ and Prints Employee(Shivam,Sharan,50000) without __str__

print(repr(emp1))  # or print(emp1.__repr__()) Prints Employee(Shivam,Sharan,50000)
print(str(emp1))   # or print(emp1.__str__()) Prints Shivam Sharan  - Shivam.Sharan@company.com

# Below add and len methods are used for objects by creating dunders as we used for strings and integers
print(emp1+emp2) # Prints 110000 because of add dunder otherwise it would show an error
print(len(emp1)) # Prints 14













