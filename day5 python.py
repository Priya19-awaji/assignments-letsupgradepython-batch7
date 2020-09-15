#!/usr/bin/env python
# coding: utf-8

# In[1]:


#WAP FOR CLACULATOR WHICH BRETURNS VALUE RATHER THAN PRINTING THEM

def calci(a,b,ops):
    if ops=="+":
        return a+b
    elif ops=="-":
        return a-b
    elif ops=="*":
        return a*b
    elif ops=="/":
        return a/b
    else:
        return ("no ops specified only +,-,*,/ is possible")
    


# In[2]:


calci(3,4,"+")


# In[ ]:





# In[ ]:




