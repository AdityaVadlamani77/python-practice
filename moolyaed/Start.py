"""l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[1:1:3])
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7:2])"""

# Python program to demonstrate
# string slicing# String slicing
String = 'ASTRING'  # Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
# s3 = slice(-1, -12, -2)
print(String[s1])
print(String[s2])
# print(String[s3])

# String slicing
#         0123456789
String = 'GPEKSFORGE'
# Using indexing sequence
print(String[1:5:4])
# 1 2 3 4 5
# p e k s f
#    0  1  2  3  4  5  6  7  8  9
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[1:2:4])
# list[start:stop:step]
# 1 2 3 4 5
# 1 4
l.insert(8, 10)
print(l)
set1 = {1, 2, 3, 4, 3, 4, 'A', 'B', 'C', 'D'}
set2 = {41, 42, 43, 44, 45, 46, 47, 'A', 'B'}
k = set1.union(set2)
print(k)
m = set1.intersection(set2)
print(m)
l = set1.symmetric_difference(set2)
print(l)
print(set1)
set1.add(100)
print(set1)
set1.pop()
print(set1)
a = 50
a += 100
print(a)
for i in set1:
    print(i)
