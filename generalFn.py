import numpy as np
import matplotlib.pyplot as plt

def derivative ( f,x,h):
    return (f(x+h)-f(x))/h

def func(x):
    return 2*np.sin(x)**2 + x

print (derivative(func, 1, 0.0001))

def nDerivative (f,x,h,n):
    t=0
    for k in range (n+1):
        t =t + (-1)**(k+n) * np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)) * f(x+k*h)
    return t/h**n

print(nDerivative(func,1,0.0001,1))