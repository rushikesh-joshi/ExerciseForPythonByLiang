# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 09:29:31 2018

@author: Rushikesh

I have loop, format and ** (exponent) operator, alternatively you print message with text only.
"""


print ("a \t a² \t a³")

i = 1
while (i < 5):
        print ("{} \t {} \t {}".format(i,i**2, i**3))
        i += 1