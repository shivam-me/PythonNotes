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



class Developer(Employee):  # Inheriting from class Employee
    raise_amount = 2 # If we don't provide explicity it will take default as 1.5

    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay) # It makes the base class(Employee) handle the init except prog_lang
        # Employee.__init__(self,first, last, pay) # It is same as Above but not commonly used
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None): # employees is an empty list ,manager will manage them

        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else :
            self.employees = employees

    def add_emp(self,emp): # Adding employees for manager
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self, emp):  # Removing employees for manager
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emp(self):

        for emp in self.employees:
            print('--->',emp.fullname())




emp1 = Developer('Shivam', 'Sharan', 50000,'Python')
emp2 = Developer('Griffolyon', 'Newz', 60000,'Java')


print(help(Developer))
'''
Help on class Developer in module __main__:

class Developer(Employee)
 |  Developer(first, last, pay)
 |
 |  Method resolution order: #! THESE ARE PLACES WHERE PYTHON SEARCHES FOR ATRRIBUTES AND METHODS
 |      Developer  #! IT FIRST LOOK IN DEVELOPER CLASS FOR INIT METHOD,BUT DIDN'T FIND IT THERE
 |      Employee #! THEN IT LOOK FOR INIT METHOD IN EMPLOYEE WHERE IT FOUND SUCCESSFULLY
 |      builtins.object #! EVERY PYTHON CLASS INHERIT FROM THIS BASE OBJECT
 |
 |  Methods inherited from Employee: #! INIT,FULLNAME AND RAISES
 |
 |  __init__(self, first, last, pay)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  fullname(self)
 |
 |  raises(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Employee:
 |
 |  raise_amount = 1.5

'''


print(emp1.pay)  # Prints 50000
emp1.raises()  # Takes raise_amount = 2 from developer then pass to method raises
print(emp1.pay) # Prints 100000

# WITHOUT INHERITANCE
# emp3 = Employee('Shivam', 'Sharan', 50000)
# print(emp3.pay)  # Prints 50000
# emp3.raises()  # Takes raise_amount = 1.5 from class Employee
# print(emp3.pay)  # Prints 75000

print(emp1.prog_lang) # Prints Python

mgr1 =Manager('Sue', 'Smith', 60000,[emp1])
print(mgr1.print_emp())  # Prints ---> Shivam Sharan

mgr1.add_emp(emp2)
print(mgr1.print_emp()) # ---> Shivam Sharan
                        # ---> Griffolyon Newz
mgr1.del_emp(emp2)

print(isinstance(mgr1,Manager)) # Prints True ,It is used to check if it is instance of a class
print(issubclass(Manager, Developer))  # Prints False

