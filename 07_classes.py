# CREATING CLASS
# CLASS: blueprint for creating new object
# OBJECT: instance of a class
# Example- Class: Human; Object: Atul, Sima, etc;

# naming convention: PascalCase
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))  # check if point is instance of point class


# CONSTRUCTOR
# self is reference to current object
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # this will not work because it does not know from where to get x and y
    # it needs reference to an object of class Coordinate
    # therefore self is required
    # def draw():
    #     print(f"({x}, {y})")

    def draw(self):
        print(f"({self.x}, {self.y})")


point = Coordinate(1, 2)
point.draw()


# CLASS vs INSTANCE ATTRIBUTES
# classes and attributes in PYTHON are dynamic and hence not required to define at one go

# class level attributes are visible to all instance of class known as objects
# if class level attributes value are changed then it is visible to all objects
class BlackBox:
    default_color = "Purple"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name: {self.name}\nAge: {self.age}")


human = BlackBox("Atul", 25)
human.get_details()

print(f"Color: {human.default_color}")
print(BlackBox.default_color)

BlackBox.default_color = "Green"
print(f"Color: {human.default_color}")
print(BlackBox.default_color)


# CLASS METHOD vs INSTANCE METHOD
class NewPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # decorator
    def zero(cls):  # cls is short for class method optional but for clarity
        return cls(0, 0)

    def draw(self):
        print(f"({self.x}, {self.y})")

    # override default __str__ method to print like (x, y) in place of
    # <__main__.NewPoint object at 0x000001FA65A56CF0>
    def __str__(self):
        return f"({self.x}, {self.y})"

    # override default equality __eq__ method
    def __eq__(self, other):
        return (other.x == self.x and other.y == self.y)

    # override graterthan __gt__ method
    def __gt__(self, other):
        return (self.x > other.x and self.y > other.y)
    # performinh arithmetic operations

    def __add__(self, other):
        return NewPoint(self.x + other.x, self.y+other.y)

    # COMPARING OBJECTS
point = NewPoint.zero()
point.draw()
print(point)

point2 = NewPoint(1, 2)
point3 = NewPoint(3, 6)

print(point > point2)
print(point2 > point)
print(point3 + point2)


# making custom containers
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def increment(self, tag):
        tag = tag.lower()  # consider for case sensitivity
        self.__tags[tag] = self.__tags.get(tag, 0) + 1

    # for print(cloud["atul"]) to work
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), None)

    # for cloud["atul"] = 4 to work
    def __setitem__(self, key, value):
        self.__tags[key] = value

    # for print(TagCloud) to work
    def __str__(self):
        return "\n".join([f"{key}: {value}" for key, value in self.__tags.items()])

    # for print(len(TagCloud)) to work
    def __len__(self):
        return len(self.__tags)

    # to get iterator object for the class
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.increment("Atul")
cloud.increment("Atul")
cloud.increment("Atul")
cloud.increment("Atul")
cloud.increment("ATUL")
# print(cloud.__tags)
print(cloud["atul"])
print(cloud["Atul"])
print(cloud["ankit"])

cloud["atul"] = 420
cloud["sima"] = 840
print(cloud)
print(len(cloud))


# private members: prefix them with double underscore(__)
# NOTE: there is no such thing as private memeber in python
# trick: if you want to rename any word fimly click on any one occurance of work and press F2 and update the value
# print(cloud.__tags["atul"])
# how to access private member
print(cloud.__dict__)  # bydefault everything in class are stored as dictionary
# we (can see the structure and content using object.__dict__ like this : '_TagCloud__tags'
# OUTPUT: {'atul': 420, 'sima': 840} although we tried to keep private
print(cloud._TagCloud__tags)


# PROPERTIES: althought below is correct implementation but not utilizing python full potential
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if (value < 0):
            raise ValueError("Price of product can't be negative")
        self.__price = value


try:
    product = Product(-1)
except ValueError:
    print("ValueError")


# PYTHONIC WAY: but make it private
class Product2:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if (price < 0):
            raise ValueError("Price of product can't be negative")
        self.__price = price

    price = property(get_price, set_price)


mango = Product2(100)
print(mango.price)
mango.price = 55
print(mango.price)
try:
    mango.price = -4
except ValueError:
    print("ValueErrror")


# using decorator
# if in decorator we dont have setter then it will become read-only object
class Product3:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if (price < 0):
            raise ValueError("Price of product can't be negative")
        self.__price = price


product = Product3(400)
product.price = 123
print(product.price)
try:
    product.price = -5
except ValueError:
    print("ValueError")
print(product.price)


# make class read only
class Product4:
    def __init__(self, price):
        self.__price = price  # since setter is not present so use __price to set price

    @property
    def price(self):
        return self.__price


product = Product4(100)
print(product.price)
try:
    product.price = 420
except AttributeError:
    print("AttributeError")
