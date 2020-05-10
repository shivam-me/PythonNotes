
person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)


sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)



class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)



sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print(sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(**person)  # Unpacking dictionary
print(sentence)

for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)


for i in range(1, 11):
    sentence = 'The value is {:04}'.format(i)   # Value will be of 4 digits and starts with zeros
    print(sentence)
# The above program prints
# The value is 0001
# The value is 0002
# The value is 0003
# The value is 0004
# The value is 0005
# The value is 0006
# The value is 0007
# The value is 0008
# The value is 0009
# The value is 0010

pi = 3.14159265

sentence = 'Pi is equal to {:.3f}'.format(pi)

print(sentence) # Prints 3.142


sentence = '1 MB is equal to {:,} bytes'.format(1000**5)  # Comma after 3 zeros and five times

print(sentence)  # 1 MB is equal to 1,000,000,000,000,000 bytes

sentence = '1 MB is equal to {:,.5f} bytes'.format(1000**5)  # Comma after 3 zeros and five times upto five decimal places

print(sentence)  # 1 MB is equal to 1,000,000,000,000,000.00000 bytes





import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)  # Prints 2016-09-24 12:30:45
# Here are some frequently used types

# class datetime.date
# An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Attributes: year, month, and day.

# class datetime.time
# An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. (There is no notion of “leap seconds” here.) Attributes: hour, minute, second, microsecond, and tzinfo.

# class datetime.datetime
# A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.


# class datetime.timedelta
# A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.

# class datetime.tzinfo
# An abstract base class for time zone information objects. These are used by the datetime and time classes to provide a customizable notion of time adjustment(for example, to account for time zone and/or daylight saving time).

# class datetime.timezone
# A class that implements the tzinfo abstract base class as a fixed offset from the UTC




sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence) # Prints March 01, 2016 , Look for screenshots for %B,%d,%Y


sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

print(sentence) # March 01, 2016 fell on a Tuesday and was the 061 day of the year.
