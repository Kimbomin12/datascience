#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[2]:


import numpy


# In[5]:


# .dtype attribute

a= np.array([1,"A",True])
print(a.dtype)

b = np.array([1,2,3])
print(a.dtype)

c = np.array([1.1,2.3])
print(c.dtype)


# In[7]:


"""
Size comparison of ndarray and list object
"""

from sys import getsizeof
lst =[1,2,3,4,5,6,7,8,9,10]
print(getsizeof(lst))

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(getsizeof(Arr))


# 

# In[ ]:


"""
Exercise
"""

test_1

