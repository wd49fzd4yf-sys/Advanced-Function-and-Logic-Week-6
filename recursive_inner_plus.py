#!/usr/bin/env python
# coding: utf-8

# In[6]:


def innermost_plus_one_inplace(lst):
    for item in lst:
        if isinstance(item, list):
            innermost_plus_one_inplace(item)
            return
    for i in range(len(lst)):
        lst[i] += 1

input_list = [5, 10, [15, 20, [25, 30]]]
innermost_plus_one_inplace(input_list)    
print(input_list)


# In[ ]:




