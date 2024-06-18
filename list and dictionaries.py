lst1 = [10, 20, 30 ,40]
lst1[0]

10 in  lst1

lst2 = ["a", "b ", "c"]
"d" in  lst2

len(lst1)
# 4
if len(lst1) > 0:
    print("list is not empty")
else:
    print("list is empty")
# list is not empty  ## list is not empty is through an exception so it failed to execute th code and noted as comment

lst1.append("6")
lst1
# [10, 20, 30, 40, '6']
lst1.insert(1, "om sairam")
lst1
# [10, 'om sairam', 20, 30, 40, '6']
lst1 = [1 ,1, 2,2,2 ]
lst1
# [1, 1, 2, 2, 2]
lst1 = [10, 20, 30 ,40]
lst1.remove(10)
lst1
# [20, 30, 40]
#lst1.remove(50)  ## in list the element 50 is not consists so it shows error
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[21], line 1
# ----> 1 lst1.remove(50)
#
# ValueError: list.remove(x): x not in list
lst1
# [20, 30, 40]
lst1.reverse()
lst1
# [40, 30, 20]
lst1.sort()
lst1
# [20, 30, 40]
lst1 = [-200, -36, 76, 89, 988, -987]
a = lst1.sort()
a
a
lst1
# [-987, -200, -36, 76, 89, 988]
lst_new = sorted(lst1)
lst_new
# [-36, -20, 76, 89, 988]
lst_new = [10, 20, 30, 40 ,50, 60 ]
lst_new[3:]
# [40, 50, 60]
lst_new[-1]
# 60
lst_new[-2]
# 50
lst_new
# [10, 20, 30, 40, 50, 60]
lst_new[-3:]
# [40, 50, 60]
lst_new
# [10, 20, 30, 40, 50, 60]
lst_new[0::3]
# [10, 40]
lst_reverse = lst_new[::-1]
lst_reverse
# [60, 50, 40, 30, 20, 10]
lst = [0]
mul_lst = lst*10
mul_lst
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lst = [1,2,3] *3
lst
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
lst1 = [1]
lst2 = [2]
lst3 = lst1 + lst2
lst3
# [1, 2]
lst1 = ["a", " b", "c"]
lst1_copy = lst1
lst1_copy.append("d")
lst1
# ['a', ' b', 'c', 'd']
lst2_copy = lst1.copy()
lst2_copy.append("e")
lst1
# ['a', ' b', 'c', 'd']
lst3_copy = lst1[:]
# Mutable

lst1
# ['a', ' b', 'c', 'd']
lst1[0] = 5
lst1
# [5, ' b', 'c', 'd']
#Tuple
#ordered, immutable , and allows duplicate elements
tup = ("pranav", "22", "lbnagar")
tup[0]
# 'pranav'
# tup[0] = "sairam"
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[73], line 1
# ----> 1 tup[0] = "sairam"
#
# TypeError: 'tuple' object does not support item assignment
tup[-1]
# 'lbnagar'
for i in tup:
    print(i)
print("pravav")
# 22
print("lbnagar")
"pranav" in  tup
# True
len(tup)
# 3
tup = ("b", "a", "n", "a", "n", "a")
tup.count("a")
# 3
tup.index("n")
# 2
lst = list(tup)
lst
# ['b', 'a', 'n', 'a', 'n', 'a']
tuple(lst)
# ('b', 'a', 'n', 'a', 'n', 'a')
tup = ("pranav", "22", "lbnagar")
a,b,c = tup
a
# 'pranav'
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

for k in zip(lst1,lst2):
    print(k)
    #print(i+j)
# (1, 4)
# (2, 5)
# (3, 6)
list(zip(lst1, lst2))
# [(1, 4), (2, 5), (3, 6)]
for k in zip(lst1,lst2):
    print(k)
list(enumerate(lst2))
# [(0, 4), (1, 5), (2, 6)]
a,b = (0,4)
for index,value in enumerate(lst2):
    print(index)
# 0
# 1
# 2
list(range(0,10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tup = ("pranav", 22, "lbnagar", True)
type(tup)
tuple
a, b , c, d = tup
type(d)
# bool
type(b)
# int
num_tup = tuple(range(0,10))
num_tup
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
i1, i2, i3,i4,i5,i6,i7,i8,i9,i10 = num_tup
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[126], line 1
# ----> 1 i1, i2, i3 = num_tup
#
# ValueError: too many values to unpack (expected 3)
i1
# 0
i3
# 9
i2
# [1, 2, 3, 4, 5, 6, 7, 8]
#Dictionary
#key-value pair , unordered, mutable
dict_1 = {"name": "pranav", "age":22, "location":"lbnagar", "is_good": True}
dict_1["name"]
# 'pranav'
dict_1["is_good"]
# True
print(dict_1)
# {'name': 'pranav', 'age': 22, 'location': 'lbnagar', 'is_good': True}
dict_1["age"] = 38
dict_1
# {'name': 'pranav', 'age': 38, 'location': 'lbnagar', 'is_good': True}
del dict_1["name"]
dict_1
# {'age': 38, 'location': 'lbnagar', 'is_good': True}
dict_1.pop("age")
# 38
dict_1
# {'location': 'lbnagar', 'is_good': True}
dict_1 = {"name": "pranav", "age":22, "location":"lbnagar", "is_good": True}
dict_1.keys()
# dict_keys(['name', 'age', 'location', 'is_good'])
"name" in  dict_1.keys()
# True
dict_1.values()
# dict_values(['pranav', 22, 'lbnagar', True])
dict_1.items()
# dict_items([('name', 'pranav'), ('age', 22), ('location', 'lbnagar'), ('is_good', True)])
print("Before...")
print(dict_1)
for key, value in dict_1.items():
    if value == "pranav":
        del dict_1["name"]
        break

print("After...")
print(dict_1)
# Before...
# {'name': 'pranav', 'age': 22, 'location': 'lbnagar', 'is_good': True}
# After...
# {'age': 22, 'location': 'lbnagar', 'is_good': True}
dict_1 = {"name": "pranav", "age": 22, "location": "lbnagar", "is_good": True}
dict_2 = {"name": "sairam", "age1": 3455, "location": "sec", "is_good": False}
dict_1.update(dict_2)
dict_1
# {'name': 'sairam',
#  'age': 22,
#  'location': 'sec',
#  'is_good': False,
#  'age1': 3455}
dict_1 = {"name": "pranav", "age": 22, "location": "lbnagar", "is_good": True}
# dict_1["age2"]
# ---------------------------------------------------------------------------
# KeyError
# Traceback(most
# recent
# call
# last)
# Cell
# In[159], line
# 1
# ----> 1
# dict_1["age2"]
#
# KeyError: 'age2'
try:
    print(dict_1["age2"])
except:
    print("no such key")

# no
# such
# key