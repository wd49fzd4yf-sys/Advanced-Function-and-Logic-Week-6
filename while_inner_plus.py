#!/usr/bin/env python
# coding: utf-8

# In[8]:


input_list = [5, 10, [15, 20, [25, 30]]]

current = input_list
# Keep going deeper while the current list still contains a list
while any(isinstance(item, list) for item in current):
    for item in current:
        if isinstance(item, list):
            current = item # step into the nested list
            break

result = [num + 1 for num in current]
print(result)


# In[ ]:




