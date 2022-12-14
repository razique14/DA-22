# -*- coding: utf-8 -*-
"""OOPS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ktDzjF3frI7g-YirlOY3wiW2s8qJSIxr
"""

a  ='python'
print(type(a))

"""Object oriented progamming System(OOPS)

Object oriented programming is a programming paradigm based on the concepts of 'Objects' which can contain data, in the form of fields(often known as attributes or properties) and the code in the form of procedures/functions(known as methods).

An object has two characteristics:

attributes or properties or state
behaviour or functionality or action
Let's take an example:

A Human is an object, as it has the following properties:

name, weight, height as attributes
walking, running, dancing as behavior

The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

In Python, the concept of OOP follows some basic principles:

Class :
A class is a blueprint for the object.
"""

# Naming convention: Class name should be capitalised
class Human:
 pass

"""Object :

All real world entities are called as 'Object'. Ex: car, bus, pen etc.


An object (instance) is an instantiation of a class containing variables or methods. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.
"""

obj = Human()
# obj2 = Human()
obj

obj.height = 5
obj.weight = 60

# print(obj.height)
print(obj.weight)

def dummy(a):
  return f'{a} is a hero'

dummy('superman')

class Human:
  s = 4
  def dummy(a):
   return f'{a} is a hero'

obj1 = Human()

# obj1.s
obj1.dummy

class Human:
  # Class Attribute
  name = 'razique'

  def walking(self):
    # self is an implicit instance/ implicit reference, it always points to the current object
    # self is like a parameter to a function, acts like a catylyst and calls the object.
    # self must be first parameter
    # print('Ironman is walking')
    print(f'{self.name} is walking')
  
  def running(self):
    print(f'{self.name} is running')

a = Human()
# a.name
# a.walking()
a.running()

class Human:
  # Class Attribute
  name = 'Ironman'

  def __init__(self,name,age,weight,height):
    self.name = name
    self.age = age
    self.height = height
    self.weight=weight
    print(f'Hi {self.name}, my age is {self.age}. my height is {self.height} and my weight is {self.weight}')

  def walking(self):
    print(f'{self.name} is walking')
  
  def running(self):
    print(f'{self.name} is running')

a = Human('razique',25,64,5.7)
a.walking()
a.running()
# a.age 
# a.height = 3

a = Human('Spiderman',21,45,6)
#alternative way of calling class methods
# Human.walking(a) #this is why we need self
# a.walking()

class Human:
  # Class Attribute
  name = 'Ironman'

  def __init__(self,name,age,weight,height):
    # Instance variables/Attributes
    self.name = name
    self.age = age
    self.height = height
    self.weight=weight
    # print(f'Hi {self.name}, my age is {self.age}. my height is {self.height} and my weight is {self.weight}')

  def walking(self):
    # print(f'{self.name} is walking')
    print(f'Hi {self.name}, my age is {self.age}. my height is {self.height} and my weight is {self.weight}')

  
  def running(self):
    print(f'{self.name} is running')

# a = Human('Spiderman',21,45,6)
# a.name
# a.name = 'Akhil'
a.walking()





class car:
  name='ford'
  def __init__(self,name,engine,seats,colour):
    self.name = name
    self.engine = engine
    self.seats = seats
    self.colour= colour
    print(f' {self.name} its engine is {self.engine} it has seats {self.seats} and its color is {self.colour}')

a = car('ford','electric',5,'white')

#this is called object initiation

class rectangle:
  name = 'ABCD'
  def __init__(self,area):
    a = int(input('enter length of rectangle'))
    b = int(input('enter breadth of rectangle '))
    area=a*b
    self.area=area
    def Area(self):
      print(f'area of rectangle is {self.area}')

rec = rectangle('area')

rec.area()

class Rectangle:
  name = 'Rectangle'
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth

  def Area(self):
    print(f'Area of rectangle is {self.length * self.breadth}')

rec  = Rectangle(5,4)

rec.Area()

"""Properties of OOPS :

1.Inheritance

2.Polymorphism

3.Encapuslation

4.Abstraction

Inheritance:

1.Single level
"""

# Inheritance
# 1. Single  level

class Parent:
  a = 2
  b = 3
  def pfun(self):
    print('I am a parent class/Base class method')

class Child(Parent):
  c = 5
  d = 6
  def cfun(self):
    print('I am Child class/Sub class/Derived class')

class Parent:
  a = 2
  b = 3
  def pfun(self):
    print('')

# create a method print job roles?
class Employee:
  def details(self):
    print('i am an employee')

