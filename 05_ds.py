# list
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque
letters = ["a", "b", "c"]  # 1-d array
matrix = [[0, 1], [2, 3]]  # 2-d array
zeros = [0] * 10  # 1-d array containing 10 zeros
combined = zeros + letters
print(combined)  # OUTPUT: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'a', 'b', 'c']

# any iterable items given to list, it will make it array containing those
series = list(range(20))
print(series)
series = list("ATULPRAKASH")
print(series)
print(len(series))
series[-1] = '8'
# return every nth element from array array[::n]
print(series[::2])
# return array in reverse order without modifying original array
print(series[::-1])

# list unpaacking
numbers = [1, 2, 3]
first, second, third = numbers  # number of elements on both side must be same
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
first, second, *others = numbers  # keep rest in others array
print(others)
first, *others, last = numbers  # keep rest in others array
print(others)

# looping over list
for number in numbers:
    print(number)

for number in enumerate(numbers):
    print(number)  # tuple (index, value)

# list unpacking [it will also work for tuples]
for index, letter in enumerate(numbers):
    print(letter)

# adding or removing items
letters = ['a', 'b', 'c', 'd']
# add
letters.append('e')
print(letters)

# remove from end of list
letters.pop()
print(letters)

letters.pop(2)  # remove element at particular index
print(letters)

letters.append('z')
letters.append('z')
letters.append('z')
letters.remove('z')  # only remove first occurance from list
print(letters)

# to delete range of items
del letters[0:3]
print(letters)


# finding items
letters = ['a', 'b', 'c', 'd']
# it will generate ValueError if we pass an element not in array
print(letters.index("d"))
# to resolve value error, first check if that element is present or not
if 'd' in letters:
    print(letters.index('d'))

print(letters.count('q'))  # return the count of given element

# sorting lists
numbers = [3, 51, 2, 8, 99]
numbers.sort()
numbers.sort(reverse=True)
print(numbers)
numbers = sorted(numbers)
print(numbers)

items = [
    ("P1", 6),
    ("P2", 89),
    ("P3", 12)
]


items.sort()  # it will not work because it is ambigious that how to sort items
print(items)


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# lambda functions
# SYNTAX: lambda parameters:expression
items = [
    ("P1", 6),
    ("P2", 89),
    ("P3", 12)
]
items.sort(key=lambda item: item[1])
print(items)


# map function: return iterable
items = [
    ("P1", 6),
    ("P2", 89),
    ("P3", 12)
]

prices = []
for item in items:
    prices.append(item[1])
print(prices)

x = map(lambda item: item[1], items)
print(x)  # sincle map returns iterable
for item in x:
    print(item)

prices = list(map(lambda item: item[1], items))
print(prices)

# filter function: returns iterable
# naieve approach: loop over list and select items satisfying given contition

print(filter(lambda item: item[1] >= 10, items))
print(list(filter(lambda item: item[1] >= 10, items)))


# list comprehension
# prices = list(map(lambda item: item[1], items))
# earlier line can be achieved by this
new_prices = [item[1] for item in items]
print(new_prices)

# print(list(filter(lambda item: item[1] >= 10, items)))
print([item for item in items if item[1] > 10])

# zip function: returns iterable
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8]
print(list(zip(list1, list2)))  # [(1, 2), (3, 4), (5, 6), (7, 8)]
# [(1, 2, 'a'), (3, 4, 'b'), (5, 6, 'c'), (7, 8, 'd')]
print(list(zip(list1, list2, "abcde")))

# stacks: use list to build stack
mystack = []
# to push
mystack.append(1)
mystack.append(2)
mystack.append(3)
# to pop
mystack.pop()
# to see top of stack
print(mystack[-1])
# is stack empty
if not mystack:
    print("Empty")


# QUEUE: use deque form collections
queue = deque([])  # wrap list in deque
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # to remove from front
queue.popleft()  # to remove from front
queue.popleft()  # to remove from front
print(queue)
if queue:
    print(queue[0])  # to see top without InexError
# to check if queue is empty or not
if not queue:
    print("empty")

# TUPLES: it is read-only
# used when accidental error are to be avoided
# syntax: variableName = (a, b, c, ...) OR variableName = a,b,c,...
point = 1, 2
print(type(point))  # <class 'tuple'>
# empty tuple
point = ()
# concatanate tuples
point = (1, 2) + (3, 4)
print(point)

# repeat same pattern n times or multiply tuple
point = (1, 2)*5
print(point)

# list to tuple
letters = tuple("ATUL")  # string to tuple
print(letters)
letters = tuple([1, 2, 3, 4, 5])  # list to tuple
print(letters)
print(letters[0:3])  # access particular segment of tuple
a, b, *c = letters  # unpack tuples
print(c)

if 4 in letters:
    print("exists")

# swapping values
x = 10
y = 11
print("x: ", x)
print("y: ", y)
z = x
x = y
y = z
print("x: ",  x)
print("y: ",  y)

x, y = y, x
print("x: ",  x)
print("y: ",  y)

# don't solve a problem that doesn't exist
# ARRAY: this is useful if element is over 10000
# array("type_code", [elements...]) where typecode is for type of data
data = array("i", [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 5, 6, 5, 99, 51,
             21, 49, 64, 651, 31, 24, 2, 2, 51,])
print(data)
# data[0] = 1.2 # it will raise TypeError as it is not integer

# SETS: {a,b,c,...} aka curly brackets are used and duplicate are removed
# data = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 5, 6, 5, 99, 51,
#         21, 49, 64, 651, 31, 24, 2, 2, 51, 52]
uniques = set(data)
print(uniques)
second = {1, 4}
print(second)
second.add(5)
print(second)
second.remove(1)
print(second)
print(len(second))

first = set([1, 2, 3, 4, 5])
second = set([5, 6, 7, 8, 9])
print(first | second)  # UNION
print(first & second)  # INTERSECTION
print(first - second)  # DIFFERENCE
print(first ^ second)  # SYMMETRIC DIFFERENCE (either in first or second)
# set items does not support indexing ie first[0] is not valid

# DICTIONARIES
point = {"x": 1, "y": 2}
point2 = dict(x=1, y=2)
print(point)
print(point2)
# print(point2["n"])
# if key being searched for is not found then KeyError will be generated, to prevent it use
if "x" in point:
    print(point["x"])

# if key is not then return 0 or any desired number as default
print(point.get("n", 0))

# loop extracts key only in this format
for key in point:
    print(key, point[key])

# loop extracts key value as tuple in this format
for key in point.items():
    print(key)
# since tuple we an extract this information like key value pair
for key, value in point.items():
    print(key, value)

# to delete an item in dictionary
del point['x']

# DICTIONARY COMPREHENSION
values = []
for x in range(5):
    values.append(x * 2)
print(values)

# [expression for item in items]
data = [x * 2 for x in range(5)]
print(data)
data = {x * 2 for x in range(5)}
print(data)
data = {x: x * 2 for x in range(5)}
print(data)


# GENERATOR EXPRESSION
# these are iterable and on each iteration it spit out the new value
# it doesn't store the value
# small bracket is used
# it is used when data set is too big or infinite stream of data is there
values = (x*2 for x in range(1))
print(values)
for x in values:
    print(x)

# from sys import getsizeof
values = (x*2 for x in range(123456789))
print("gen: ", getsizeof(values))
values = [x*2 for x in range(100)]
print("gen: ", getsizeof(values))


# unpacking operators: we can unpack any iterable using * before that iterable
numbers = [1, 2, 3]
print(numbers)
print(1, 2, 3)
print(*numbers)

letters = [*"PRAKASH"]
print(letters)
numbers = [*range(5)]
print(numbers)

print([*first, "z", *"ATULPRAKASH", *numbers])

first = {"x": 1}
second = dict(x=6, z=18)
# if more than one key is present then last value of that key will be kept
combined = {**first, **second, "q": 789}

print(combined)

# EXERCISE: find the most repeated character in the text
# from pprint import pprint
sentence = "This is a common interview question"
data = {}
for c in sentence:
    if c in data:
        data[c] += 1
    else:
        data[c] = 1
pprint(data, width=1)

data = sorted(data.items(), key=lambda kv: kv[1], reverse=True)
print(data[0])
