#!/usr/bin/env python
# coding: utf-8

# Mechanics of Defining a Subclass.
# 
# We said that inheritance provides us a more elegant way of, for example, creating Dog and Cat types, rather than making a very complex Pet class. In the abstract, this is pretty intuitive: all pets have certain things, but dogs are different from cats, which are different from birds. Going a step further, a Collie dog is different from a Labrador dog, for example. Inheritance provides us with an easy and elegant way to represent these differences.
# 
# Basically, it works by defining a new class, and using a special syntax to show what the new sub-class inherits from a super-class. So if you wanted to define a Dog class as a special kind of Pet, you would say that the Dog type inherits from the Pet type. In the definition of the inherited class, you only need to specify the methods and instance variables that are different from the parent class (the parent class, or the superclass, is what we may call the class that is inherited from. In the example we’re discussing, Pet would be the superclass of Dog or Cat).
# 
# Here is an example. Say we want to define a class Cat that inherits from Pet. Assume we have the Pet class that we defined earlier.
# 
# We want the Cat type to be exactly the same as Pet, except we want the sound cats to start out knowing “meow” instead of “mrrp”, and we want the Cat class to have its own special method called chasing_rats, which only Cat s have.
# 
# For reference, here’s the original Tamagotchi code

# In[1]:


from random import randrange

# Here's the original Pet class
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
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

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
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
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

# Here's the new definition of class Cat, a subclass of Pet.
class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
    sounds = ['Meow']

    def chasing_rats(self):
        return "What are you doing, Pinky? Taking over the world?!"


# All we need is the few extra lines at the bottom of the ActiveCode window! The elegance of inheritance allows us to specify just the differences in the new, inherited class. In that extra code, we make sure the Cat class inherits from the Pet class. We do that by putting the word Pet in parentheses, class Cat(Pet):. In the definition of the class Cat, we only need to define the things that are different from the ones in the Pet class.
# 
# In this case, the only difference is that the class variable sounds starts out with the string "Meow" instead of the string "mrrp", and there is a new method chasing_rats.
# 
# We can still use all the Pet methods in the Cat class, this way. You can call the __str__ method on an instance of Cat to print an instance of Cat, the same way you could call it on an instance of Pet, and the same is true for the hi method – it’s the same for instances of Cat and Pet. But the chasing_rats method is special: it’s only usable on Cat instances, because Cat is a subclass of Pet which has that additional method.
# 
# In the original Tamagotchi game in the last chapter, you saw code that created instances of the Pet class. Now let’s write a little bit of code that uses instances of the Pet class AND instances of the Cat class.

# In[2]:


p1 = Pet("Fido")
print(p1) # we've seen this stuff before!

p1.feed()
p1.hi()
print(p1)

cat1 = Cat("Fluffy")
print(cat1) # this uses the same __str__ method as the Pets do

cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi()
print(cat1)

print(cat1.chasing_rats())

#print(p1.chasing_rats()) # This line will give us an error. The Pet class doesn't have this method!


# And you can continue the inheritance tree. We inherited Cat from Pet. Now say we want a subclass of Cat called Cheshire. A Cheshire cat should inherit everything from Cat, which means it inherits everything that Cat inherits from Pet, too. But the Cheshire class has its own special method, smile.

# In[3]:


class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

    def smile(self): # this method is specific to instances of Cheshire
        print(":D :D :D")

# Let's try it with instances.
cat1 = Cat("Fluffy")
cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi() # Uses the special Cat hello.
print(cat1)

print(cat1.chasing_rats())

new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
new_cat.hi() # same as Cat!
new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

# cat1.smile() # This line would give you an error, because the Cat class does not have this method!

# None of the subclass methods can be used on the parent class, though.
p1 = Pet("Teddy")
p1.hi() # just the regular Pet hello
#p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
#p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.


# After you run the code, new_cat = Cheshire("Pumpkin"), how many instance variables exist for the new_cat instance of Cheshire? 4

# In[ ]:


# What would print after running the following code:

new_cat = Cheshire("Pumpkin”)
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
another_cat.song()
                   
# We are Siamese if you please. We are Siamese if you don’t please. 
# another_cat is an instance of Siamese, so its song() method is invoked.                   


# In[ ]:


# What would print after running the following code:

new_cat = Cheshire("Pumpkin”)
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
new_cat.song()
                   
# Error would result. You cannot invoke methods defined in the Siamese class on an instance of the Cheshire class. 
# Both are subclasses of Cat, but Cheshire is not a subclass of Siamese, so it doesn't inherit its methods.                   

