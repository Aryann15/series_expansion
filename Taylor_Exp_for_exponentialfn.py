import numpy as np
import matplotlib.pyplot as plt

def expTaylor(x,x0, nmax):
        t =0
        for n in range(nmax+1):
            t = t+ np.exp(x0) * (x-x0)**n / np.math.factorial(n)
        return t
