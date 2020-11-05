#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:03:50 2018

@author: serafim, jonathan and tiago
"""

# Import modules.
from math import sqrt
import numpy as np
import operators

def walking(N,l,k):

    # Initial state preparation
    aa = []
    ab = []
    ba = []
    bb = []
    
    aa.append(0)
    ab.append(0)
    ba.append(0)
    bb.append(0)
    
    aa.append((1/N)*(k))
    ab.append((1/N)*sqrt((k*(N-k))))
    ba.append((1/N)*sqrt((k*(N-k))))
    bb.append((1/N)*(N-k))
    
    psi = [aa,ab,ba,bb]
                
    # Number of applications of U
    runtimes = np.int((np.pi/sqrt(4*k+2*l-2))*sqrt(N))       
    
    # U operator
    U = operators.shift(N,l,k)
    
    # Walking
    for t in range(runtimes):
        
        psi_0 = U[0][0]*psi[0][1] + U[0][1]*psi[1][1] + U[0][2]*psi[2][1] + U[0][3]*psi[3][1]
        psi_1 = U[1][0]*psi[0][1] + U[1][1]*psi[1][1] + U[1][2]*psi[2][1] + U[1][3]*psi[3][1]
        psi_2 = U[2][0]*psi[0][1] + U[2][1]*psi[1][1] + U[2][2]*psi[2][1] + U[2][3]*psi[3][1]
        psi_3 = U[3][0]*psi[0][1] + U[3][1]*psi[1][1] + U[3][2]*psi[2][1] + U[3][3]*psi[3][1]
    
        psi[0][1] = psi_0
        psi[1][1] = psi_1
        psi[2][1] = psi_2
        psi[3][1] = psi_3
        
    return psi
