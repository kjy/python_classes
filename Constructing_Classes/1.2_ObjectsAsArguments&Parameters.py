#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Objects as Arguments and parameters

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):  # Constructor with double underscore, "dunderscore"

        self.x = initX   # Initialize instance variable x
        self.y = initY   # Insitialize instance variable y

    def getX(self):   # Method is a function inside of a class with first argument as self. 
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

# In[30]:


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

    def distance(self, point2):   # This is a method, notice self as first argument and indentation within class Point
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(4,3)
q = Point(0,0)
print(p.distance(q))


# In[31]:


# Converting an Object to a String
# When we’re working with classes and objects, it is often necessary to print an object 
# (that is, to print the state of an object). Consider the example below.

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
print(p)
# prints the Point object


# The print function shown above produces a string representation of the Point p. The default functionality provided by Python tells you that p is an object of type Point. However, it does not tell you anything about the specific state of the point.
# 
# We can improve on this representation if we include a special method call __str__. Notice that this method uses the same naming convention as the constructor, that is two underscores before and after the name. It is common that Python uses this naming technique for special methods.
# 
# The __str__ method is responsible for returning a string representation as defined by the class creator. In other words, you as the programmer, get to choose what a Point should look like when it gets printed. In this case, we have decided that the string representation will include the values of x and y as well as some identifying text. It is required that the __str__ method create and return a string.
# 
# Whatever string the __str__ method for a class returns, that is the string that will print when you put any instance of that class in a print statement. For that reason, the string that a class’s __str__ method returns should usually include values of instance variables. If a point has x value 3 and y value 4, but another point has x value 5 and y value 9, those two Point objects should probably look different when you print them, right?

# In[32]:


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

    def __str__(self):   # Use special --str-- to print out actual value instead of object with memory address
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7,6)
print(p)


# When we run the program above you can see that the print function now shows the string that we chose.
# 
# Now, you ask, don’t we already have a str type converter that can turn our object into a string? Yes we do!
# 
# And doesn’t print automatically use this when printing things? Yes again!
# 
# However, as we saw earlier, these automatic mechanisms do not do exactly what we want. Python provides many default implementations for methods that we as programmers will probably want to change. When a programmer changes the meaning of a method we say that we override the method. Note also that the str type converter function uses whatever __str__ method we provide.

# In[33]:


class Cereal:
    """ Cereal class. """

    def __init__(self, initString1, initString2, initInt1):

        self.name = initString1
        self.brand = initString2
        self.fiber = initInt1

    def getname(self):
        return self.name

    def getbrand(self):
        return self.brand

    def getfiber(self):
        return self.fiber
    

    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand, self.fiber)  

c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(c1)
print(c2)


# Instance as Return Values.
# 
# Functions and methods can return objects. This is actually nothing new since everything in Python is an object and we have been returning values for quite some time. (You can also have lists or tuples of object instances, etc.) The difference here is that we want to have the method create an object using the constructor and then return it as the value of the method.
# 
# Suppose you have a point object and wish to find the midpoint halfway between it and some other target point. We would like to write a method, let’s call it halfway, which takes another Point as a parameter and returns the Point that is halfway between the point and the target point it accepts as input.

# In[34]:


class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)    # you can return a value

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)
# note that you would have exactly the same result if you instead wrote
# mid = q.halfway(p)
# because they are both Point objects, and the middle is the same no matter what

print(mid)
print(mid.getX())
print(mid.getY())
# The resulting Point, mid, has an x value of 4 and a y value of 8. 
# We can also use any other methods on mid since it is a Point object.


# Sorting Lists of Instances.
# 
# You previously learned how to sort lists. Sorting lists of instances of a class is not fundamentally different from sorting lists of objects of any other type. There is a way to define a default sort order for instances, right in the class definition, but it requires defining a bunch of methods or one complicated method, so we won’t bother with that. Instead, you should just provide a key function as a parameter to sorted (or sort).
# 
# Previously, you have seen how to provide such a function when sorting lists of other kinds of objects. For example, given a list of strings, you can sort them in ascending order of their lengths by passing a key parameter. Note that if you refer to a function by name, you give the name of the function without parentheses after it, because you want the function object itself. The sorted function will take care of calling the function, passing the current item in the list. Thus, in the example below, we write key=len and not key=len().

# In[35]:


L = ["Cherry", "Apple", "Blueberry"]

print(sorted(L, key=len))# sort by length in L

#alternative form using lambda, if you find that easier to understand
print(sorted(L, key= lambda x: len(x)))  


# When each of the items in a list is an instance of a class, you need to provide a function that takes one instance as an input, and returns a number. The instances will be sorted by their numbers.

# In[36]:


class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)


# Sometimes you will find it convenient to define a method for the class that does some computation on the data in an instance. In this case, our class is too simple to really illustrate that. But to simulate it, I’ve defined a method sort_priority that just returns the price that’s stored in the instance. Now, that method, sort_priority takes one instance as input and returns a number. So it is exactly the kind of function we need to provide as the key parameter for sorted. Here it can get a little confusing: to refer to that method, without actually invoking it, you can refer to Fruit.sort_priority. This is analogous to the code above that referred to len rather than invoking len().

# In[37]:


class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)


# You have already seen that each instance of a class has its own namespace with its own instance variables. Two instances of the Point class each have their own instance variable x. Setting x in one instance doesn’t affect the other instance.
# 
# A class can also have class variables. A class variable is set as part of the class definition.
# 
# For example, consider the following version of the Point class. Here we have added a graph method that generates a string representing a little text-based graph with the Point plotted on the graph. It’s not a very pretty graph, in part because the y-axis is stretched like a rubber band, but you can get the idea from this.
# 
# Note that there is an assignment to the variable printed_rep on line 4. It is not inside any method. That makes it a class variable. It is accessed in the same way as instance variables. For example, on line 16, there is a reference to self.printed_rep. If you change line 4, you have it print a different character at the x,y coordinates of the Point in the graph.

# In[38]:


# Class variables and instance variables.

# When python searches for instancename.instancevar (like p1.graph()), it first searches inside of the 
# instance and then it searches inside the class. If nothing is found, a runtime error will result.


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())


# To be able to reason about class variables and instance variables, it is helpful to know the rules that the python interpreter uses. That way, you can mentally simulate what the interpreter does.
# 
# When the interpreter sees an expression of the form <obj>.<varname>, it:
# Checks if the object has an instance variable set. If so, it uses that value.
# If it doesn’t find an instance variable, it checks whether the class has a class variable. If so it uses that value.
# If it doesn’t find an instance or a class variable, it creates a runtime error (actually, it does one other check first, which you will learn about in the next chapter.)
# When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:
# Evaluates the expression on the right-hand side to yield some python object;
# Sets the instance variable <varname> of <obj> to be bound to that python object. Note that an assignment statement of this form never sets the class variable, it only sets the instance variable.
# In order to set the class variable, you use an assignment statement of the form <varname> = <expr> at the top-level in a class definition, like on line 4 in the code above to set the class variable printed_rep.
# 
# In case you are curious, method definitions also create class variables. Thus, in the code above, graph becomes a class variable that is bound to a function/method object. p1.graph() is evaluated by:
# looking up p1 and finding that it’s an instance of Point
# looking for an instance variable called graph in p1, but not finding one
# looking for a class variable called graph in p1’s class, the Point class; it finds a function/method object
# Because of the () after the word graph, it invokes the function/method object, with the parameter self bound to the object p1 points to.

# A Tamagotchi Game
# There are also a lot of interesting ways to put user-defined classes to use that don’t involve data from the internet. Let’s pull all these mechanics together in a slightly more interesting way than we got with the Point class. Remember Tamagotchis, the little electronic pets? As time passed, they would get hungry or bored. You had to clean up after them or they would get sick. And you did it all with a few buttons on the device.
# 
# We are going to make a simplified, text-based version of that. In your problem set and in the chapter on Inheritance <chap_inheritance> we will extend this further.
# 
# First, let’s start with a class Pet. Each instance of the class will be one electronic pet for the user to take care of. Each instance will have a current state, consisting of three instance variables:
# hunger, an integer
# boredom, an integer
# sounds, a list of strings, each a word that the pet has been taught to say
# In the __init__ method, hunger and boredom are initialized to random values between 0 and the threshold for being hungry or bored. The sounds instance variable is initialized to be a copy of the class variable with the same name. The reason we make a copy of the list is that we will perform destructive operations (appending new sounds to the list). If we didn’t make a copy, then those destructive operations would affect the list that the class variable points to, and thus teaching a sound to any of the pets would teach it to all instances of the class!
# 
# There is a clock_tick method which just increments the boredom and hunger instance variables, simulating the idea that as time passes, the pet gets more bored and hungry.
# 
# The __str__ method produces a string representation of the pet’s current state, notably whether it is bored or hungry or whether it is happy. It’s bored if the boredom instance variable is larger than the threshold, which is set as a class variable.
# 
# To relieve boredom, the pet owner can either teach the pet a new word, using the teach() method, or interact with the pet, using the hi() method. In response to teach(), the pet adds the new word to its list of words. In response to the hi() method, it prints out one of the words it knows, randomly picking one from its list of known words. Both hi() and teach() cause an invocation of the reduce_boredom() method. It decrements the boredom state by an amount that it reads from the class variable hunger_decrement. The boredom state can never go below 0.
# 
# To relieve hunger, we call the feed() method.

# In[39]:


from random import randrange

class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, 
                                      # we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


# Let’s try making a pet and playing with it a little. Add some of your own commands, too, and keep printing p1 to see what the effects are. If you want to directly inspect the state, try printing p1.boredom or p1.hunger.

# In[40]:


p1 = Pet("Fido")
print(p1)
for i in range(10):
    p1.clock_tick()
    print(p1)
p1.feed()
p1.hi()
p1.teach("Boo")
for i in range(10):
    p1.hi()
print(p1)


# In[41]:


import sys
sys.setExecutionLimit(60000)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                animals.append(Pet(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()



play()


# In[ ]:





# In[ ]:




