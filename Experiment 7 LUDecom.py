import numpy as np

def LUDecomp(A,B,n): 
  
    lower = [[0 for x in range(n)] for y in range(n)] 
    upper = [[0 for x in range(n)] for y in range(n)]

    for i in range(n): 
        for k in range(i, n):  
            sum = 0
            for j in range(i): 
                sum += (lower[i][j] * upper[j][k])   
            upper[i][k] = A[i][k] - sum

        for k in range(i, n): 
            if (i == k): 
                lower[i][i] = 1
            else: 
                sum = 0
                for j in range(i): 
                    sum += (lower[k][j] * upper[j][i])
                lower[k][i] = float((A[k][i] - sum) /upper[i][i])
  
    EquationSolver(lower,upper,B,n)
    
def EquationSolver(L,U,B,n):
    Z = np.linalg.solve(L, B)
    X = np.linalg.solve(U, Z)
    print("L Matrix : ")
    print(L)
    print("\nU Matrix : ")
    print(U)
    print("\nResultant X Matrix : ")
    print(X)
    
A = np.array([[1,4,1],[1,6,-1],[2,-1,2]])
B = np.array([7,13,5])
  
LUDecomp(A,B,3)