class Programmer(Employee):
  def details(self):
    print('i am a programmer')

obj = Employee()
obj.details()

obj = Programmer()
obj.details()

"""2. Multi-level Inheritance"""

class GrandParent:
  a = 2
  b = 3
  def gfun(self):
    print('I am a grand parent class/Base class method')

class Parent(GrandParent):
  c = 6
  d = 5
  def pfun(self):
    print('I am a parent class/Base class method')

class Child(Parent):
  e = 8
  f = 9
  def cfun(self):
    print('I am Child class/Sub class/Derived class')

gobj = GrandParent()
# gobj.a
gobj.b

pobj = Parent()
pobj.a
# pobj.b
# pobj.pfun()

# create a class called person then create a class attribute called 'India'.Create a class called citizenship

class Person:
    country = 'India'
    def citizenship(self):
      print(f'i am a citizen of {self.country}')

class Student(Person):
  state = 'Andhra pradesh'
  salary = 0
  def __init__(self,state,salary):
    self.salary = salary
    self.state = state
  def getstate(self):
    print(f'my state  is {self.state} and my salary is {self.salary} INR')

obj  = Person()
obj.citizenship()

obj = Student('bihar',200000)
obj.getstate()

class Person:
    country = "India"
    def citizenship(self):
        print(f"I am a citizen of {self.country}")

class Student(Person):
  state = 'Andhra pradesh'
  salary = 0
  def __init__(self,state,salary):
    self.salary = salary
    self.state = state
  def getstate(self):
    print(f'my state  is {self.state} and my salary is {self.salary} INR')

class Programmer(Student):
  state = 'Bihar'
  salary = 100
  def __init__(self,state,salary):
    self.salary = salary
    self.state = state
  def getstate(self):
    print(f'my state  is {self.state} and my salary is {self.salary} INR')

obj = Student('kerala',65)
obj.getstate()

raz = Programmer('bihar', 442443)
raz.getstate()



"""3. Hierarchical Inheritance"""

class Parent:
  a = 2
  b = 3
  def pfun(self):
    print('i am a parent class/base class method')

class Daughter(Parent):
  c = 5
  d = 6
  def dfun(self):
    print('i am a child class/sub class')

class Son(Parent):
  e = 8
  f = 9
  def sfun(self):
    print('i am a child class/sub class')

obj = Parent()
# obj.pfun()
obj.a
obj.b

obj = Daughter()
# obj.dfun()
obj.c
obj.d

obj = Son()
# obj.sfun()
obj.e
obj.f

"""4. Multiple Inheritance"""

class Father:
  a = 2
  b = 3
  def ffun(self):
    print('I am a parent class/Base class method')

class Mother:
  c = 6
  d = 5
  def mfun(self):
    print('I am a parent class/Base class method')

class Child(Father,Mother):
  e = 8
  f = 9
  def cfun(self):
    print('I am Child class/Sub class/Derived class')

obj = Father()
# obj.ffun()
# obj.a
obj.b

obj = Mother()
# obj.mfun()
# obj.c
obj.d

obj = Child()
# obj.cfun()
# obj.e
obj.f

class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):    
    print(f'the area of rectangle is {self.length*self.breadth}')
  def perimeter(self):
    print(f'the perimeter of rectangle is {2*(self.length+self.breadth)}')

obj1 = Rectangle(5,3)
# obj1.area()
obj1.perimeter()

class Square:
  def __init__(self,length):
    self.length=length
  def area(self):
    print(f'the area of square{(self.length)*(self.length)}')
  def perimeter(self):
    print(f'the of square is {4*(self.length)}')

obj2 = Square(8)
# obj2.area()
obj2.perimeter()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle): 
    def __init__(self, length):
        super().__init__(length,length)

    
class Cube(Square):
  def area(self):
    return 6*super().area()
  
  def volume(self):
    return super().area()*self.length

s1 = Square(6)
s1.area()



class Cube:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 6*self.length*self.length

    def perimeter(self):
        return 12* self.length

    def volume(self):
        return self.length**3

obj = Cube(5)
obj.area()
obj.perimeter()
obj.volume()





"""2. Poly-morphism

many forms

1. Overloading(Compile time)

2. Over riding(run time)
"""

class Polygon:
  a =10
  def area(self,a,b,c):
    return a*b*c

p1 = Polygon()
p1.area(4,6,3)

# Over Loading
class Dog:
  def sound(self):
    print('bow')

class Cat:
  def sound(self):
    print('meow')

