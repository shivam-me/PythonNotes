a = [1,2,3]
b = [1,2,3]
c = a
print(b==a) # Prints True
print(b is a) # Prints False

print(id(a))
print(id(b))
# Both id are different 'is' checks for id
print(id(b) == id(a))  # Is same as writing print(b is a) which prints False
print(c is a) # Prints true

# False Values:
# False
# None
# Zero of any numeric type
# Any space sequence : (),'',[]
# Any empty mapping : {}

condition = ''

if condition:
    print('Satisfied')
else:
    print('Not Satisfied')
# Prints Not Satisfied


