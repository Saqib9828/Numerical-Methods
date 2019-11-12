import math 
from scipy.integrate import quad

invexp = lambda x: math.log(x)

def simpsons_( a, b, n ):
    h = ( b - a )/n
    x = [a + i * h for i in range(n)]
    y = [invexp(x[i]) for i in range(n)]
    res = [y[j] if (j==0 or j==n) else 4*y[j] if j%2 !=0 else 2*y[j] for j in range(len(y))]
    total = sum(res)
    return (total*(h/3))
    
lower = 4
upper = 5.2
n = 6

I1 = simpsons_(lower, upper, n)
print("Value using User Defined Function:",I1)

I2 = quad(invexp,lower,upper)
print("Value using Library Function:",I2[0])

print("Difference between Functions:{:0.10f}".format(abs(I1-I2[0])))