#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
 
# create Special methods (dunder)
    def __repr__(self):
        pass
    
    
#    def __str__(self):
#        pass
        
emp_1 = Employee('FirstName', 'LastName', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)


# In[2]:


class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    
#    def __str__(self):
#        pass
        
emp_1 = Employee('FirstName', 'LastName', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

#repr(emp_1)
#str(emp_1)

print(emp_1)


# In[3]:


class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    
    def __str__(self):
           return '{} - {}'.format(self.fullname(), self.email)
        
emp_1 = Employee('FirstName', 'LastName', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

#repr(emp_1)
#str(emp_1)

print(emp_1)


# In[4]:


print(emp_1.__repr__())
print(emp_1.__str__())


# In[5]:


print(1+2)


# In[6]:


# adding integers
print(int.__add__(1,2))


# In[7]:


# concatenation of strings
print(str.__add__('a','b'))


# In[8]:


class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    
    def __str__(self):
           return '{} - {}'.format(self.fullname(), self.email)
        
    def __add__(self, other):   # Add the pay of two employees
        return self.pay + other.pay
        
emp_1 = Employee('FirstName', 'LastName', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)


# In[9]:


print('test'.__len__())


# In[ ]:




