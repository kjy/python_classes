#!/usr/bin/env python
# coding: utf-8

# 20.1. Introduction: Classes and Objects - the Basics
# 20.1.1. Object-oriented programming
# Python is an object-oriented programming language. That means it provides features that support object-oriented programming (OOP).
# 
# Object-oriented programming has its roots in the 1960s, but it wasn’t until the mid 1980s that it became the main programming paradigm used in the creation of new software. It was developed as a way to handle the rapidly increasing size and complexity of software systems and to make it easier to modify these large and complex systems over time.
# 
# Up to now, some of the programs we have been writing use a procedural programming paradigm. In procedural programming the focus is on writing functions or procedures which operate on data. In object-oriented programming the focus is on the creation of objects which contain both data and functionality together. Usually, each object definition corresponds to some object or concept in the real world and the functions that operate on that object correspond to the ways real-world objects interact.

# 20.2. Objects Revisited
# In Python, every value is actually an object. Whether it be a dictionary, a list, or even an integer, they are all objects. Programs manipulate those objects either by performing computation with them or by asking them to perform methods. To be more specific, we say that an object has a state and a collection of methods that it can perform. (More about methods below.) The state of an object represents those things that the object knows about itself. The state is stored in instance variables. For example, as we have seen with turtle objects, each turtle has a state consisting of the turtle’s position, its color, its heading and so on. Each turtle also has the ability to go forward, backward, or turn right or left. Individual turtles are different in that even though they are all turtles, they differ in the specific values of the individual state attributes (maybe they are in a different location or have a different heading).
# 
# Simple object has state and methods.

# In[1]:


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):  # Constructor is an initializer method

        self.x = 0  # instance variable x
        self.y = 0  # isntance variable y

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print("Nothing seems to have happened with the points")


# In[2]:


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):

        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)

print(p is q)  # Notice that the 2 class instances are 2 different objects
# When you print on a class instance object, you get the memory location of object


# In[4]:


class NumberSet:
    def __init__(self, num1, num2):

        self.num1 = num1
        self.num2 = num2

t = NumberSet(6,10)  # variable assignment


# In[5]:


# Adding other Methods to a class
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


p = Point(7,6)
print(p.getX())  # Use print function on p class instance object
print(p.getY())


# In[6]:


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(7,6)
print(p.distanceFromOrigin())


# In[11]:


class Animal:
    """ Animal class. """

    def __init__(self, initArms, initLegs):

        self.arms = initArms
        self.legs = initLegs

    def limbs(self):
        return self.arms + self.legs  # add the number of limbs


spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)


# In[8]:


# Objects as Arguments and parameters

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

def distance(point1, point2):   # Notice that this is a function and not a method. Note indentation and lack of self.
    xdiff = point2.getX()-point1.getX()
    ydiff = point2.getY()-point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4,3)
q = Point(0,0)
print(distance(p,q))


# We could have made distance be a method of the Point class. Then, we would have called the first parameter self, and would have invoked it using the dot notation, as in the following code. Which way to implement it is a matter of coding style. Both work correctly. Most programmers choose whether to make functions be stand-alone or methods of a class based on whether the function semantically seems to be an operation that is performed on instances of the class. In this case, because distance is really a property of a pair of points and is symmetric (the distance from a to b is the same as that from b to a) it makes more sense to have it be a standalone function and not a method. Many heated discussions have occurred between programmers about such style decisions.

# In[9]:


import math

class Point:  # You don't need to have () for a class name, class name is Capitalized
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(self, point2):   # This is a method, notice self as first argument and indentation within class Point
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(4,3)
q = Point(0,0)
print(p.distance(q))


# In[ ]:




