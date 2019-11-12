import numpy as np

def TDMA(c, d, e, b):
    n = len(b)
    for i in range(1, n):
        q = c[i-1]/d[i-1]
        d[i] = d[i] - q*e[i-1] 
        b[i] = b[i] - q*b[i-1]
        	    
    x = d
    x[-1] = b[-1]/d[-1]

    for i in range(n-2, -1, -1):
        x[i] = (b[i]-e[i]*x[i+1])/d[i]

    return x

c = np.array([-1,-1,-1,-1]) 
d = np.array([2,2,2,2,2])
e = np.array([-1,-1,-1,-1]) 
b = np.array([5,-5,4,-5,5])

print (TDMA(c, d, e, b))

#Tridiagonal Array :
#    [  2 -1  0  0  0 ]             [ 5]
#    [ -1  2 -1  0  0 ]             [-5]
#    [  0 -1  2 -1  0 ]             [ 4]
#    [  0  0 -1  2 -1 ]             [-5]
#    [  0  0  0 -1  2 ]    with B = [ 5]


#Output [ 2 -1  1 -1  2]
