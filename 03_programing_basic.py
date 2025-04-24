# comparision operator
# [>, >=, <, <=, ==]
print(10 == '10')  # false because of different type

print(ord('b'))
print(ord('B'))
print("bag" > "apple")
print("bag" == "BAG")

# conditional statements
# indented part are part of condition given
temp = 35
if temp > 30:
    print("drink water")
    print("it is warm")
elif temp > 35:
    print("have SPF")
else:
    print("Sit inside, way to hot to handle")
print("condition exited")

# ternary operator
age = 22
# WAY 1
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# WAY 2
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)

# WAY 3: TERNARY OPERATOR
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# logical operator [AND, OR]
high_income = True
good_credit = True

if high_income and good_credit:
    print("eligible for loan")
else:
    print("Not eligible")

if high_income or good_credit:
    print("eligible for loan")
else:
    print("Not eligible")

student = True
if not student:
    print("eligible")
else:
    print("not eligible")

if not student and (high_income or good_credit):
    print("eligible")
else:
    print("NOT")
    # in python logical operato are short circuit evaluation

# chaining comparision operator
# age should be between 18 and 65
age = int(input("age: "))
# if age >= 18 and age < 65:
if 18 <= age < 65:  # earlier line and this is same
    print("SAB LEGAL HAI")
else:
    print("BHAG CHUZZA KAHI KA")

# for loop
for number in range(3):
    print("Attempt:", number + 1)

# first is start from and second is end before
for number in range(1, 4):
    print("Attempt:", number)

# third argument is step factor that is increment by
for number in range(1, 4, 2):
    print("Attempt:", number)

# if loop does not terminate early then else only else will execute
number = 420
for x in range(3):
    print("Attempt", x + 1)
    num = int(input("Enter Your Guess: "))
    if num == number:
        print("Chor kahi ka dekh liya na")
else:
    print("alsi kahi ka itna bhi nahi hota hai kya")


# Nested loop
for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")

# Iterables
for x in "python":
    print(x)

for x in [1, 2, 3, 4, 5]:
    print(x)

# while loop
number = 100
while number > 0:
    print(number)
    number //= 10

command = ""
while (command.lower() != "quit"):
    command = input(">")
    print("ECHO", command)

# infinite loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# EXERCISE: print even number between 1 to 10 and print count of even numbers
count = 0
for num in range(1, 10):
    if not (num % 2):
        print(num)
        count += 1
print(f"We have {count} even numbers")
