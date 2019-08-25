#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python Object-Oriented Programming


# In[5]:


# Class is a blueprint
# Instance class

class Employee():
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
emp_1 == emp_2


# In[6]:


class Employee():
    pass

emp_1 = Employee()
emp_2 = Employee()

# manually setting of variables, time-consuming 
emp_1.first = 'Jane'
emp_1.last = 'Doe'
emp_1.email = 'Jane.Doe@company.com'
emp_1.pay = '50000'

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = '60000'

print(emp_1.email)
print(emp_2.email)


# In[13]:


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
        
emp_1 = Employee('Jane', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())  # make sure to use () when calling the method, instance class dot method
print(emp_2.fullname())
Employee.fullname(emp_1)  # call the method on the class so pass in the class instance, class dot method


# too time consuming to create print format for every time we want first and last name
# so create a method instead
# print('{} {}'.format(emp_1.first, emp_1.last))
        


# In[ ]:





# In[ ]:




