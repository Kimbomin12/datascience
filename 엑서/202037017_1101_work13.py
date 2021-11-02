#!/usr/bin/env python
# coding: utf-8

# In[22]:


pip install pandas_datareader


# In[24]:


import pandas as pd


# In[13]:


from pandas_datareader import data
goog = data.DataReader('GOOG', start=2004 , end=2021, data_source='yahoo')
                        
print(goog)


# In[15]:


# Visualization setup

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")


# In[16]:


#Plooting
goog = goog['Close']
goog.plot()


# In[17]:


#Resampleling (down sampling)
goog.resample('Q').mean() #Q= Quarter 1분기

#Resampling (up sampling)
goog.resample('H').max() # H=Hour 1시간, max() : 일별 최대값을 취하기


# In[25]:


print(pd.date_range('2021-11-01', periods=10, freq="M")) # M: Month end


# In[26]:


print(pd.date_range('2021-11-01', periods=10, freq="BM")) 


# In[30]:


print(pd.date_range('2021-11-01', periods=10, freq="MS")) # MS : Month start

print(pd.date_range('2021-11-01', periods=10, freq="QS")) #QS : 분기의 첫날

print(pd.date_range('2021-11-01', periods=10, freq="BMS")) #BAS : 매년 영업일 기준 첫날

print(pd.date_range('2021-11-01', periods=10, freq="1H30T")) # H : 시간, T: 분


# In[35]:


#Offsets
from pandas.tseries.offsets import DateOffset

ts = pd.Timestamp('2021-10-31 23:28:30')
ts + DateOffset(hours=40)


# In[37]:


#Offsets
from pandas.tseries.offsets import DateOffset

ts = pd.Timestamp('2021-10-31 23:28:30')
ts - DateOffset(years=71, month=4, days=5, hours=19, minutes=28, seconds=30)


# In[44]:


"""
Time-shifts
"""

#shift() and tshift() by 900 days
fig, ax =plt.subplots(3, sharey=True, figsize=(12,12))

#Apply a frequency to the data
goog = goog.asfreq('D', method= 'pad') #pad = forward fill NaN values

goog.plot(ax=ax[0])
goog.shift(900).plot(ax=ax[1])
goog.tshift(900).plot(ax=ax[2])

#Legends and annotations
local_max = pd.to_datetime('2007-11-05')
offset = pd.Timedelta(900, 'D')

ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[2].set(weight='heavy', color='red')
ax[0].axvline(local_max,alpha=0.3, color='red')

ax[0].legend(['shift(900)'], loc=2)
ax[0].get_xticklabels()[2].set(weight='heavy', color='red')
ax[0].axvline(local_max+offset,alpha=0.3, color='red')

ax[0].legend(['tshift(900)'], loc=2)
ax[0].get_xticklabels()[1].set(weight='heavy', color='red')
ax[0].axvline(local_max+offset,alpha=0.3, color='red');


# In[45]:


goog.tshift(900)


# In[48]:


"""
Rolling Windows
"""

rolling = goog.rolling(365, center=True)

data = pd.DataFrame({'input' : goog, 'one-year rolling_mean' : rolling.mean(), 'one-year rolling_std' : rolling.std()})

ax = data.plot(style=['-','--',':'])
ax.lines[0],set_alpha(0,3)

