import numpy as np
import matplotlib.pyplot as plt

def sinTaylor(x,x0, nmax):
        t =0
        for n in range(nmax+1):
            t = t+ (-1)**n * x**(2*n+1)/ np.math.factorial (2*n +1)
        return t

plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-2,2])

x_list= np.linspace(-10,10,101)
plt.scatter(x_list, np.sin(x_list))

plt.plot(x_list, sinTaylor(x_list,0,3), 'blue')
plt.plot(x_list, sinTaylor(x_list,0,6), 'red')
plt.plot(x_list, sinTaylor(x_list,0,9), 'green')

plt.show()


