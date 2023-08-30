import numpy as np
import matplotlib.pyplot as plt

def derivative ( f,x,h):
    return (f(x+h)-f(x))/h

def func(x):
    return 2*np.sin(x)**2 + x

print (derivative(func, 1, 0.0001))