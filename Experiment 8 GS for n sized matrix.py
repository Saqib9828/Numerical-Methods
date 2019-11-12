import numpy as np
A = np.array([[4, -1, 1], [-1, 4, -2], [1, -2, 4]])
B = np.array([12, -1, 5])
n = len(B)
X= np.zeros(n)
while True:
    for i in range(n):
        sum=0
        for j in range(n):
            if(i!=j):
                sum = float(sum+A[i][j]*X[j])
        X[i] = float((B[i]-sum)/A[i][i])
    if(X[i]==X[i-1]):
        break
print(X)


#output = [2.995,0.993,0.998]