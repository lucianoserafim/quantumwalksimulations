#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:25:14 2018

This code represents the simulation of the
training of a classical neural network using
a quantum search process.

@author: serafim, jonathan and tiago
"""

# Import modules.
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import oracle
import walking
import functions
from datetime import datetime
import os

pid = os.getpid()

# Parameters
L = 4
l = 1
k = 0


# Calculation of the midpoint
middlePoint = np.int(np.ceil(L/2))

# Relatives values
windowValue = 4
window = [middlePoint-windowValue,middlePoint+windowValue]

# shifts values
offset = 2
initialOffset = [window[0],window[0] + offset]
N = offset**9

# Distance value between positions
learningRate = [0.5]

path = 'address_to_files'
textCount = ""

initialDateTime = datetime.now()
dateTimeExperiment = open(path + 'DateTime', 'a')
dateTimeExperiment.write('startProcess ' + str(pid) + ' ' + str(initialDateTime) + '\n')
dateTimeExperiment.close()

X,Y,Z,W,P,Q,S,T,V = functions.openFileOffset(path,initialOffset)

# Oracle and counting
while (True):
    
    k = oracle.oracle(learningRate,offset,middlePoint,path,X,Y,Z,W,P,Q,S,T,V)
   
    if (k != 0):
        
        returnWalk = walking.walking(N,l,k)
        
        result = functions.roulette(returnWalk)
        
        score = open(path + 'score', 'a')

        textCount = "Solutions:" + str(k) + " offset " + str(offset) + " Measure aa: " + str((result.count(0)*100)/10000) + " Measure ab: " + str((result.count(1)*100)/10000) + " Measure ba: " + str((result.count(2)*100)/10000) + " Measure bb: " + str((result.count(3)*100)/10000)  + " Learning Rate: " + str(learningRate[0]) + " Space: " + str(X) + str(Y) + str(Z) + str(W) + str(P) + str(Q) + str(S) + str(T) + str(V) + "\n"
                
        score.write(textCount)
        score.close()
        
    if (k != 0):
        break
        
    functions.saveCurrentState(path,"auxCurrentState",X,Y,Z,W,P,Q,S,T,V)
    
    if ((X[1] == window[1]) and (Y[1] == window[1]) and (Z[1] == window[1]) and (W[1] == window[1]) and (P[1] == window[1]) and (Q[1] == window[1]) and (S[1] == window[1]) and (T[1] == window[1]) and (V[1] == window[1])):
        break
        
    X,Y,Z,W,P,Q,S,T,V = functions.shiftsRegion(X,Y,Z,W,P,Q,S,T,V,offset,initialOffset,window[1])
    
    functions.saveCurrentState(path,"currentState",X,Y,Z,W,P,Q,S,T,V)
    
finalDateTime = datetime.now()
dateTimeExperiment = open(path + 'DateTime', 'a')
dateTimeExperiment.write('endProcess ' + str(pid) + ' ' + str(finalDateTime) + '\n')
dateTimeExperiment.close()
  

