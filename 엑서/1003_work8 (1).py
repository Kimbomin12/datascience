#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[7]:


"""
Numpy Array Attributes
"""

#Creating an array

print(np.arange(3)) #stop
print(np.arange(2,5)) #start, stop
print(np.arange(1,9,2)) #start,stop,step


# In[64]:


# Random number generator

arr1=np.random.randint(10) #0~9사이 숫자들 (10은 제외)
print(arr1)
arr2=np.random.randint(10,size=(5)) #0~9까지 크기5로 배열
print(arr2)
arr3=np.random.randint(100,size=(3,5))
print(arr3)
arr4=np.random.randint(100,size=(3, 5, 2))
print(arr4)


# In[80]:


#Attributes

print("arr2.ndim = ", arr2.ndim)
print("arr3.ndim = ", arr3.shape)
print("arr3.size = ", arr3.size)

print("arr3.dtype = ", arr3.dtype)
print("arr3.itemsize = ", arr3.itemsize)

arr5 = np.array([1.5, 2.3, 3.4])
print("arr5.itemsize = ", arr4.itemsize)

print("arr3.nbytes = ", arr3.nbytes)


# In[113]:


"""
Subarrays as no-copy views
"""
np.random.seed(1) #동일한 난수배열을 유지하기 위해 (새로운 값 생성 안함)

arr= np. random.randint(10, size=(3,4))
print(arr,'/n')

arr_sub=arr[:2,:2]
print(arr_sub,'/n')


arr_sub[0,0] =-1  #원본 배열을 -1로 바꿈
print(arr_sub, '/n')

print(arr) #출력해보면 원본 배열도 -1로 바꿔져 있음


# In[5]:


# .copy()
np.random.seed(1)

arr=np.random.randint(10,size =(3,4))
print(arr)

arr_sub = arr[:2,:2].copy() #원본 배열 유지
print(arr_sub,'/n')

arr_sub[0,0] = -1   #원본 배열 -1로 바꿈
print(arr_sub,'/n')
 
print(arr) #.copy로 인해 원본배열 -1로 안바뀜


# In[2]:


"""
Resahping of Arrays
"""

arr= np.arange(1,10)
print(arr)

grid = arr.reshape(3,3)
print(grid)


# In[6]:


#np.newaxis

arr=np.array([1,2,3,])
print(arr)
print("arr.ndim =", arr.ndim)
print("arr.shape =",arr.shape)

arr_new = arr[np.newaxis, :]
print(arr_new)
print("arr_new.ndim = ", arr.ndim)
print("arr_new.ndim = ", arr.shape)


# In[17]:


"""
Array Concatenation
"""
#np.concatenate(), np.vstack(), np.hstack()

arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
arr_3 = np.array([7,8,9])

arr_total = np.concatenate([arr_1,arr_2,arr_3])
print(arr_total)

arr_total = np.vstack([arr_1,arr_2,arr_3])
print(arr_total)

arr_total = np.hstack([arr_1,arr_2,arr_3])
print(arr_total)


# In[19]:


"""
Array Splitting
"""

arr=[1,2,3,99,99,3,2,1]
print(arr)

arr_1,arr_2,arr_3 = np.split(arr,[3,5]) #3기준으로 자르고 5기준으로 자른다 > 0~2번까지 자르고 3~4번까지 자른다
print(arr_1,arr_2,arr_3)

