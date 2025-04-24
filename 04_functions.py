# functions
def greet():
    print("hi there")
    print("Welcome abroad")


greet()

# paramenter is input that we define for our function
# arguments is actual value of parameter


def welcome(first_name, last_name):
    print(f"hi {first_name} {last_name}, welcome to India!")


welcome("Atul", "Prakash")


def onboard(first_name, last_name):
    return f"hi, {first_name} {last_name}! You are onboarded. Enjoy!"


print(onboard("Atul", "Prakash"))

# in python all function bydefault return None value
print(greet())

# Types of functions: one that carries out the task, another that return the value
# if not explicitly returning anything then it is carrying out the task


# Keyword Arguments (Used for clarity)
def increment(number, by):
    return number + by


print(increment(5, by=2))  # by=2 is keyword arguments for clarity


# default arguments
def multiply(number, another, times=1):
    while times:
        number *= another
        times -= 1
        return number


print(multiply(5, 3, 3))


# xargs: any number of arguments
def multiply_all(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


print(multiply_all(2, 3, 4, 5, 6, 7))


# xxargs: ** is used and key:value pair aka dictionary is passed and treated
def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=6, name="Atul", age="24")


# scope of variable
# local and global variable
# to change global variable through function
message = "a"


def change_global(name):
    global message
    message = name


change_global("Sima")
print(message)

# DEBUGGING
# f5 to execute till breakpoint
# f10 to step into breakpoint segment
# f11 to step into a function and execute line by line
# shift + f11 to step out of a function
# to comment few lines select those line and press CTRL+/

# EXERCISE: if divisible by
# 3: fizz
# 5: buzz
# 3 & 5: fizzbuzz
# other: other


def fizz_buzz(number):
    if number <= 0:
        return number
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return number


print(fizz_buzz(6))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(0))
print(fizz_buzz(17))
