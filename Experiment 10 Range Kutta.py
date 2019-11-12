def lorenz_ode_test ( ):
  n = 20000
  t, x, y, z = lorenz_ode_compute ( n )
  lorenz_ode_plot_3d ( n, t, x, y, z )
  return

def lorenz_ode_compute ( n ):

  import numpy as np
  t_final = 40.0
  h = t_final / n

  t = np.linspace ( 0.0, t_final, n + 1 )

  x = np.zeros ( n + 1 )
  y = np.zeros ( n + 1 )
  z = np.zeros ( n + 1 )

  x[0] =1.0
  y[0] = 1.0
  z[0] = 1.0
  for j in range ( 0, n ):

    xyz = np.array ( [ x[j], y[j], z[j] ] )
    xyz = rk4vec ( t[j], 3, xyz, h, lorenzEQ )

    x[j+1] = xyz[0]
    y[j+1] = xyz[1]
    z[j+1] = xyz[2]

  return t, x, y, z

def lorenz_ode_plot_3d ( n, t, x, y, z ):

  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  
  fig = plt.figure ( )
  ax = fig.gca ( projection = '3d' )
  ax.plot ( x, y, z, linewidth = 2, color = 'b' )
  ax.grid ( True )
  ax.set_xlabel ( '<--- X(T) --->' )
  ax.set_ylabel ( '<--- Y(T) --->' )
  ax.set_zlabel ( '<--- Z(T) --->' )
  ax.set_title ( 'Lorenz 3D Plot' )
  plt.show ( )

  return

def lorenzEQ ( t, m, xyz ):

  import numpy as np

  beta = 8.0 / 3.0
  rho = 28.0
  sigma = 10.0

  dxdt = np.zeros ( 3 )

  dxdt[0] = sigma * ( xyz[1] - xyz[0] )
  dxdt[1] = xyz[0] * ( rho - xyz[2] ) - xyz[1]
  dxdt[2] = xyz[0] * xyz[1] - beta * xyz[2]

  return dxdt

def rk4vec ( x0, m, u0, h, lorenzEQ ):
  f0 = lorenzEQ ( x0, m, u0 )

  k1 = x0 + h / 2.0
  l1 = u0 + h * f0 / 2.0
  m1 = lorenzEQ ( k1, m, l1 )

  k2 = x0 + h / 2.0
  l2 = u0 + h * m1 / 2.0
  m2 = lorenzEQ ( k2, m, l2 )

  k3 = x0 + h
  l3 = u0 + h * m2
  m3 = lorenzEQ ( k3, m, l3 )

  k = u0 + h * ( f0 + 2.0 * m1 + 2.0 * m2 + m3 ) / 6.0

  return k

lorenz_ode_test ( )


