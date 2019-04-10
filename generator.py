#!/usr/bin/env python
# coding: utf-8

# In[38]:


def scq(max):
    a,b=0,1
    while b<max:
        yield b
        a,b=b,2*b
    return 'done'

for i in scq(1000):
    print(i)


# In[42]:


g=scq(100)
print(next(g))
print(next(g))
print(next(g))
print(next(scq(100)))
print(next(scq(100)))
print(next(scq(100)))


# In[43]:


g1=scq(100)
print(next(g1))
g2=scq(100)
print(next(g2))
g3=scq(100)
print(next(g3))


# In[ ]:




