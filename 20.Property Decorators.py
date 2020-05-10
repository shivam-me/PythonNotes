class Employee:

    raise_amount = 1.5

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # Property decorator can be used to if we want to use method without ()
    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    @property # These are called getters i.e used to get values like printing
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @fullname.setter # We use methodname.setter for which we want to develop setter
    def fullname(self,name): # Method name has to be same as original
        self.first,self.last = name.split(' ')

    @fullname.deleter  # We use methodname.setter for which we want to develop setter
    def fullname(self):  # Method name has to be same as original
        print("Delete Name!")
        self.first,self.last=None,None



emp1 = Employee('Shivam', 'Sharan')
emp2 = Employee('Griffolyon', 'Newz')

# GETTERS
print(emp1.fullname)  # Prints Shivam Sharan beacause of property decorator
# print(emp1.fullname()) # Will raise an error

# SETTERS
emp2.fullname = 'Ed Sheeran' # Will raise AttributeError: can't set attribute, if setter is not defined otherwise fine
print(emp2.first) # Prints Ed
print(emp2.email)  # Prints Ed.Sheeran@email.com

# DELETERS
del emp1.fullname # Prints Delete Name which shows deleter called
