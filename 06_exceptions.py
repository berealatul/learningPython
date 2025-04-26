from timeit import timeit
number = [1, 2]
try:
    print(number[3])
except IndexError:
    print("Wrong Index Value")

age = 0
while True:
    try:
        age = int(input("AGE: "))
        break
    except ValueError:
        print("AGE IS NOT VALID")
print(age)

while True:
    try:
        age = int(input("AGE: "))
    except ValueError:
        print("AGE IS NOT VALID")
    else:
        break

print(age)

try:
    age = int(input("AGE: "))
except ValueError as ex:
    print(ex)
else:
    print("GOOD WORK")

xfactor = 0
try:
    age = int(input("AGE: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("WRONG INPUT")
else:
    print("GOOD WORK")

print(xfactor)

try:
    file = open("01_intro.py")
    age = int(input("AGE: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("WRONG INPUT")
else:
    print("GOOD WORK")
finally:
    # finally clause is always executed
    file.close()

# WITH STATEMENT: wheather finally is there or not it will close files opened with "with" clause
# if a function support context management or variableName.__enter__ or variableName.__exit__
try:
    with open("01_intro.py") as file:
        print("file opened")
    age = int(input("AGE: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("WRONG INPUT")
else:
    print("GOOD WORK")

# RAISING EXCEPTION


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age must be greater or equal to zero")
    return 10/age


# from timeit import timeit
code = """
def calculate_factor(age):
    if age <= 0:
        raise ValueError("Age must be greater or equal to zero")
    return 10/age
try:
    calculate_factor(-1)
except ValueError as error:
    pass  # to ignore exception
"""
print("first", timeit(code, number=10000))

code2 = """
def calculate_factor(age):
    if age <= 0:
        return None
    return 10/age
xfactor = calculate_factor(-1)
if xfactor == None:
    pass
"""
print("second", timeit(code2, number=10000))

# hence don't use exceptions raise unwanted since it is time taking operation
