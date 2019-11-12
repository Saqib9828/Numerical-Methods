import numpy as np
import math

def conjGrad(A,x,b,tol=0.001):
	n = len(b)
	r = b - np.dot(A,x)
	s = r.copy()
	for i in range(0,n):
		u = np.dot(A,s)
		alpha = np.dot(s,r)/np.dot(s,u)
		x = x + alpha*s
		r = b - np.dot(A,x)
		if(math.sqrt(np.dot(r,r))) < tol:
			break
		else:
			beta = -np.dot(r,u)/np.dot(s,u)
			s = r + beta*s
	return x

A = np.array([[4,-1,1],[-1,4,-2],[1,-2,4]])
b = np.array([12,-1,5])
x = np.zeros(3)
soltn = conjGrad(A,x,b)
print(soltn)
