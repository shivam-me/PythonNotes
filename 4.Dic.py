student = {'name':'Shivam','age':'20','courses':['Python','DataScience']}
print(student['name'])

# TO check if a key exist or not use get method
print(student.get('subject')) # prints None or change using second argument
print(student.get('subject','Oops Not Found')) # prints Oops Not Found

# To update or add new key-val pair to dic
student['stream']='Comp' # Adds 'stream': 'Comp' to dic
# We can directly update the existing value of one key but to update more than one update method is used
student.update({'name':'Griffolyon','age':'21','city':'Pune'}) # We will use update always

# We can use del or pop method to remove a key ,pop can be used for storing the pop value in the variable
del student['city']
popped = student.pop('stream')

print(len(student))
print(student.keys())
print(student.values())
print(student.items()) # Contains both keys and values


