#!/usr/bin/env python
# coding: utf-8

# ### Interpreting Results of Logistic Regression
# 
# In this notebook (and quizzes), you will be getting some practice with interpreting the coefficients in logistic regression.  Using what you saw in the previous video should be helpful in assisting with this notebook.
# 
# The dataset contains four variables: `admit`, `gre`, `gpa`, and `prestige`:
# 
# * `admit` is a binary variable. It indicates whether or not a candidate was admitted into UCLA (admit = 1) our not (admit = 0).
# * `gre` is the GRE score. GRE stands for Graduate Record Examination.
# * `gpa` stands for Grade Point Average.
# * `prestige` is the prestige of an applicant alta mater (the school attended before applying), with 1 being the highest (highest prestige) and 4 as the lowest (not prestigious).
# 
# To start, let's read in the necessary libraries and data.

# In[8]:


import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("./admissions.csv")
df.head()


# There are a few different ways you might choose to work with the `prestige` column in this dataset.  For this dataset, we will want to allow for the change from prestige 1 to prestige 2 to allow a different acceptance rate than changing from prestige 3 to prestige 4.
# 
# 1. With the above idea in place, create the dummy variables needed to change prestige to a categorical variable, rather than quantitative, then answer quiz 1 below.

# In[9]:


df.prestige.value_counts()


# In[10]:


df[['prestige 1','prestige 2','prestige 3','prestige 4']] = pd.get_dummies(df.prestige)
df.head()


# `2.` Now, fit a logistic regression model to predict if an individual is admitted using `gre`, `gpa`, and `prestige` with a baseline of the prestige value of `1`.  Use the results to answer quiz 2 and 3 below.  Don't forget an intercept.

# In[11]:


df['intercept'] = 1
model = sm.Logit(df.admit, df[['gre','gpa','prestige 2','prestige 3','prestige 4','intercept']])
results = model.fit()
results.summary()


# In[13]:


print(np.exp(0.7793),'gpa')
print(np.exp(0.0022),'gre')
print(np.exp(-0.6801),'prestige 2')
print(np.exp(-1.3387),'prestige 3')
print(np.exp(-1.5534),'prestige 4')


# In[14]:


print(1/np.exp(-0.6801),'prestige 2')
print(1/np.exp(-1.3387),'prestige 3')
print(1/np.exp(-1.5534),'prestige 4')


# In[ ]:





# In[ ]:




