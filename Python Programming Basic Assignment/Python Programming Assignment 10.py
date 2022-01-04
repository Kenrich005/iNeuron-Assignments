# 1. Write a python program to find sum of elements in a list

newlist = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10]

print(sum(newlist))

f_sum = 0
for i in newlist:
    f_sum = f_sum + i
print('sum = ', f_sum)

# 2. Write a python program to multiply all number in the list
import numpy as np

print('product = ', np.prod(newlist))

f_prod = 1
for i in newlist:
    f_prod = f_prod * i
print('product = ', f_prod)

# 3. Write a Python program to find the smallest number in a list

print('min = ', min(newlist))

# 4. Write a Python program to find the largest number in a list

print('max = ', max(newlist))

# 5. Write a Python program to find second largest number in the list

newlist.sort()

print('second largest number = ', newlist[-2])


# 6. Write a Python Program to find n largest number in the list

def n_largest(n):
    print(f'{n}th largest integer is = {newlist[-n]}')


n_largest(5)

# 7. Write a python program to return even number in a list
evenlist = []
for i in newlist:
    if i % 2 == 0:
        evenlist.append(i)
print(evenlist)

# 8. Write a Python program to print the odd numbers in a list

oddlist = []

for i in newlist:
    if i % 2 != 0:
        oddlist.append(i)
print(oddlist)

# 9. Write a Python program to remove empty list from list

emptylist = [1, 2, 3, [], [], 3, 6, 7]
notemptylist = []

for i in emptylist:
    if i != []:
        notemptylist.append(i)
print(notemptylist)

# 10. Write a Python program to clone or copy a list

list_og = [1,2,3,4]
list_clone = list_og[:]
print(list_clone)

# 11. Write a python program to count the number of occurrences in a list

anotherlist = [1,2,1,3,2,1,1,3,]
from collections import Counter
Counter(anotherlist)
