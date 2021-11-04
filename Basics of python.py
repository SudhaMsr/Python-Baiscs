#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
# 
# ## Features of python:
# * Python is a programming language
# * High-level, Simple and General purpose language
# * Used for software development
# * Used for web development
# * Used for maths
# * Open source
# * Dynamic nature
# * Object oriented programming
# 
# ### Compiler:
#  * Converts high-level language to low-level-language
#  
# ### Interpreter:
# * High-level language to machine level language.
#   
#   Although similar to a compiler, the way that code is executed is different for both.
#   
# ### Kaggel:
# * It is an online community of data scientists and machine learning practitioners.
# * Collection of datasets.
# * https://www.kaggle.com/datasets

# ## Table of Contents:-
# 
# * Installation of python
#    1. Anaconda individual version-https://www.anaconda.com/products/individual
#    2. Syntax of python
#    3. Indentation of python
#    4. Comments
#    5. Variables
#    6. Primitive Data types of python
#    7. Python numbers
#    8. Conversion of data types
#    9. Strings
#    10. Boolean-True or False
#    11. Python lists
#    12. Python tuples
#    13. Python sets
#    14. Python Dictionaries
#    15. Conditional statements
#    16. Python loops
#    17. Python collection Functions and range functions
#    18. Python lambda
#    19. Python arrays
#    20. Python iterations
#    

# # Sytanx of python:

# In[1]:


print("Hello, Reader!")


# # Indentation:
# *  To specify the codes we use whitespace i.e spaces and tabs.
# * It improves the readablity of code

# ### Example:-

# In[2]:


def my_function(): 
    print("Hello World")
my_function()


# ![](indentation_error.jpg)

# # Indentation error:-
# 

# In[3]:


from IPython.display import Image
Image("Desktop\indentation_error.jpg")


# # Comments:
# * There are two different types of commenting in python
#    
#    * Single-line Commenting
#    
#    * Multi-line Commenting
# * To exaplian the code
# * To make it more readable
# * Used to prevent execution

# In[4]:


#Single-line commenting
print("Hello, world!")


# In[5]:


#Multi-line commenting
#Multi-line commenting
#Multi-line commenting
if 5 > 2:
    print("five is greater than 2")


# In[6]:


"""Multiline commenting
 Multiline commenting
 Multiline commenting"""
if 5 > 2:
    print("five is greater than 2")

