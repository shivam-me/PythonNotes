li=[4,3,5,1,9,6,7,8,2]
sorted_li =sorted(li) # Dosen't change the original list
print('Sorted List :\t',sorted_li) # Prints Sorted List :    [1, 2, 3, 4, 5, 6, 7, 8, 9]
li.sort() # Changes the original list

# To sort in descending order use reverse=True , True with T in caps
sorted_li =sorted(li,reverse= True)
li.sort(reverse=True)

# Tuple don't have sort method(to change orginal),it only has sorted method
Tuple=(4,3,5,1,9,6,7,8,2)
print(sorted(Tuple)) # Prints [1, 2, 3, 4, 5, 6, 7, 8, 9] which is a list

# In dictionary sorted is used and by default it is sorted according to the key value
So, Let's use only sorted method in all the cases

li=[-5,-6,-7,1,2,3,4]
print(sorted(li,key=abs)) # Prints [1, 2, 3, 4, -5, -6, -7] according to absolute value

# Let's cover Sorting of object in OOP class