def makesound(animal): 
     return animal.sound()

# cat  = Cat()
# makesound(cat)
dog  = Dog()
makesound(dog)

"""Over-riding"""

# Variable overriding
class Man:
  name = 'parwez'
class Men(Man):
  name = 'razique'

m = Men()
print(m.name)

class Bike1:
  def Gears(self):
    return 3
class Bike2(Bike1):
  def Gears(self):
    return 4

b = Bike1()
print(b.Gears())

"""Decorators


Python has an interesting feature called decorators to add functionality to an existing code.

This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.
"""

def first(msg):
  print(msg)
first('hello')

def first(msg):
  print(msg)
# first('hello')
sec = first
sec('hey')

def first():
  print('hi')

def second(fun):
  fun()
  print('Hello')
  fun()

second(first)

def first():
  print('*****************')

def second(fun):
  fun()
  print('Hello')
  fun()

second(first)

"""So what are closures good for?

Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solution. But when the number of attributes and methods get larger, it's better to implement a class.

Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.
"""

def multiplier1(a):
  # print('1')
  def multiplier2(b):
    # print('3')
    return a*b
  # print('2')
  return multiplier2

# mul = multiplier1(2)
# mul(3)
# multiplier1(2)(3)
 
mul1 = multiplier1(5)
mul2 = multiplier1(6)
mul2(mul1(7))

def decorate_it(fun):
  def wrapper():
    print('***********************')
    fun()
    print('***********************')
  return wrapper

@decorate_it
def hello():
  print('hello world')

hello()

# decorate_it(hello)()

# hey = decorate_it(hello)
# hey()

def star(fun):
  def wrapper():
    print('***********************')
    fun()
    print('***********************')
  return wrapper

def hash(fun):
  def wrapper():
    print('########################')
    fun()
    print('########################')
  return wrapper

@star
@hash
def hello():
  print('hello world')

hello()



"""Absraction:

In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity. It also enhances the application efficiency.

Hide Implementation details, returns using call backs

ABSTRACT CLASS : If it has one or more abstract methods

ABSTRACT METHOD : Only declaration, but no Definition

CONCRETE CLASS : If it doesnt have abstract class

CONCRETE METHOD : If it has both definition and declaration

Object cannot be instantiated for abstract class

Object can only be instantiated by concrete class
"""

# Importing ABC class and abstract method from abc module
from abc import ABC,abstractmethod 
class A(ABC): #Abstract class
  @abstractmethod
  def display(self): #abstract method
    return None

class Demo(A): #concrete class
  def display(self): #concrete method
     print('I am an abstract method')

c = Demo()
c.display()

class A(ABC):
  @abstractmethod
  def display(self):
    return None
  
  @abstractmethod
  def show(self):
    return None

class B(A):
  def display(self):
    return 'Display method'
 
  def show(self):
    return 'show method'

c = B()
# c.display()
# c.show()



"""Encapsulation:

Public: Accesible everywhere

Private:Accesible by that class and by inherited classes.

Protected: Only accesible by that class but not inherited classes.

Public example
"""

class Human:
  name = 'Ironman'
  def walking(self):
    print('Ironman is working')

a = Human()
# a.walking()
a.name

# Public variable example
class Avenger:
  def __init__(self, name, color):
     # public data members
     self.name = name
     self.color = color
     print(f'{self.name} is in {self.color} color ')

  def show(self):
     # accessing public data member inside the class
     print("Name: ", self.name, '; Color:', self.color)
     print(f'{self.name} is in {self.color} color ')

class Power_ranger(Avenger):
  def show2(self):
      print(f'{self.name} is in {self.color} color ')

# Accessing public data member in the inherited class
b = Power_ranger('Thor','white')
# b.show2()
# Accessible outside the class
b.name

"""Protected example

single Underscore(_)
"""

class Human:
  _name = 'Ironman'
  def __init__(self,name):
      self.name=name
  def walking(self):
    print(f'{self._name} is working')

class Human2(Human):
  def walking(self):
      print(f'{self._name} is working')

# a = Human('superman')
# a = Human2('superman')
# a.walking()

# Accessing protected data member outside the class should be restrained
a._name

"""Private example

Double Underscore(__)
"""

class Human:
  _name = 'Ironman'
  def __init__(self,name):
      self.name=name
  def walking(self):
    print(f'{self._name} is working')

class Human2(Human):
  def walking(self):
      print(f'{self._name} is working')

a = Human('superman')
# a = Human2('superman')
# a.walking()
# a.__name

a._Human__name