#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:26:31 2019

@author: fist08
"""

#---------------------------------
def f( x ):
    return (1/(x**3))
     
def simpson(l, r):
    return (r-l)/6*(f(l)+4*f((l+r)/2)+f(r))

def calc(l, r, ans):
    m=(l+r)/2
    x=simpson(l,m)
    y=simpson(m,r)
    if(abs(x+y-ans)<eps):
        return x+y
	return calc(l,m,x) + calc(m,r,y)

eps=0.01
L=4
R=5.2
print("Ans=%.6f"% calc(L,R,simpson(L,R)))