class Employee:

    # __init__ is called everytime when an instance is created, it is like constructor from c++
    def __init__(self, first, last, pay):  # It is not necessary to name it self,
        self.first = first  # self.fanme=first but it is advised to keep the same name
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):  # Instance is the only argument in this function ,Always add self to function classes
        return '{} {} '.format(self.first, self.last)


emp1 =Employee('Shivam','Sharan',50000)
# Manualy what happens is it sets
# emp1.first =first
# emp1.last = last and so on
# Which means self is replaced by emp1 i.e. instance of the class

print(emp1.email)  # Prints Shivam.Sharan@company.com
print('{} {} '.format(emp1.first, emp1.last))  # Prints Shivam Sharan
print(emp1.fullname())  # Prints Shivam Sharan
print(Employee.fullname(emp1))  # Prints Shivam Sharan , We will not use this often














