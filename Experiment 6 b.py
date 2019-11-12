from scipy import integrate
import numpy as np

f2 = lambda x,a=1,b=2,c=3:a*(np.exp(-((x-b)/c)**2))
res2 = integrate.quad(f2, -5, 5)[0]
print(res2)

import matplotlib.pyplot as plt
Y = np.arange(-5,5,0.1)
X=[]
a = 1;b = 2;c = 3;
X = [a*(np.exp(-((i-b)/c)**2)) for i in Y ]

plt.plot(Y,X)
plt.xlabel("Values of X")
plt.ylabel("Values of fX")