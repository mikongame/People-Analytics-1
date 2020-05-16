#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.cluster import KMeans
sns.set()


    


# In[2]:


data = pd.read_csv('MFGEmployees4.csv')
data.head()


# In[3]:


data.describe()


# In[4]:


new_data = data.copy()
new_data = new_data.sample(100)
new_data.head()


# In[6]:


plt.scatter(new_data['Age'],new_data['AbsentHours'])
plt.xlabel('Age')
plt.ylabel('AbsentHours')
plt.title('Age & AbsentHours')
plt.show()


# In[12]:


plt.figure(figsize=(20, 9))
sns.boxplot(new_data["DepartmentName"],new_data["AbsentHours"], hue="Gender", data=new_data)
plt.xticks(rotation = 45)
plt.title('Absenteeism per Department');


# In[17]:


plt.figure(figsize=(30, 10))
sns.boxplot(new_data["Division"],new_data["AbsentHours"], hue="Gender", data=new_data)
plt.xticks(rotation = 45)
plt.title('Absenteeism per Division')


# In[18]:


plt.figure(figsize=(30, 10))
sns.boxplot(new_data["StoreLocation"],new_data["AbsentHours"], hue="Gender", data=new_data)
plt.title('Absenteeism per store location')
plt.xticks(rotation = 90)


# In[22]:


avg_male_absent = new_data.AbsentHours[new_data.Gender == 'M'].mean()
avg_female_absent = new_data.AbsentHours[new_data.Gender == 'F'].mean()


# In[25]:


avg_male_absent


# In[26]:


avg_female_absent

