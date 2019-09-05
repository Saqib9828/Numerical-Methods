#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:07:16 2019

@author: fist08
"""
def func( x ): 
	return (1/(x**3))

def simpsons( ll, ul, n ): 

	h = ( ul - ll )/n 

	x = list() 
	fx = list() 
	
	i = 0
	while i<= n: 
		x.append(ll + i * h) 
		fx.append(func(x[i])) 
		i += 1

	res = 0
	i = 0
	while i<= n: 
		if i == 0 or i == n: 
			res+= fx[i] 
		elif i % 2 != 0: 
			res+= 4 * fx[i] 
		else: 
			res+= 2 * fx[i] 
		i+= 1
	res = res * (h / 3) 
	return res 
	
lower_limit = 4  
upper_limit = 5.2  
n = 6  
print("%.6f"% simpsons(lower_limit, upper_limit, n)) 
