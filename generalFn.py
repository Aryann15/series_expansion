import numpy as np
import matplotlib.pyplot as plt

def derivative ( f,x,h):
    return (f(x+h)-f(x))/h

def func(x):
    return 2*np.sin(x)**2 + x

#print (derivative(func, 1, 0.0001))

def nDerivative (f,x,h,n):
    t=0
    for k in range (n+1):
        t =t + (-1)**(k+n) * np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)) * f(x+k*h)
    return t/h**n

#print(nDerivative(func,1,0.0001,1))

def taylorExp(f,x,x0,nmax,h):
    t= 0
    for n in range(nmax + 1):
        t= t+ nDerivative(f,x0,h,n) * (x-x0)**n / np.math.factorial(n)
    return t

plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-8,8])

x_list = np.linspace(-5,5,101)
plt.scatter(x_list, func(x_list))
plt.plot(x_list,taylorExp(func, x_list,0,25,0.05),'red')
plt.plot(x_list,taylorExp(func, x_list,2,15,0.05),'green')
plt.plot(x_list,taylorExp(func, x_list,4,5,0.05),'blue')
plt.show()
