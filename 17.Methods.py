class Employee:

    raise_amount = 1.5
    no_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.no_of_emp += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def raises(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # It is called classmethod decorator ,using this it means we are working with class not particular instances
    def set_raise_amt(cls,amount): # Cls is class variable name
        cls.raise_amount = amount

    @classmethod # Self(instance) can also be used instead of cls(class variable), both works same but conveys different meanings.
    def from_string(cls,string):
        first, last, pay = str1.split('-')
        return cls(first,last,pay) # Create new instance/Object when 'from_string' method is called

    @staticmethod # It is used when we have nothing to do with instances,it dosen't take class/instance as argument
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # weekday() is pre-method , 5= Saturday,6=Sunday
            return False
        return True # If Week day is 0,1,2,3,4

emp1 = Employee('Shivam', 'Sharan', 50000)
emp2 = Employee('Griffolyon', 'Newz', 60000)

# USING CLASSMETHODS
emp1.set_raise_amt(1.75) # We are working with class not instances as set_raise_amt is classmethod so, it can be anything emp1,emp2,Employee
Employee.set_raise_amt(1.61) # This will also give the same result(amount=1.75) as stated above,It is advised to used this
emp1.set_raise_amt(1.80)  # Same result

# All of them prints 1.8 because we worked with the whole class whether we use emp1,emp2,Employee as per  Line 28
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# WITHOUT USING CLASSMETHODS
Employee.raise_amount = 1.75
emp1.raise_amount = 1.80
emp2.raise_amount = 1.92

print(Employee.raise_amount) # Prints 1.75
print(emp1.raise_amount) # Prints 1.8
print(emp2.raise_amount) # Prints 1.92


# TO CREATE INSTANCES FROM STRINGS

str1 = 'Koven-NCS-20000'
emp3 = Employee.from_string(str1)
print(emp3.email)  # Prints  Koven.NCS@company.com

# We can use this way but it is really bad
# str1 = 'Koven-NCS-20000'
# first, last, pay = str1.split('-')
# emp3 =Employee(first,last,pay)
# print(emp3.email)  # Prints Koven.NCS@company.com

# STATIC METHODS
import datetime
my_date =datetime.date(2020,5,13)
print(Employee.is_weekday(my_date)) # Print True, We can also use emp1 and emp2 as it is independent of instances
