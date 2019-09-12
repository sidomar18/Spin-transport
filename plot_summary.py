#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 17:53:31 2019

@author: sidomar
"""

import numpy as np
import matplotlib.pyplot as plt
a=4
b=8
x0=3
x=np.linspace(0,10,100)
y=np.zeros(len(x))
for i in x:
    if (i<x0):
        x1=i
        y1=-(a+b)*i
       # plt.plot(x,y1)
    else: 
        x2=i
        y2=-a*x
        #plt.plot(x,y2)
plt.plot(x1,y1)    
plt.plot(x2,y2)    
plt.show()    