# INHERITANCE
from abc import ABC, abstractmethod


class Mammal:
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")


class Fish:
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")


# DRY: don't repeat yourself
class Animal:
    def __init__(self, age=1):
        print("Animal Constructor")
        self.age = age

    def eat(self):
        print("eat")


# dog inherits animal class features
# Animal: Parent/base class
# Dog: child, sub-class
class Pet(Animal):
    def walk(self):
        print("walk")


d = Pet()
d.eat()
print(d.age)
print(isinstance(d, Animal))
print(isinstance(d, Pet))
# every class in python inherits base class as object class
print(isinstance(d, object))
print(f"Pet is subclass of Animal: {issubclass(Pet, Animal)}")
print(f"Animal is subclass of Pet: {issubclass(Animal, Pet)}")


# Method Overriding
class Bird(Animal):
    # it will replace Animal constructor to this constructor
    def __init__(self, weight=1):
        self.weight = weight

    def fly(self):
        print("fly")


crow = Bird()
# print(crow.age)  # AttributeError: 'Bird' object has no attribute 'age'


# SEQUENCE OF CONSTRUCTOR CAN BE CHANGED BY CHANGING SUPER() LINE BEFORE OR AFTER
class Cow(Animal):
    def __init__(self, age=1, weight=1):
        super().__init__(age)
        print("Cow Constructor")
        self.weight = 15

    def eat(self):
        print("eat")


cow = Cow()


# MULTIPLE INHERITANCE
class Student:
    def greet(self):
        print("greet(): Student")


class Department():
    def greet(self):
        print("greet(): Department")


class Mca(Student, Department):
    pass


mca = Mca()
mca.greet()  # greet(): Student | because Student was written first in inheritance list


class Btech_cse(Department, Student):
    pass


btech = Btech_cse()
btech.greet()  # greet(): Department | because Department was written first in inheritance


# GOOD EXAMPLE OF INHERITANCE
class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


# ANOTHER GOOD EXAMPLE: READING DATA FROM STREAM

# by convention all error should end with error name
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


# ABSTRACT CLASS
# since we are using Stream class only for extracting out common functionality and its actual instance is not valid
# therefore making it abstract would suffice it
# from abc import ABC, abstractmethod
# abc: abstract base class

# if a class derrived form abstaract class, it should define all abstract method otherwise it will also be considered as abstract class
class MemoryStream(Stream):
    pass


# ms = MemoryStream() # it is abstract and can't be instantiated


class MessageStream(Stream):
    def read(self):
        print("Reading data from memory stream")


ms = MessageStream()
