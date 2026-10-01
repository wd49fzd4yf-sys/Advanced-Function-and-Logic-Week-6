#!/usr/bin/env python
# coding: utf-8

# In[1]:


def filter_numbers(numbers, threshold):
    result = []
    for num in numbers:
        if num <= threshold:
            result.append(num)
    return result

my_numbers = [5, 10, 15, 20, 25, 30]
user_threshold = float(input("Enter a threshold value: "))

filtered = filter_numbers(my_numbers, user_threshold)
print("Original list:", my_numbers)
print("numbers <= threshold:", filtered)


# In[ ]:




