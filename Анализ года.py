#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[68]:


df = pd.read_excel('D:\PycharmProjects\Dali_Avto_Data\\2016список.xls')


# In[69]:


df.head()


# In[70]:


df = df.loc[:,['Дата','Партнер','Сумма']]


# In[71]:


df.columns = ['date','client','summ']


# In[72]:


df.date = df.date.apply(lambda x: x[3:10])


# In[73]:


df1 = df.groupby('date', as_index=False).agg({'summ':sum})


# In[74]:




# In[67]:


df1.sort_values('summ')
df1.plot(kind='line', x='date', y='summ', label=f'sum')
plt.grid()
print(df1)
plt.show()

# In[ ]:




