#!/usr/bin/env python
# coding: utf-8

# In[3]:


is_tasted = True

print(type(is_tasted))

a=3.14
print(type(a))


# In[4]:


print("Yes"=='Yes')


# In[5]:


print((2>1)==(5<10))


# In[7]:


c='2'
d=2
print(c==d)


# In[9]:


print("Yes" != "No")


# In[10]:


va11=10
va12=20
print(va11!=va12)


# In[11]:


print((10>1)!=(10>1000))


# In[12]:


True or True


# In[13]:


True or False


# In[15]:


False or False


# 1<2 or 3<1

# In[18]:


1<2 or 3<1


# In[19]:


3<1 or 1>6


# In[20]:


1==1 or 1<2


# In[21]:


True and True


# In[22]:


True and False


# In[23]:


False and False


# In[24]:


1==1 and 1<2


# In[25]:


1<2 and 3<1


# 

# In[37]:


puppy='maltepoo'
is_yes=False

if puppy =='maltese':
    print('말티즈 맞네')
    is_yes= True
elif puppy == 'poodle':
    print('응')
    is_yes = True
elif puppy=='maltepoo':
    print("말티푸")
    is_yes =True

elif puppy == "shitzu":
    print('응')
    is_yes=True
else:
    print("종료")
print(is_yes)


# In[38]:


x=1
try:
    print(y)
    print(x)
except:
    print("[ERROR] : y is not declared")
    
print("continue")


# In[ ]:




