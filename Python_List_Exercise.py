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
#print(list3)

#Exercise Question 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

# Exercise Question 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = list(filter(None,list1))
# print(list2)

# Exercise Question 7: Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
# print(list1)

# Exercise Question 8: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
tmp_ls = ["h","i","j"]
list1[2][1][2].extend(tmp_ls)
# print(list1)

# Exercise Question 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
t = list.index(20)
list1[t] = 200
# print(list1)

# Exercise Question 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = []
for i in list1:
	if i != 20:list2.append(i)
print(list2)