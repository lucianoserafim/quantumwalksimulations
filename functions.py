#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 02:41:38 2018

@author: serafim, jonathan and tiago
"""

import math
import os.path as path
import numpy as np
import random as random
from operator import itemgetter

def sigmoide(x):
  return round(1 / (1 + math.exp(-10*(x-0.5))),10)


def shiftsRegion(shiftsDimX,shiftsDimY,shiftsDimZ,shiftsDimW,shiftsDimP,shiftsDimQ,shiftsDimS,shiftsDimT,shiftsDimV,shiftOffset,inicialShiftOffset,L):
    
    if (shiftsDimV[1] < L):
        shiftsDimV[0] = shiftsDimV[0] + shiftOffset
        shiftsDimV[1] = shiftsDimV[1] + shiftOffset
    elif (shiftsDimT[1] < L):
        shiftsDimT[0] = shiftsDimT[0] + shiftOffset
        shiftsDimT[1] = shiftsDimT[1] + shiftOffset
        shiftsDimV[0] = inicialShiftOffset[0]
        shiftsDimV[1] = inicialShiftOffset[1]
    elif (shiftsDimS[1] < L):
        shiftsDimS[0] = shiftsDimS[0] + shiftOffset
        shiftsDimS[1] = shiftsDimS[1] + shiftOffset
        shiftsDimT[0] = inicialShiftOffset[0]
        shiftsDimT[1] = inicialShiftOffset[1]
        shiftsDimV[0] = inicialShiftOffset[0]
        shiftsDimV[1] = inicialShiftOffset[1]
    elif (shiftsDimQ[1] < L):
        shiftsDimQ[0] = shiftsDimQ[0] + shiftOffset
        shiftsDimQ[1] = shiftsDimQ[1] + shiftOffset
        shiftsDimS[0] = inicialShiftOffset[0]
        shiftsDimS[1] = inicialShiftOffset[1]
        shiftsDimT[0] = inicialShiftOffset[0]
        shiftsDimT[1] = inicialShiftOffset[1]
        shiftsDimV[0] = inicialShiftOffset[0]
        shiftsDimV[1] = inicialShiftOffset[1]
    elif (shiftsDimP[1] < L):
        shiftsDimP[0] = shiftsDimP[0] + shiftOffset
        shiftsDimP[1] = shiftsDimP[1] + shiftOffset
        shiftsDimQ[0] = inicialShiftOffset[0]
        shiftsDimQ[1] = inicialShiftOffset[1]
        shiftsDimS[0] = inicialShiftOffset[0]
        shiftsDimS[1] = inicialShiftOffset[1]
        shiftsDimT[0] = inicialShiftOffset[0]
        shiftsDimT[1] = inicialShiftOffset[1]
        shiftsDimV[0] = inicialShiftOffset[0]
        shiftsDimV[1] = inicialShiftOffset[1]
    elif (shiftsDimW[1] < L):
        shiftsDimW[0] = shiftsDimW[0] + shiftOffset
        shiftsDimW[1] = shiftsDimW[1] + shiftOffset
        shiftsDimP[0] = inicialShiftOffset[0]
        shiftsDimP[1] = inicialShiftOffset[1]
        shiftsDimQ[0] = inicialShiftOffset[0]
        shiftsDimQ[1] = inicialShiftOffset[1]
        shiftsDimS[0] = inicialShiftOffset[0]
        shiftsDimS[1] = inicialShiftOffset[1]
        shiftsDimT[0] = inicialShiftOffset[0]
        shiftsDimT[1] = inicialShiftOffset[1]
        shiftsDimV[0] = inicialShiftOffset[0]
        shiftsDimV[1] = inicialShiftOffset[1]
    elif (shiftsDimZ[1] < L):
        shiftsDimZ[0] = shiftsDimZ[0] + shiftOffset
        shiftsDimZ[1] = shiftsDimZ[1] + shiftOffset
        shiftsDimW[0] = inicialShiftOffset[0]
        shiftsDimW[1] = inicialShiftOffset[1]
        shiftsDimP[0] = inicialShiftOffset[0]
        shiftsDimP[1] = inicialShiftOffset[1]
        shiftsDimQ[0] = inicialShiftOffset[0]
        shiftsDimQ[1] = inicialShiftOffset[1]
        shiftsDimS[0] = inicialShiftOffset[0]
        shiftsDimS[1] = inicialShiftOffset[1]
        shiftsDimT[0] = inicialShiftOffset[0]
        shiftsDimT[1] = inicialShiftOffset[1]
        shiftsDimV[0] = inicialShiftOffset[0]
        shiftsDimV[1] = inicialShiftOffset[1]
    elif (shiftsDimY[1] < L):
        shiftsDimY[0] = shiftsDimY[0] + shiftOffset
        shiftsDimY[1] = shiftsDimY[1] + shiftOffset
        shiftsDimZ[0] = inicialShiftOffset[0]
        shiftsDimZ[1] = inicialShiftOffset[1]
        shiftsDimW[0] = inicialShiftOffset[0]
        shiftsDimW[1] = inicialShiftOffset[1]
        shiftsDimP[0] = inicialShiftOffset[0]
        shiftsDimP[1] = inicialShiftOffset[1]
        shiftsDimQ[0] = inicialShiftOffset[0]
        shiftsDimQ[1] = inicialShiftOffset[1]
        shiftsDimS[0] = inicialShiftOffset[0]
        shiftsDimS[1] = inicialShiftOffset[1]
        shiftsDimT[0] = inicialShiftOffset[0]
        shiftsDimT[1] = inicialShiftOffset[1]
        shiftsDimV[0] = inicialShiftOffset[0]
        shiftsDimV[1] = inicialShiftOffset[1]
    elif (shiftsDimX[1] < L):
        shiftsDimX[0] = shiftsDimX[0] + shiftOffset
        shiftsDimX[1] = shiftsDimX[1] + shiftOffset
        shiftsDimY[0] = inicialShiftOffset[0]
        shiftsDimY[1] = inicialShiftOffset[1]
        shiftsDimZ[0] = inicialShiftOffset[0]
        shiftsDimZ[1] = inicialShiftOffset[1]
        shiftsDimW[0] = inicialShiftOffset[0]
        shiftsDimW[1] = inicialShiftOffset[1]
        shiftsDimP[0] = inicialShiftOffset[0]
        shiftsDimP[1] = inicialShiftOffset[1]
        shiftsDimQ[0] = inicialShiftOffset[0]
        shiftsDimQ[1] = inicialShiftOffset[1]
        shiftsDimS[0] = inicialShiftOffset[0]
        shiftsDimS[1] = inicialShiftOffset[1]
        shiftsDimT[0] = inicialShiftOffset[0]
        shiftsDimT[1] = inicialShiftOffset[1]
        shiftsDimV[0] = inicialShiftOffset[0]
        shiftsDimV[1] = inicialShiftOffset[1]
        
    return shiftsDimX,shiftsDimY,shiftsDimZ,shiftsDimW,shiftsDimP,shiftsDimQ,shiftsDimS,shiftsDimT,shiftsDimV

def openFileOffset(address,openFileOffset):
    
    textX = ""
    textY = ""
    textZ = ""
    textW = ""
    textP = ""
    textQ = ""
    textS = ""
    textT = ""
    textV = ""
    
    openFileDimx = [openFileOffset[0],openFileOffset[1]] 
    openFileDimy = [openFileOffset[0],openFileOffset[1]] 
    openFileDimz = [openFileOffset[0],openFileOffset[1]] 
    openFileDimw = [openFileOffset[0],openFileOffset[1]]
    openFileDimp = [openFileOffset[0],openFileOffset[1]] 
    openFileDimq = [openFileOffset[0],openFileOffset[1]] 
    openFileDims = [openFileOffset[0],openFileOffset[1]] 
    openFileDimt = [openFileOffset[0],openFileOffset[1]] 
    openFileDimv = [openFileOffset[0],openFileOffset[1]]
    
    existe = path.exists(address + 'currentState')
    if (existe == False):
        currentState = open(address + 'currentState', 'w')
        text = str(openFileDimx[0]) + " " + str(openFileDimx[1]) + "\n" + str(openFileDimy[0]) + " " + str(openFileDimy[1]) + "\n" +str(openFileDimz[0]) + " " + str(openFileDimz[1]) + "\n" + str(openFileDimw[0]) + " " + str(openFileDimw[1]) + "\n" + str(openFileDimp[0]) + " " + str(openFileDimp[1]) + "\n" + str(openFileDimq[0]) + " " + str(openFileDimq[1]) + "\n" + str(openFileDims[0]) + " " + str(openFileDims[1]) + "\n" + str(openFileDimt[0]) + " " + str(openFileDimt[1]) + "\n" + str(openFileDimv[0]) + " " + str(openFileDimv[1])
        currentState.write(text)
        currentState.close()
        
        auxCurrentState = open(address + 'auxCurrentState', 'w')
        auxCurrentState.write(text)
        auxCurrentState.close()
    else:
        f = open(address + 'currentState','r')
        f = f.readlines()
        if (f == []):
            f = open(address + 'auxCurrentState','r')
            f = f.readlines()
            if (f == []):
                textX = [str(openFileOffset[0]),str(openFileOffset[1])]
                textY = [str(openFileOffset[0]),str(openFileOffset[1])]
                textZ = [str(openFileOffset[0]),str(openFileOffset[1])]
                textW = [str(openFileOffset[0]),str(openFileOffset[1])]
                textP = [str(openFileOffset[0]),str(openFileOffset[1])]
                textQ = [str(openFileOffset[0]),str(openFileOffset[1])]
                textS = [str(openFileOffset[0]),str(openFileOffset[1])]
                textT = [str(openFileOffset[0]),str(openFileOffset[1])]
                textV = [str(openFileOffset[0]),str(openFileOffset[1])]
            else:
                textX = f[0].split()
                textY = f[1].split()
                textZ = f[2].split()
                textW = f[3].split()
                textP = f[4].split()
                textQ = f[5].split()
                textS = f[6].split()
                textT = f[7].split()
                textV = f[8].split()
        else:
            textX = f[0].split()
            textY = f[1].split()
            textZ = f[2].split()
            textW = f[3].split()
            textP = f[4].split()
            textQ = f[5].split()
            textS = f[6].split()
            textT = f[7].split()
            textV = f[8].split()
            
        openFileDimx[0] = np.int(textX[0])
        openFileDimx[1] = np.int(textX[1])
        openFileDimy[0] = np.int(textY[0])
        openFileDimy[1] = np.int(textY[1])
        openFileDimz[0] = np.int(textZ[0])
        openFileDimz[1] = np.int(textZ[1])
        openFileDimw[0] = np.int(textW[0])
        openFileDimw[1] = np.int(textW[1])
        openFileDimp[0] = np.int(textP[0])
        openFileDimp[1] = np.int(textP[1])
        openFileDimq[0] = np.int(textQ[0])
        openFileDimq[1] = np.int(textQ[1])
        openFileDims[0] = np.int(textS[0])
        openFileDims[1] = np.int(textS[1])
        openFileDimt[0] = np.int(textT[0])
        openFileDimt[1] = np.int(textT[1])
        openFileDimv[0] = np.int(textV[0])
        openFileDimv[1] = np.int(textV[1])
    
    
    return openFileDimx,openFileDimy,openFileDimz,openFileDimw,openFileDimp,openFileDimq,openFileDims,openFileDimt,openFileDimv

def roulette(system):
    
    individuals = {system[0][1]**2 : 0, system[1][1]**2 : 1, system[2][1]**2 : 2, system[3][1]**2 : 3}
    individuals = sorted(individuals.items(), key=itemgetter(0))
    result = []
    
    for repetition in range(10000):
        
        randomValue = random.random()
        accumulatedValue = 0
        
        for individual in individuals:
            accumulatedValue = accumulatedValue + individual[0]
            
            if (accumulatedValue >= randomValue):
                result.append(individual[1])
                break
                
            
    return result

def saveCurrentState(address,file,X,Y,Z,W,P,Q,S,T,V):
    
    auxCurrentState = open(address + file, 'w')
    currentStateText = str(X[0]) + " " + str(X[1]) + "\n" + str(Y[0]) + " " + str(Y[1]) + "\n" +str(Z[0]) + " " + str(Z[1]) + "\n" + str(W[0]) + " " + str(W[1]) + "\n" + str(P[0]) + " " + str(P[1]) + "\n" + str(Q[0]) + " " + str(Q[1]) + "\n" + str(S[0]) + " " + str(S[1]) + "\n" + str(T[0]) + " " + str(T[1]) + "\n" + str(V[0]) + " " + str(V[1])
    auxCurrentState.write(currentStateText)
    auxCurrentState.close()