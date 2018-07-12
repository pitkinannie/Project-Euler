
# coding: utf-8

# ### Problem 1 
# #### Multiples of 3 and 5

# In[2]:


a, b = 3, 5

def mult(x, l = 1000):

    p = l / (2 * x)
    r = l % x
    if(r == 0):
        z = l
        p -= 1
        s = (z * p) + (l / 2)
    elif(r % 2 != 0):
        z = l - r
        p += 1
        s = (z * p)
    else: 
        z = l + (x - r)
        s = (z * p)
    return s

f = mult(a) + mult(b) - mult(a*b)
print(f) 

