import my_module as mm  # Prints  Module imported which shows success
# from my_module import find_index as fi, test
# from my_module import *
import sys
import

courses = ['Math','Chemistry','Physics']

index = mm.find_index(courses,'Math')
# index = fi(courses, 'Math') # If Function is imported directly

print(index) # Prints 0
# print(sys.path)

