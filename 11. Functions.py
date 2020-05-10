def hello(greeting, name = 'Shivam'):
    return '{}, {}'.format(greeting,name)
print(hello('Hello'))  # Prints Hello, Shivam  Here second parameter is optional with a default value set.
print(hello('Hello', 'Sharan '))  # Prints Hello, Sharan
print(hello('Hello', name ='Sharan ')) # It is same thing

def student(*args,**kwargs):
    print(args)
    print(kwargs)


course = ['math', 'arts']
info = {'name': 'Shivam', 'age': 20 }

student(*course,**info)
# Prints ('math', 'arts') ----Tuple (args)
# {'name': 'Shivam', 'age': 20} ----Dictionary (kwargs)


student('math','arts',name='Shivam',age=20)
Prints ('math', 'arts') ----Tuple (args)
{'name': 'Shivam', 'age': 20} ----Dictionary (kwargs)






# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year)
    # Return True for leap years, False for non-leap years.

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month)
    # Return number of days in that month in that year.

    # year 2017
    # month 2
    if not 1 = month = 12
        return 'Invalid Month'

    if month == 2 and is_leap(year)
        return 29

    return month_days[month]

print(days_in_month(2017, 2))
