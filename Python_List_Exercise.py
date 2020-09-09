### Python exercises from https://pynative.com/python-list-exercise-with-solutions/
#1. Exercise Question 1: Given a Python list you should be able to display Python list in the following order [500, 400, 300, 200, 100]
aLsit = [100, 200, 300, 400, 500]
aLsit.sort(reverse = True)
#print(aLsit)

# Exercise Question 2: Concatenate two lists index-wise to get output as ['My', 'name', 'is', 'Kelly']
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i+j for i,j  in zip(list1,list2)]
# print(list3)

# Exercise Question 3: Given a Python list. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
aLsits = [x **2 for x in aList]
# print(aLsits)

# Exercise Question 4: Concatenate two lists in the following order ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [i+j for i in list1 for j in list2]
print(list3)