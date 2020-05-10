courses= ['ML','Neural Networks','React JS'] # Lists, it is formed by using square brackets
print(type(courses))
print(len(courses))
print(courses[1]) # Indexing
print(courses[-1]) # Getting last element of the list
print(courses[:2]) # Prints ['ML', 'Neural Networks'] ,remember second index is not inclusive
courses.append('Node JS') # To add/append element at the end of list
courses.insert(0,'Blockchain') # To add element at the specific index
print(courses.index('React JS')) # Prints the index of the element

# If we want to check if element is present in list or not use this
print('ML' in courses) # Prints True


# If we want to merge to lists use extends otherwise insert will behave the latter list as an individual list within list
courses_1=['C++','Python']
courses.append(courses_1)
print(courses)  # It Prints ['ML', 'Neural Networks', 'React JS', ['C++', 'Python']] where last element is itself a list
courses.extend(courses_1) # It prints ['ML', 'Neural Networks', 'React JS', 'C++', 'Python'] as desired
print(courses)

courses.remove('React JS')
popped = courses.pop()  # It will remove last element 'React JS' like a stack/queue
# print(popped) # It prints the popped value React JS
# print(courses) # It prints the resultant original list i.e ['ML', 'Neural Networks']
# courses.reverse()
# courses.sort() # Sorts in ascending order of name
# courses.sort(reverse=True) # Sorts in descending order
# sorted(courses) # This dosen't change the original list just a sorted version of that

# To convert Lists to String use join method
courses_str='-'.join(courses) # Prints "ML-Neural Networks"
# To convert Strings to List use split method
courses_list=courses_str.split('-')

nums =[5,2,6,3,1]
print(max(nums)) # Prints 6
print(sum(nums)) # Prints 17 as sum of all numbers

# TUPLES CAN'T BE MODIFIED LIKE LISTS SO THEY ARE CALLED IMMUTABLE AND IS REPRESENTED USING PARANTHESIS
courses= ('ML','Neural Networks','React JS')
print(type(courses)) # <class 'tuple'>
# courses[0]='HI'
print(courses) # It will raise an TypeError: 'tuple' object does not support item assignment
# So tuples are only usefull when we create a immutable list(i.e Tuple) and just iterate through them using loops etc.

# SETS ARE USED TO CHECK IF AN ELEMENT IS PART OF SET OR NOT,IT DOSEN'T CARE ABOUR ORDER. IT IS REPRESENTED BY CURLY BRACES
courses= {'ML','Neural Networks','React JS','ML'}
courses_new ={'Maths','React JS','English'}
print(courses) # Print result varies like {'ML', 'React JS', 'Neural Networks'} dosen't care aboout order and also ignores duplicates
print('ML' in courses) # Prints true and sets are mainly used for this purpose and set operations

print(courses.intersection(courses_new)) # Prints React JS
# Similarly we can use union,difference or to check various methods use
print(dir(courses))
'''Prints ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__',
'__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
'__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection','intersection_update', 'isdisjoint', 'issubset', 'issuperset',
'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'] '''


# To create empty lists,tuples,sets
empty_list=[]    # Creates empty lists
empty_list=list() # Creates empty lists also

empty_tuple=()    # Creates empty tuple
empty_tuple=tuple() # Creates empty tuple also

empty_set={}    # This is not an empty set, it is an empty dictonary
empty_list=list() # Creates empty set







