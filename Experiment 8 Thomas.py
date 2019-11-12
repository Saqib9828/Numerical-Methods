import numpy as np
A=np.array([[2.0,-1,0,0,0],[-1.0,2,-1,0,0],[0,-1,2.0,-1,0] ,[0,0,-1,2.0,-1],[0,0,0,-1,2.0]],dtype=float)
a=np.array([-1,-1,-1,-1])
c=np.array([-1,-1,-1,-1])
d=np.array([2,2,2,2,2])
b=np.array([5,-5,4,-5,5])
x=np.array([0,0,0,0,0])
n=len(d)
def decompose(a,b,c,d):
    a[0]=a[0]/d[0]
    b[0]=b[0]/d[0]
    d[0]=1
    for k in range(n-2):
        a[k+1]=a[k+1]/(d[k+1]-a[k]*c[k])
        b[k+1]=b[k+1]/(d[k+1]-a[k]*c[k])
    
    d[n-1]=d[k-1]-(a[k-2]*c[k-2])
    b[n-1]=b[n-1]/d[n-1]
    return a,b,
def evaluate(a,b,x):

    x[n-1]=b[n-1]
    for k in range (n-2,-1,-1):
        x[k]=(b[k]-a[k]*x[k+1])/d[k]
    return x
a,b=decompose(a,b,c,d)
x=evaluate(a,b,x)  
print(x)     