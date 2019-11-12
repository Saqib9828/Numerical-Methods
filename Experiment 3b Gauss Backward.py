import math

def cal_u(u, n): 

	temp = u 
	for i in range(1, n): 
		temp = temp * (u - i)
	return temp

n = 5
x = [ 21,25,29,33,37 ]
ym = [18.4708,17.8144,17.1070,16.3432,15.5154]
find_this = 30

y = [[0 for i in range(n)] for j in range(n)]

for j in range(n):
    y[j][0]= ym[j]

for i in range(1, n):
    for j in (n-1, 1, -1):
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

sum = y[n-1][0]
u = (find_this - x[n-1]) / (x[1] - x[0])

for i in range(1,n):
	sum = sum + (cal_u(u, i) * y[n - 1][i]) / math.factorial(i)

print("\nValue of y at x =", find_this,"is", round(sum, 5))