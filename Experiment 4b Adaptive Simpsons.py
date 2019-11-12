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
  
def Adap_Simpsons(calculated,actual,low,high,n=2):
    while calculated-actual < -0.00001:
        calculated = simpsons_(low, high,n)
        n= 2*n-1
    return calculated

lower = 4
middle = 4.6
upper = 5.2

#Normal Integration
First_Actual = quad(invexp,lower,middle)[0]
Second_Actual = quad(invexp,middle,upper)[0]
Final_Actual = First_Actual+Second_Actual

#Adaptive Integration
First_Cal,Second_Cal = 0,0
First_Cal = Adap_Simpsons(First_Cal,First_Actual,lower,middle)
Second_Cal = Adap_Simpsons(Second_Cal,Second_Actual,middle,upper)
Final_Cal = First_Cal+Second_Cal

print("Normal Integration:{:0.7f}".format(Final_Actual))
print("Adaptive Simpsons Integration:{:0.7f}".format(Final_Cal))
print("Error:{:0.7f}".format(abs(Final_Cal-Final_Actual)))

