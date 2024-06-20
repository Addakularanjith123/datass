lst=[10,20,9,39,84,44]
print(lst)
print(20 in lst)
print(50 in lst)
print(len(lst))
#append
lst.append("60")
print(lst)
lst.append(str(60))#this is the string type of 60 not integer
lst1=[10,20,9,39,84,44,"ranjith"]
print(lst1)
lst1.insert(2,"addakula")
print(lst1)
lst1.remove(84)#delete element in the list irresepctive of the index
print(lst1)
lst1.reverse()
print(lst1)
# print(lst1.sort())#it will not sorted because the list having the combination of integer and string
lst2=[30,8,33,21,12,44,89,23,3]
print(lst2)
# print(lst2.sort())
lst2.sort()
print(lst2)
#print(lst[2:])
