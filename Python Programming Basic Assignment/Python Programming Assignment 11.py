print('1. Write the python Program to find words which are greater than given length k\n')

names = ['kenny', 'aditi', 'lakshmi', 'deepthi', 'rahul']
k = 5


def k_list(k):
    k_names = []
    for i in names:
        if len(i) > k:
            k_names.append(i)
    return k_names


print(f'List of names with length greater than {k} = {k_list(k)}\n')

print('2. Write the python Program for removing ith character from the string\n')

name = 'aditi_goyal'
i = 8
print(f'When {i}th character is removed from the string "{name}", it becomes "{name.replace(name[i], "")}"\n')

# 3. Write a Python Program to split and join a string
name = 'kenny_d_aditi_g'
seperator = '_'
split_name = name.split(seperator)
new_name = ''.join(split_name)

print(f'When name {name} is split by {seperator}, it becomes {split_name}\n')
print(f'When we join the split name, we get {new_name}')

# 4. Write a Python program to find if given string is binary or not

test_string = '10101201'
flag = True
for i in test_string:
    if i in ['1', '0']:
        continue
    else:
        flag = False
        print(f'{test_string} is not a binary string')
        break
if (flag):
    print(f'{test_string} is a binary string')

# 5. Write a Python Program to find uncommon words from two strings

str1 = 'My name is Kenny'
str2 = 'My name is Aditi'
lst1 = str1.split(' ')
lst2 = str2.split(' ')
lst3 = []
for i in lst1:
    if i not in lst2:
        lst3.append(i)
for j in lst2:
    if j not in lst1:
        lst3.append(j)
print(lst3)

# 6. Write a Python Program to find the duplicate characters in a string

newstr = 'This duplicate is not a duplicate'
duplicates = []

for i in newstr:
    if newstr.count(i)>1:
        if i not in duplicates:
            duplicates.append(i)
dupstr = ' '.join(duplicates)
print(dupstr)

# 6.1 Write a Python Program to find the duplicate words in a string
newstr = 'This duplicate is not a duplicate'

def duplicate_finder(newstr):
    newlst = newstr.split(' ')
    duplst = []
    for i in newlst:
        if newlst.count(i) > 1:
            if i not in duplst:
                duplst.append(i)
    print(duplst)

duplicate_finder('aditi goyal goyal')

# 7. Write a Python Program to check if the string contains any special character

thestrng = 'K@nny$'

special_characters = ['$','!','@','#','%','&']

for i in thestrng:
    if i in special_characters:
        print(f"This string {thestrng} contains {i} which is a special character")