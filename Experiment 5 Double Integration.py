#find double integration using simpsons 1/3rd rule
from scipy import integrate
dblfx = lambda y,x: (x**3)-(y**2)

def empty_matrix(n,m):
    empty_mtx=[[0 for i in range(n+1)] for j in range(m+1)]
    return empty_mtx

def matcof(n,m):
    L=[1 if (j==0 or j==n) else 4 if j%2 !=0 else 2 for j in range(n+1)]
    M=L
    mat_lm = empty_matrix(n,m)
    for i in range(n+1):
        for j in range(m+1):
            mat_lm[i][j] = M[i]*L[j]
    return mat_lm

def fxy_cal(n,m,xlist,ylist):
    mat_fxy= empty_matrix(n,m)    
    for i in range(n+1):
        for j in range(m+1):
            mat_fxy[i][j] = dblfx(ylist[i],xlist[j])
    return mat_fxy

def result(a1,b1,a2,b2,n,m):
    h = (b1-a1)/float(n)
    k = (b2-a2)/float(m)
    xlist = [a1 + i * h for i in range(n+1)]
    ylist = [a2 + i * k for i in range(m+1)]
    res=0
    mat_cof = matcof(n,m)
    mat_fxy = fxy_cal(n,m,xlist,ylist)
    for i in range(n+1):
        for j in range(m+1):
            res+= mat_cof[i][j] * mat_fxy[i][j]
    res = res* (h*k)/9.0
    return res

answer = result(-1,1,-1,1,4,4)
answerLib = integrate.dblquad(dblfx, -1, 1, lambda x: -1, lambda x: 1)[0]
print('Double Integration using Library Function = :{:1.4f}'.format(answerLib))
print('Double Integration using My Function = :{:1.4f}'.format(answer))