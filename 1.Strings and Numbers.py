message ="Hello World"
print(len(message))   # This is of the form __len__
print(message.upper()) # This is method
print(message.lower())
print(message.count('l'))
print(message.find('Universe')) # Returns -1 if not found
message=message.replace("World"," ")

greeting="Shivam"
new_message=message + ', ' + greeting # But this is a bad way because it will get difficult for long numbers of + sign
new_message='{},{} .Welcome!'.format(message,greeting) # This is better than above but there is something else
new_message=f'{message},{greeting.upper()} .Welcome!' # This is called F-String introduced in Python 3.0+ . We can also use methods easily

# If we want to know the methods available for string manipulation use dir follow
print(dir(message))
''' Prints ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
'replace', 'rfind', 'rindex', 'rjust','rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 'zfill'] '''

# If we want to know the documentation methods available for string manipulation use dir follow
print(help(str))

num = -3.145
print(abs(num))  # Prints absolute value i.e non-negative value
print(round(num,2)) # Rounds the floating number to 2 decimal places

num1='100'
num2='200'
print(num1+num2) # This is concatenation because num1 and num2 are strings not integers

# Type Casting of strings to integers
num1=int(num1)
num2=int(num2)
print(num1+num2)

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2






