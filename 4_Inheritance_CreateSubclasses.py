#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
        
 # Inherit from the employee class, you get all the functionality (attributes and methods of employee class)       
class Developer(Employee):
    pass
        
#dev_1 = Employee('Jane', 'Doe', 50000)
#dev_2 = Employee('Test', 'Employee', 60000)

dev_1 = Developer('Jane', 'Doe', 50000)
dev_2 = Developer('Test', 'Employee', 60000)

print(help(Developer))  # gives method resolution order

print(dev_1.email)
print(dev_2.email)       


# In[6]:


# Inherit from Employee class        
class Developer(Employee):
    pass
    
#    def __init__(self, first, last, pay, prog_lang):
#        Employee.__init__(first, last, pay, prog_lang)
#        self.prog_lang = prog_lang


dev_1 = Developer('Jane', 'Doe', 50000)
dev_2 = Developer('Test', 'Employee', 60000)

print(dev_1.pay)
dev_1.apply_raise()  # raise amount used from parent class
print(dev_1.pay)
 


# In[15]:


# Inherit from Employee class        
class Developer(Employee):
    
    raise_amt = 1.10  # change raise amount in subclass
    
    def __init__(self, first, last, pay, prog_lang):
        #Employee.__init__(first, last, pay)  # did not work
        super().__init__(first, last, pay) # alternative way referring to parent class as super()
        self.prog_lang = prog_lang


dev_1 = Developer('Jane', 'Doe', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

#print(dev_1.pay)
#dev_1.apply_raise()  # raise amount used from parent class
#print(dev_1.pay)


# In[22]:


# Inherit code from parent class Employee
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []     
        else:
            self.employees = employees
            
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
                        
                
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            

dev_1 = Developer('Jane', 'Doe', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.print_emps()

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print(mgr_1.email)

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


# In[23]:


print(isinstance(mgr_1, Manager))


# In[24]:


print(isinstance(mgr_1, Employee))


# In[25]:


# Both manager and developer inherit from Employee but are not a part of each other's inheritance
print(isinstance(mgr_1, Developer))


# In[28]:


print(issubclass(Developer, Employee))


# In[29]:


print(issubclass(Manager, Employee))


# In[30]:


print(issubclass(Manager, Developer))


# In[ ]:




