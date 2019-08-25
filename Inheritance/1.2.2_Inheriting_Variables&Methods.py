#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Create a Person class to represent a person with name and age
CURRENT_YEAR = 2019

class Person:
    
    def __init__(self, name, year_born):
        self.name = name    # create instance variable for name
        self.year_born = year_born  # create instance variable for year_born
        
    def getAge(self):   # create method that takes year_born and subtract it from current year
        return CURRENT_YEAR - self.year_born
    
    def __str__(self):  # create special str method to print out result
        return '{} ({})'.format(self.name, self.getAge())
    
alice = Person('Alice Smith', 1990)
print(alice)    
    


# In[9]:


# Create a Student class that has everything that Person class has plus more, knowledge
# Include a method called study()

class Student:
    
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born
        self.knowledge = 0   # create instance variable knowledge with value 0
        
    def study(self): 
        self.knowledge += 1  # increment by 1
        
    def getAge(self):
        return CURRENT_YEAR - self.year_born
    
    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())
    
    
alice = Student('Alice Smith', 1990) 
print(alice)


# In[10]:


class Student:
    
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born
        self.knowledge = 0
        
    def study(self): 
        self.knowledge += 1
        
    def getAge(self):
        return CURRENT_YEAR - self.year_born
    
    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())
    
    
alice = Student('Alice Smith', 1990) 
print(alice.knowledge)


# In[11]:


class Student:
    
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born
        self.knowledge = 0
        
    def study(self): 
        self.knowledge += 1
        
    def getAge(self):
        return CURRENT_YEAR - self.year_born
    
    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())
    
    
alice = Student('Alice Smith', 1990) 
alice.study()
print(alice.knowledge)


# In[14]:


# Revise using inheritance. 
# Student class should have everything that Person class has plus more.
# Student class should inherit form Person class.
# Remove getAge() from Student class since it is already found in Person class.
# Remove thunderscore str method since it is already found in Person class. 

class Student(Person):  # Every student is a person. 
    
    def __init__(self, name, year_born):
        #self.name = name  # remove this since it is found in Person class
        
        Person.__init__(self, name, year_born) # this will call def __init__(self, name, year_born): in Person class.
        
        #self.year_born = year_born  # remove this since it is found in Person class
        
        self.knowledge = 0
        
    def study(self): 
        self.knowledge += 1
        
    # def getAge(self):   # remove this as it is found in Person class
    #    return CURRENT_YEAR - self.year_born    
        
    
    # def __str__(self):  # remove this as it is found in Person class
    #    return '{} ({})'.format(self.name, self.getAge())

alice = Student('Alice Smith', 1990)
alice.study()
print(alice.knowledge)


# In[15]:


# Cleaned up code. 
# Student class will inherit from Person class
# Create Person and Student classes with inheritance
# Student class inherits from Person class

CURRENT_YEAR = 2019

class Person():
    
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born
        
    def getAge(self):
        return CURRENT_YEAR - self.year_born
    
    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())

    
    

class Student(Person):  # Every student is a person. 
    
    def __init__(self, name, year_born):
        # Person constructor created to inherit from Person class which is the class you want to inherit from.
        Person.__init__(self, name, year_born) # this will call def __init__(self, name, year_born): in Person class.
        self.knowledge = 0
        
    def study(self): 
        self.knowledge += 1

        
alice = Student('Alice Smith', 1990)
alice.study()
print(alice.knowledge)
print(alice.getAge())


# In[ ]:




