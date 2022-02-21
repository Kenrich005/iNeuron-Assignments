# 1.	Write a Python program to Extract Unique values dictionary values?

names = {1: 'Kenny', 2: 'Aditi', 3: 'Kenny', 4: 'Horse'}

print('The original dictionary is ', str(names))

print('The unique values in this dictionary are', sorted(set(names.values())))

# 2. Write a Python program to find sum of all items in a dictionary

scores = {'Anil': 72, 'Kohli': 45, 'Sehwag': 20, 'Dhoni': 50, 'Rishab': 30}

print('The items in dictionary are', str(scores))

print('The sum of all scores is ', sum(scores.values()))

# 3. Write a Python program to merge two dictionaries

print('Merged dictionary', str({**names, **scores}))

# 4. Write a Python program to convert key-values list into flat dictionary

icecream = ['vanilla', 23, 'strawberry', 30, 'butterscotch', 35, 'chocolate', 40]

print(dict(zip(icecream[::2], icecream[1::2])))

# 5. Write a Python program to insert at the beginning of ordered dictionary

from collections import OrderedDict

ordered_scores = OrderedDict(scores)

ordered_scores.update({'Manjeet': 30})
ordered_scores.move_to_end('Manjeet', last=False)

print(str(ordered_scores))

# 6. Write a Python Program to check the order of character in string using OrderedDict

str = 'balloon'
patrn = 'lo'

def check_order(str, patrn):
    index = 0
    for key in OrderedDict.fromkeys(str).keys():
        if key != patrn[index]:
            pass
        else:
            index = index + 1
        if index != len(patrn):
            continue
        return True
    return False

print(check_order("ballon", "lo"))

# 7. Write a Python Program to sort Python Dictionaries by Key or value

from operator import itemgetter

def sorted_dict_key(dictionary):
    return OrderedDict(sorted(scores.items()))

def sorted_dict_value(dictionary):
        return OrderedDict(sorted(scores.items(),key=itemgetter(1)))


print("Dictionary sorted by key",sorted_dict_key(scores))

print("Dictionary sorted by value", sorted_dict_value(scores))

