#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[32]:


import numpy as np


# In[ ]:





# In[33]:


pd.Series


# In[3]:


pd.Series([10,20,30,40,50])


# In[10]:


n=pd.Series([10,20,30,40,50])


# In[11]:


type(n)


# In[12]:


n.size


# In[ ]:





# In[13]:


n.axes


# In[ ]:





# In[14]:


n.dtype


# In[ ]:





# In[15]:


n.ndim


# In[16]:


n.values


# In[ ]:





# In[23]:


n.head()


# In[ ]:





# In[24]:


n.head(3)


# In[ ]:





# In[26]:


n.tail()


# In[ ]:





# In[28]:


n.tail(3)


# In[ ]:





# In[68]:


mytail = np.array([8,9,10,11,12,13])
mytail


# In[ ]:





# In[69]:


mytail = pd.Series(mytail)


# In[71]:


mytail.tail()


# In[ ]:





# In[76]:


mytail.index


# In[73]:


mytail.values


# In[75]:


pd.Series([22,23,24,25,26])


# In[ ]:





# In[78]:


pd.Series([22,23,24,25,26], index=[2,3,4,5,6])


# In[ ]:





# In[81]:


n=pd.Series([22,23,24,25,26], index=['first','second','third','fourth','fifth'])
n


# In[ ]:





# In[85]:


n['third']


# In[88]:


Ages={'John':40, 'Jude':43, 'Jules':23}
Ages


# In[ ]:





# In[89]:


pd.Series(Ages)


# In[ ]:





# In[90]:


n1 = pd.Series([4,5,6])
n2 = pd.Series([7,8,9])
pd.concat([n1,n2])


# In[ ]:





# In[93]:


n1[2]


# In[106]:


n["first"]


# In[98]:


s=pd.Series([11,12,13,14,15],index=['First','Second','Third','Fourth','Fifth'])
s


# In[ ]:





# In[104]:


list(s.items())


# In[102]:


s.keys


# In[ ]:





# In[105]:


list(s.items())


# In[ ]:





# In[111]:


s1 = pd.Series([2,3,55,2,6,44])
s1


# In[ ]:





# In[112]:


3 in s1


# In[ ]:





# In[113]:


34 in s1


# In[ ]:





# In[114]:


s1[[2,4]]


# In[ ]:





# In[115]:


s1[[1,5]]


# In[ ]:





# In[116]:


s1[[2]]


# In[ ]:





# In[118]:


s1[2]


# In[ ]:





# In[119]:


s1[0] =4


# In[120]:


s1


# In[ ]:





# In[121]:


pd.DataFrame({'Name':['Malcom','Clint','Bush','Jat'], 'Age':[15,19,24,21], 'Location':['Adum','Suame','Bantama','Kotei']})


# In[ ]:





# In[128]:


var = {'Name':['Malcom','Clint','Bush','Jat'], 'Age':[15,19,24,21], 'Location':['Adum','Suame','Bantama','Kotei']}
dataframe = pd.DataFrame(var)
dataframe


# In[ ]:





# In[129]:


dataframe[['Location']]


# In[ ]:





# In[130]:


dataframe.Location


# In[ ]:





# In[132]:


dataframe['Location']


# In[ ]:





# In[134]:


d=[20,25,36,98,47,21,59]
df=pd.DataFrame(d,columns=['Variables'])
df


# In[ ]:





# In[135]:


names=['Bill','Boris','Jane','Janet']
df=pd.DataFrame(names,columns=['Names'])
df


# In[ ]:





# In[141]:


import numpy as np
arr=np.array([8,9,5,7,6,3,2,1,4]).reshape(3,3)
arr


# In[ ]:





# In[142]:


df=pd.DataFrame(arr,columns=['Variable1','Variable2','Variable3'])
df


# In[ ]:





# In[143]:


df.axes


# In[ ]:





# In[144]:


df.shape


# In[ ]:





# In[145]:


df.ndim


# In[ ]:





# In[146]:


df.size


# In[ ]:





# In[147]:


df.columns


# In[ ]:





# In[148]:


df.values


# In[ ]:




