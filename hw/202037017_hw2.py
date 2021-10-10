#!/usr/bin/env python
# coding: utf-8

# In[14]:


subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]
gradebook=[["physcics",98],["calculus",97],["poetry",85],["history",88]]
gradebook.append(["computer science",100])
gradebook.append(["visual arts",93])
gradebook.remove(["poetry",85])
gradebook.append(["potery","pass"])
last_semester_gradebook=[["politics",80],["latin",96],["dance",97],["architecture",65]]
full_gradebook=(last_semester_gradebook+gradebook)

print(full_gradebook)

