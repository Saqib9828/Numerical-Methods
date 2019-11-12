import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.array([0.15,2.30,3.15,4.85,6.25,7.95])
y = np.array([4.79867,4.49013,4.2243,3.47313,2.66674,1.51909])
xnew = 4.3

# Linear Interpolation
fi = interp1d(x, y)
yi = fi(xnew)
plt.plot(x, y, 'bo', xnew, yi, 'ro',linestyle='--', linewidth=2)
plt.show()

# Cubic Spline
fc = interp1d(x, y,kind= 'cubic')
yc = fc(xnew)
plt.plot(x, y, 'bo', xnew, yc, 'ro',linestyle='-', linewidth=2)
plt.show()

# Comparision Part
print('{:.10f} is the value of x at y = 4.3 using Linear Interpolation'.format(yi))
print('{:.10f} is the value of x at y = 4.3 using Cubic  Spline'.format(yc))