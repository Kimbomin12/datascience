#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Function

def my_function(x):
    return x + 1

print(my_function(1))
x=1
print(my_function(x))


#Method

class my_class:
    def my_method(self):
        return x +1

cls = my_class()
x=2
print(cls.my_method())

"""
Function Parameters
"""

def introuduce_myself(name,birthyear,city):
    print("Helo everyone, my name is %s, I was born in %d, and I live in %s" % (name,birthyear, city))
        
introuduce_myself("Bomin KIM",2001,"SeongNam")


# In[18]:


"""
Return Keyword
"""

#leap year = 윤년

def check_leap_year(year):
    if year % 4 ==0:
        return "%d is a leap year" % (year)
    else:
        return "%d is not a leap year" % (year)
print(check_leap_year(2021))


# In[21]:


"""
Returning Multiple Values
"""

def square_point(x,y,z):
    x_squared=x**2
    y_squared=y**2
    z_squared=z**2
    return x_squared, y_squared,z_squared
three_squared, four_squared, five_squared = square_point(3,4,5)
print(three_squared, four_squared, five_squared)

"""
Global Variables
"""

a= "Hello"
def prints_a():
    print(a)

prints_a()


# In[26]:


"""
Local Variables
"""

a = 5 #global var.
def f1():
    a=3 #Local var.
    print(a)
f1()


# In[28]:


"""
Keyword Arguments and Default Values
"""

def findvolume(height=1, width=1, depth=1):
    print("Height=" + str(height)) #str() : 어떤 값을 문자열 값으로 변환
    print("Width=" + str(width))
    print("Depth=%d" % (depth))
    
findvolume(1,2,3)
findvolume(width=4, depth=2, height=5)
findvolume(depth=3,width=2,) #findvolume값을 이미 1로 설정을 해놨기 때문에 def 값을 하나 입력 안해도 괜찮다.

