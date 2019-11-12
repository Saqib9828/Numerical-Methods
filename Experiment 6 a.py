from scipy import integrate
import numpy as np

f1 = lambda x: np.exp(-x**2)
res1 = integrate.quad(f1, -5, 5)[0]
print(res1)

import matplotlib.pyplot as plt
Y = np.arange(-5,5,0.1)
X=[]
X = [np.exp(-i**2) for i in Y ]
plt.plot(Y,X)
plt.xlabel("Values of X")
plt.ylabel("Values of fX")
