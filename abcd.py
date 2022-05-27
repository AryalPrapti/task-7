

#1.

# a = [18, 52, 23, 41, 32]
# smallest = min(a)
# print(f'Smallest number in the list is : {smallest}.')
 
#2.

# a = ["Hire", "the", "top", "1%", "freelancers"]

# b = []

# if a:
#     print("list is not empty")
# else:
#     print("list is empty")

#4.
# prime_numbers = [2, 3, 5]
# numbers = prime_numbers.copy()
# print('Copied List:', numbers)

#5.

# Python program to find second largest number
# in a list
 
# list1 = [10, 20, 4, 45, 99]
# new_list = set(list1)
# new_list.remove(max(new_list))
# print(max(new_list))

#8.
# intTuple = ()
# number = int(input("Enter the Total Number of Tuple Items = "))
# for i in range(1, number + 1):
#     value = int(input("Enter the %d Tuple value = " %i))
#     intTuple = intTuple + (value,)    
# print("Tuple Items = ", intTuple)

# #9.
# aTuple = (True, 28, 'Tiger')
# aList = list(aTuple)
# print(type(aList))
# print(aList)


#10.

# def convertTuple(tup):
#     st = ''.join(map(str, tup))
#     return st
# tuple = ('g', 'e', 'e', 'k', 's', 101)
# str = convertTuple(tuple)
# print(str)

#11.

# listx = [5, 10, 7, 4, 15, 3]
# print(listx)
# tuplex=tuple(listx)
# print(tuplex)
	 
#12.

# print(list x)
# tuplex=tuple(list x)
# print(tuplex)
# tuples=[('Key1',1),('Key2',2),('key3',3),('Key4',4),('Key5',5)]
# result={}
# for (Key,value)in tuples:
#        result.setdefault(Key,[].append(value))
#        print(result)

#15.

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)

# #17.
# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 4: 'd'}

# dict_3 = dict_2.copy()
# dict_3.update(dict_1)

# print(dict_3)

#19.

# s1 = {}
# print(s1)

# s2 = set()
# print(s2)

#20.
# num_set = set([0, 1, 2, 3, 4, 5])

# for n in num_set:
#   print(n)

#21.

# color_set = set()
# color_set.add("Red")
# print(color_set)

# color_set.update(["Blue", "Green"])
# print(color_set)

#22.

# num_set = set([0, 1, 3, 4, 5])
# print("Original set:")
# print(num_set)
# num_set.pop()
# print("\nAfter removing the first element from the said set:")
# print(num_set)

#23.

# num_set = set([0, 1, 2, 3, 4, 5])
# print("Original set elements:")
# print(num_set)
# print("\nRemove 0 from the said set:")
# num_set.discard(4)
# print(num_set)
# print("\nRemove 5 from the said set:")
# num_set.discard(5)
# print(num_set)
# print("\nRemove 2 from the said set:")
# num_set.discard(5)
# print(num_set)
# print("\nRemove 7 from the said set:")
# num_set.discard(15)
# print(num_set)

#24.

# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# setz = setx & sety
# print(setz)

