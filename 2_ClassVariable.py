#!/usr/bin/env python
# coding: utf-8

# In[1]:


# use class constructor and create attribute variables of class
# create a method

class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +  last + '@company.com'
            
    def fullname(self):   # use self as argument for method, you will get a type error if you forget self
        return '{} {}'.format(self.first, self.last)
    
    # Pay raise amount of 4% is hardcoded in method, which makes it difficult to udpate
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
    
emp_1 = Employee('Jane', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)    

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Can't see the following:
# emp_1.raise_amount
# Employee.raise_amount

# What if you want to modify raise amount? Don't want to change in multiple locations of code


# In[ ]:


# What data do you want to share amongst all employees? Raises.


# In[7]:


# use class constructor and create attribute variables of class
# create a method

class Employee():
    
    # create a variable
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +  last + '@company.com'
            
    def fullname(self):   # use self as argument for method, you will get a type error if you forget self
        return '{} {}'.format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # NameError: name 'raise_amount' is not defined
    
emp_1 = Employee('Jane', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)    

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
print(Employee.__dict__)
#emp_1.apply_raise()
#print(emp_1.pay)

# Can't see the following:
# emp_1.raise_amount
# Employee.raise_amount


# In[8]:


Employee.raise_amount = 1.05

# It changed the raise amount for the class and for all of the instances.
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[9]:


emp_1.raise_amount = 1.06

# It only changed the raise amount for employee 1 only in its namespace
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[10]:




class Employee():
    
    # create a calss variable
    num_of_emps = 0
    
    # create a class variable
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +  last + '@company.com'
        
        Employee.num_of_emps += 1
            
    def fullname(self):   # use self as argument for method, you will get a type error if you forget self
        return '{} {}'.format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # NameError: name 'raise_amount' is not defined
        
emp_1 = Employee('Jane', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000) 

print(Employee.num_of_emps)   
# It will increment twice for 2 instantiation


# In[ ]:




