# -- section 1
#    Python can be used in
#        Data Analysis
#        AI/ML
#        Automation
#        Web Apps
#        Mobile Apps
#        Desktop Apps
#        Testing
#        Hacking


# print something
import math
print("Hello, World!")
print("*" * 10)

# install linter named pylint extension for easy formatting, autocomplete, debuging and testing

# Python Enhancement Proposals(PEPs)

x = 1

y = 2

unit_price = 3

# variables
students_count = 56
rating = 4.99
is_published = True
course_name = "Python Programming"
# python is case sensitive language
# snake case is prefered in python
# small case is prefered

# string
# using quotes double or single
# tripple qoutes is used to format message
message = """
Hi! Atul,

This is real atul speaking to imaginary atul.

Regards
Atul
"""
print(message)

# to get length of string
str_len = len(course_name)
print(str_len)

print(course_name[0])  # first char of string
print(course_name[-1])  # first char from last
# course_name[a:b] a and b both are optional and if not provided then it will start from or end with end of string
# b is not included so beware of it
print(course_name[:])
print(course_name[1:])
print(course_name[:-2])
print(course_name[1:3])

# escape sequence [\", \', \\, \n"]
course = 'atul\'s course'
print(course)

first = '  atul'
last = 'prakash'

print(first + " " + last)
full = f"{first} {last}"
print(full)

# inside {} any expression can be done
full = f"{first} {2+9}"
print(full)

# use dot to see methods which can be applied on that variable
full.upper()  # it will not affect original string and work and return copy
print(full)
print(full.upper())
print(full.lower())
print(full.title())
print(full.strip())
print(full.rstrip())
print(full.replace('tul', 'nkit'))
print(full.find('tu'))  # index return value -1 or index
print('py' in course)  # boolean return value
print('py' not in course)  # boolean return value


# numbers
x = 1       # integer
x = 1.1     # decimal
x = 1 + 2j  # complex number [a + bi]

# operator: [+, -, /, //, *, %, **]
# x += 3 [in place of + any operator can be used from above]

print(round(2.9))
print(abs(5-9))
print(abs(9-5))

# for others import math and use it
print(math.ceil(2.2))

# type conversion
# input from user are always in string so safely convert into desired format before using it
# int(x) | float(x) | bool(x) | str(x)
x = input("x: ")
print(type(x))  # see yourself that it is default string
x = int(input("x: "))
y = x + 1
print(x)
print(y)
print(f"x: {x}, y: {y}")  # example of formatted string

# falsy value: ["", 0, None]
