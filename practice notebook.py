#!/usr/bin/env python
# coding: utf-8

# In[3]:


# SIMPLY HOW TO PRINT
print("asi kya gov")


# In[4]:


'asi chi naari camp gasaan'


# In[12]:


import numpy as np
s=np.random.normal(25.0, 5.0, 10)
print (s)


# In[30]:


#LISTS
x=[7,5,6,2,8,9,1,2,5]
print(len(x))


# In[34]:


x[:3]


# In[36]:


x[3:]


# In[40]:


x[:-2]


# In[44]:


x.extend([11,12])
x


# In[48]:


x.append(13)
x


# In[56]:


y=[100,90,80,50,32,67,89,57,45,77]
z=[x,y]
z


# In[9]:


m=[2,6,8,1]
m.sort()
m


# In[10]:


m.sort(reverse=True) 
m


# In[16]:


# TUPLES
x=(2,4,6,8)
len(x)


# In[15]:


x[3]


# In[21]:


y=[1,2,3,45]
z=[x,y]
z


# In[30]:


(length,width)="322,12".split(',')
print(length ,width)


# In[32]:


# DICTIONARIES
laptop={'brand':'LENOVO','processor':'AMD RYZEN 7','ram':'512 MB'}
print(laptop)    
# if you want to just simply print everything


# In[36]:


# if you want to print only specific thing
print(laptop['ram'])
# TO SPECIFY THE KEY I WANT TO ACCESS I CAN PUT THE SQUARE BRACKETS AND THE TYPE THE NAME OF THE KEY YOU WANT TO ACCESS


# In[37]:


#if you want to print a key which is not present in dictionary
print(laptop['harddrive'])


# In[38]:


# WE DONT WANT THE UGLY ERROR ABOVE
# ALL WE WANT A FANCY ERROR SO WE USE GET
print(laptop.get('harddrive'))


# In[42]:


#if we want to see keys and values  
print(laptop.keys())
print(laptop.values())
print(laptop.items())


# In[45]:


# if we want to use loop
for keys,values in laptop.items():
    print(keys ,values)
#     REST SEARCH FROM INTERNET


# In[49]:


# FUNCTION
# HERE WE JUST DECLARE A SIMPLE FUNCTION
def cube(x):
    return x*x*x
print(cube(2))


# In[48]:


# HOW WE CAN DECLARE FUNCTION UNDER FUNCTION
def triplecube(f,x):
    return f(x)
print(triplecube(cube,3))


# In[57]:


# LAMBDA FUNCTION
print(triplecube(lambda x: x*x*x*x,6))


# In[ ]:




