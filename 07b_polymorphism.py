from collections import namedtuple
from abc import ABC, abstractmethod

print("\tseg 1")


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# this function will change its behaviour based on given type
def draw(control):
    control.draw()


draw(TextBox())
draw(DropDownList())

print("\tSeg 2")


def check(controls):
    for control in controls:
        control.draw()


check([TextBox(), DropDownList()])


# Duck Typing: in python it is not necessarary to inherit from UIControl and it will strill work because of dynamic type nature of python
# thus we haven't specified in check() argumets that it of TYPE UIControl and thus if every type passed contains draw() it will work


print("\tseg 3")
# extending built-in-class


class Text(str):
    def duplicate(self):
        return self + self


text = Text.duplicate("Python")
print(text)
print(text.upper())  # text method has all methods of string class


class TrackableList(list):
    def append(self, object):
        # just to visualize that append of list is extended by printing
        print("Append called")
        super().append(object)


tmp = TrackableList()
tmp.append("1")
print(tmp)


print("\tseg 4")
# DATA classes


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)


p1 = Point(1, 2)
p2 = Point(3, 8)
p3 = Point(3, 8)
print(id(p1))
print(id(p2))
print(p1 == p2)
print(p3 == p2)


print("\tseg 5")
# note that just to store data and compare we are supposed to do this many things
# to avoid this use namedtuple (it is immutable)
# from collections import namedtuple
# ClassName = namedtuple("ClassName", ["variable_one", "variable_two", ...])1
Point = namedtuple("Point", ["x", "y"])
p3 = Point(3, 8)
p2 = Point(3, 8)
p1 = Point(1, 2)
print(p1 == p2)
print(p3 == p2)
