class Employee:

    raise_amount = 1.5 # Class variables
    no_of_emp = 0  # Class variables

    def __init__(self, first, last, pay): # __init__ is called everytime when an instance is created
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        # self.no_of_emp +=1 # This will not work even after creating new instances
        Employee.no_of_emp += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def raises(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.no_of_emp) # Prints 0
emp1 = Employee('Shivam', 'Sharan', 50000)
emp2 = Employee('Griffolyon', 'Newz', 60000)
print(Employee.no_of_emp)  # Prints 2

print(emp1.pay)  # Prints 50000
emp1.raises()
print(emp1.pay) # Prints 75000

# All of them prints 1.5
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Notice Below if we try to find namespace of Employee,emp1,emp2
print(Employee.__dict__)
# Notice this contains raise_amount
# Prints {'__module__': '__main__', 'raise_amount': 1.5, '__init__': <function Employee.__init__ at 0x0000026002A873A8>, 'fullname': <function Employee.fullname at 0x0000026002A87288>, 'raises': <function Employee.raises at 0x0000026002A87048>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
print(emp1.__dict__)
print(emp2.__dict__)
# Prints {'first': 'Shivam', 'last': 'Sharan', 'pay': 50000, 'email': 'Shivam.Sharan@company.com'}
# Prints {'first': 'Griffolyon', 'last': 'Newz', 'pay': 60000,'email': 'Griffolyon.Newz@company.com'}

# We can change variables of classes
emp1.raise_amount = 1.75  # If we write Employee.raise_amount =1.75 all of them will print 1.75
print(emp1.__dict__)
# {'first': 'Shivam', 'last': 'Sharan', 'pay': 50000, 'email': 'Shivam.Sharan@company.com', 'raise_amount': 1.75} , It has now 'raise_amount'
print(Employee.raise_amount) # 1.5
print(emp1.raise_amount) # 1.75
print(emp2.raise_amount) # 1.5
















