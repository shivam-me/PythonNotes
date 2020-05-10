my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Index    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Index  -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# Slicing Rule list[start:end:step] step is default=1

print(my_list[1:4]) # Prints [1, 2, 3] end is not included
print(my_list[-9:-6]) # Prints [1, 2, 3] end is not included
print(my_list[:-1]) # Prints [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[:]) # Prints entire list
print(my_list[-8:8:2]) # Prints [2, 4, 6] using step of 2
print(my_list[::-1]) # Prints [9, 8, 7, 6, 5, 4, 3, 2, 1,0] using step of -1 i.e. in reverse order

The same rule works for strings
url="http:\\itisnotthatimportant.su"
print(url[::-1]) # Prints URL in reverse us.tnatropmitahttonsiti\:ptth

