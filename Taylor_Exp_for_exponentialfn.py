import numpy as np
import matplotlib.pyplot as plt

def expTaylor(x,x0, nmax):
        t =0
        for n in range(nmax+1):
            t = t+ np.exp(x0) * (x-x0)**n / np.math.factorial(n)
        return t

expTaylor(2,0,10) #7.388994708994708

print( np.exp(2)) #7.38905609893065

plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-5,100])

x_list= np.linspace(-5,5,101)
plt.scatter(x_list, np.exp(x_list))

nmax= 10
plt.plot(x_list, expTaylor(x_list,0,nmax), 'blue')
plt.show()


