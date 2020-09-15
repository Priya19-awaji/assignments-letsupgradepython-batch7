#!/usr/bin/env python
# coding: utf-8

# In[8]:


#MAKE A FUNCTION FOR PRIME NUMBERS AND USE FILTERS TO FILTER OUT ALL THE PRIME NUMBERS FROM 1-2500
def isPrime(x):
    for n in range(2,x):
        if x%n==0:
             return False
        else:
            return True
                            
fltrObj=filter(isPrime,range(2500))
print ('Prime numbers between 1-2500:', list(fltrObj))


# In[ ]:





# In[ ]:




