# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 21:24:51 2019

@author: alexius
"""

import  numpy as np
'''
a = np.array([0,1,2,3,5]) 
print(a)
print(type(a))

a[2]
print (a.dtype)

print (a.size)

print (a.ndim) #no of dimensions '''

c = np.array([5,3,7,3,6,3,8,9,0])

c[2] =100

#slicig

d = np.array(c[1:4])

c[3:6] = 12,28,11 #can chage values


