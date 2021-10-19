#!/usr/bin/env python
# coding: utf-8

# In[28]:


pip install pandas


# In[29]:


import pandas as np


# In[30]:


import numpy as np


# In[34]:


data = pd.read_csv('data/president_heights.csv')


# In[44]:


height = np.array(data['height(cm)'])
print(heights)


# In[45]:


data.head()


# In[46]:


print("Mean height =", np.mean(height))
print("Standara deviation =", np.std(height))
print("Minimum height =", np.min(height))
print("Maximum height =", np.max(height))
print("25th percentile =", np.nanpercentile(height, 25))
print("Median =", np.nanmedian(height))
print("75th percentile =", np.nanpercentile(height, 75))


# In[47]:


max_idx = np.argmax(height)
min_idx = np.argmin(height)
print("max_idx =", max_idx)
print("min_idx =",min_idx)


# In[48]:


max_name = data.iloc[max_idx]['name']
min_name = data.iloc[min_idx]['name']

print("The tallest president is", max_name)
print("The smallest president is", min_name)


# In[52]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height(cm)')
plt.ylabel('number')
plt.show()

