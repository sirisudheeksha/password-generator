#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string


class Password(object):
    """
    perform the random password generator
    """

    
    def generate_pass():
        return ''.join(random.choice(string.ascii_letters + string.digits + ".',={}[]-/|\£$%^&*()_+~#@?><") for _ in range(10))


def user_request():
    # request user pass and store user response
    user_req = input("New Password?")
    # call generate pass
    user_req = user_req.upper()
    if user_req == "Y" or user_req == "YES":
        return Password.generate_pass()

print(user_request())


# In[ ]:




