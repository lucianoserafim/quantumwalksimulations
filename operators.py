#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 01:27:15 2018

@author: serafim, jonathan and tiago
"""

# Import modules.
from math import sqrt
import numpy as np

def shift(N,l,k):
    
    costheta = (N-(2*k)-l+1)/(N+l-1)
    sintheta = (2*(sqrt((N-k)*(k+l-1))))/(N+l-1)
    cosphi = (N-(2*k)+l-1)/(N+l-1)
    sinphi = (2*(sqrt(k*(N-k+l-1))))/(N+l-1)
    
    return np.array([[costheta,-sintheta,0,0],
                  [0,0,-cosphi,sinphi],
                  [-sintheta,-costheta,0,0],
                  [0,0,sinphi,cosphi]])   
        