#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:58:20 2018

@author: serafim, jonathan and tiago
"""

# Import modules
import numpy as np
import functions

def oracle(learningRate,offset,initialPoint,address,X,Y,Z,W,P,Q,S,T,V):
    
    text = ""
    
    output = 0.0
    
    # Number of hits
    hits = 0
    count = 0
    
    # weights
    weightOne = 0
    weightTwo = 0
    weightThree = 0
    weightFour = 0 
    weightFive = 0
    weightSix = 0
    weightSeven = 0
    weightEight = 0
    weightNine = 0

    # Inputs
    INPUT = [[0,0],[0,1],[1,0],[1,1]]
    x0 = 1.0
    
    # Expected results
    d = [0,1,1,0]
    
    # Number of patterns
    pattern = len(d)
    
    AIij1 = 0
    AYij1 = 0
    
    AIij2 = 0
    AYij2 = 0
    
    AIij3 = 0
    AYij3 = 0
    
    AWij1 = [[0,0,0]]
    AWij2 = [[0,0,0]]
    AWij3 = [[0,0,0]]
     
    for x in range(X[0],X[1]):
        for y in range(Y[0],Y[1]):
            for z in range(Z[0],Z[1]):
                for w in range(W[0],W[1]):
                    for p in range(P[0],P[1]):
                        for q in range(Q[0],Q[1]):
                            for s in range(S[0],S[1]):
                                for t in range(T[0],T[1]):
                                    for v in range(V[0],V[1]):
                    
                                        weightOne = x - initialPoint
                                        weightTwo = y - initialPoint
                                        weightThree = z - initialPoint
                                        weightFour = w - initialPoint 
                                        weightFive = p - initialPoint
                                        weightSix = q - initialPoint
                                        weightSeven = s - initialPoint
                                        weightEight = t - initialPoint
                                        weightNine = v - initialPoint                        
                                        
                                        AWij1[0][0] = weightOne * learningRate[0]
                                        AWij1[0][1] = weightTwo * learningRate[0]
                                        AWij1[0][2] = weightThree * learningRate[0]
                                        
                                        AWij2[0][0] = weightFour * learningRate[0]
                                        AWij2[0][1] = weightFive * learningRate[0]
                                        AWij2[0][2] = weightSix * learningRate[0]
                                        
                                        AWij3[0][0] = weightSeven * learningRate[0]
                                        AWij3[0][1] = weightEight * learningRate[0]
                                        AWij3[0][2] = weightNine * learningRate[0]
                                        
                                        for j in range(pattern):
                                            
                                            # Additive step of the first hidden layer neuron one
                                            AIij1 = x0 *AWij1[0][0] + INPUT[j][0] *AWij1[0][1] + INPUT[j][1] * AWij1[0][2]
                                            AYij1 = functions.sigmoide(AIij1)
                                            
                                            # Additive step of the first hidden layer neuron Two
                                            AIij2 = x0 * AWij2[0][0] + INPUT[j][0] * AWij2[0][1] + INPUT[j][1] * AWij2[0][2]
                                            AYij2 = functions.sigmoide(AIij2)
                                            
                                            # Additive step of the output layer
                                            AIij3 = x0 * AWij3[0][0] + AYij1 * AWij3[0][1] + AYij2 * AWij3[0][2]
                                            AYij3 = functions.sigmoide(AIij3)
                                            
                                            if (AYij3 > 0.9):
                                                output = 1
                                            elif (AYij3 < 0.1):
                                                output = 0
                                            else:
                                                ""
                                                
                                            if (output == d[j]):
                                                hits = hits + 1     
                                        
                                        if (hits == 4):
                                            count += 1
                                            hits = 0
                                            arq = open(address + 'file', 'a')
                                            text = str(weightOne) + " " + str(weightTwo) + " " + str(weightThree) + " " + str(weightFour) + " " + str(weightFive) + " " + str(weightSix)  + " " + str(weightSeven) + " " + str(weightEight) + " " + str(weightNine) + "\n"
                                            arq.write(text)
                                            arq.close()
                                        else:
                                            hits = 0

    return count
