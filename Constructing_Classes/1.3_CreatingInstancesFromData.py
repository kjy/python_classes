#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Data
cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = list(zip(cityNames, populations, states))
print(city_tuples)


# In[4]:


# Data
cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = list(zip(cityNames, populations, states))
print(city_tuples)

class City:
    
    def __init__(self, n, p, s):   # Constructor accepts name, population, and state
        self. name = n
        self.population = p
        self.state = s
        
    def __str__(self):   # Use str method
        return '{}, {} (pop:{})'.format(self.name, self.state, self.population)
    
cities = []

for city_tup in city_tuples:
    print(city_tup)   


# In[6]:


# Version # 2

# Data
cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = list(zip(cityNames, populations, states))
print(city_tuples)

class City:
    
    def __init__(self, n, p, s):
        self. name = n
        self.population = p
        self.state = s
        
    def __str__(self):
        return '{}, {} (pop:{})'.format(self.name, self.state, self.population)
    

for city_tup in city_tuples:
    name, pop, state = city_tup
    print(name, pop, state)


# In[8]:


# Version # 3

# Data
cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = list(zip(cityNames, populations, states))
print(city_tuples)

class City:
    
    def __init__(self, n, p, s):
        self. name = n
        self.population = p
        self.state = s
        
    def __str__(self):
        return '{}, {} (pop:{})'.format(self.name, self.state, self.population)
    

cities = []
for city_tup in city_tuples:
    name, pop, state = city_tup
    city = City(name, pop, state)  # instance of the City class
    cities.append(city)
print(cities)


# In[9]:


# Version # 4

# Data
cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = list(zip(cityNames, populations, states))
print(city_tuples)

class City:
    
    def __init__(self, n, p, s):
        self. name = n
        self.population = p
        self.state = s
        
    def __str__(self):
        return '{}, {} (pop:{})'.format(self.name, self.state, self.population)
    
cities = [City(n, p, s) for (n, p, s) in city_tuples]
print(cities) # a list of city instances


# In[11]:


# Version # 5

# Data
cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = list(zip(cityNames, populations, states))
print(city_tuples)

class City:
    
    def __init__(self, n, p, s):
        self. name = n
        self.population = p
        self.state = s
        
    def __str__(self):
        return '{}, {} (pop:{})'.format(self.name, self.state, self.population)
    
cities = [City(*t) for t in city_tuples]  # * will expand tuple into a list of arguments
print(cities)


# In[ ]:




