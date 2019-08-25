#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Employee():
    
    # create a calss variable
    num_of_emps = 0
    
    # create a class variable set to 4% raise
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +  last + '@company.com'
        
        Employee.num_of_emps += 1
            
    def fullname(self):   # use self as argument for method, you will get a type error if you forget self
        return '{} {}'.format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)  
        
    @classmethod     # class decorator, alter the functionality for our method
    def set_raise_amt(cls, amount):   # receive class, cls, as first argument as opposed to instance (self)
        cls.raise_amt = amount
        
        
        
emp_1 = Employee('Jane', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000) 

# We are working with the class as opposed to the instance
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


# In[5]:


Employee.set_raise_amt(1.05)


print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


# In[8]:


emp_1.set_raise_amt(1.06)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


# In[ ]:


# New example


# In[18]:


# employee information in the form of a string, need to parse it first before creating instances.
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Jane-Doe-80000'
emp_str_3 = 'Baby-Doe-40000'

first, last, pay = emp_str_1.split('-')
print(first)
print(last)
print(pay)

# create a new employee instance
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)


# In[21]:


# Now put the above parsing into the body of the code as a classmethod
class Employee():
    
    # create a calss variable
    num_of_emps = 0
    
    # create a class variable set to 4% raise
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +  last + '@company.com'
        
        Employee.num_of_emps += 1
            
    def fullname(self):   # use self as argument for method, you will get a type error if you forget self
        return '{} {}'.format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return cls(first, last, pay)
        
        
    @classmethod     # class decorator, alter the functionality for our method
    def set_raise_amt(cls, amount):   # receive class, cls, as first argument as opposed to instance (self)
        cls.raise_amt = amount
        
    @classmethod   # from string alternative constructor, for class method, first argument is cls
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
        
#emp_1 = Employee('Jane', 'Doe', 50000)
#emp_2 = Employee('Test', 'User', 60000)


# employee information in the form of a string, need to parse it first before creating instances.
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Jane-Doe-80000'
emp_str_3 = 'Baby-Doe-40000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


# In[26]:


# static method behave like regular functions, @staticmethod
# do not use self as first argument

class Employee():
    
    # create a calss variable
    num_of_emps = 0
    
    # create a class variable set to 4% raise
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +  last + '@company.com'
        
        Employee.num_of_emps += 1
            
    def fullname(self):   # use self as argument for method, you will get a type error if you forget self
        return '{} {}'.format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return cls(first, last, pay)
        
        
    @classmethod     # class decorator, alter the functionality for our method
    def set_raise_amt(cls, amount):   # receive class, cls, as first argument as opposed to instance (self)
        cls.raise_amt = amount
        
    @classmethod   # from string alternative constructor, for class method, first argument is cls
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
    @staticmethod    # use staticmethod decorator, don't take instance or class as first argument
    def is_workday(day):   # dates in python, 0 = Monday, 6 = Sunday
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True
        
#emp_1 = Employee('Jane', 'Doe', 50000)
#emp_2 = Employee('Test', 'User', 60000)


import datetime
my_date = datetime.date(2016, 7, 10)  # Sunday
print(Employee.is_workday(my_date))
my_date = datetime.date(2016, 7, 11)  # Monday
print(Employee.is_workday(my_date))


# In[ ]:




