#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:07:28 2019

@author: jzuluaga
"""
from enum import Enum
import numpy as np

PI=3.14159265359

class Unit(Enum):
    DEG=1
    RAD=2

class Angle(object):
    #Atributos: value, unit
    
    #Métodos
    def __init__(self,value,unit):
        self.value=value
        self.unit=unit
        
    def convertToDeg(self):
        if self.unit==Unit.DEG:
            return self.value
        else:
            return self.value*180/PI
        
    def convertToRad(self):
        if self.unit==Unit.RAD:
            return self.value
        else:
            return self.value*PI/180

def FactorialInteger(n):
    if n<0:
        raise ValueError("Factorial of a negative number")
    elif n<=1:
        return 1
    else:
        return n*FactorialInteger(n-1)

def Sin(angle,N=10):
    """
    angle is an object of the class Angle
    """
    sumSeries=0
    x=angle.convertToRad()
    for n in range(N):
        sumSeries+=(-1)**n*x**(2*n+1)/FactorialInteger(2*n+1)
    return sumSeries    
        
if __name__=="__main__":
    
    theta=Angle(15000,Unit.DEG)
    
    y=Sin(theta)
    
    print(np.sin(theta.convertToRad()))