"""
Dette programmet plotter antall sauer og ulver ut ifra en matematisk 
sammenheng mellom disse.

Beregner vha. array og for-løkke.
"""

import matplotlib.pyplot as plt
import numpy as np

b = float(input('Hvor mange sauer spiser hver ulv i løpet av et år? '))

n = 100      #antall år
t = np.linspace(0,n,n) #array over alle år
x = np.zeros(n) 
y = np.zeros(n)
x[0] = 2000 #antall sauer ved år 0
y[0] = 5    #antall ulver ved år 0
for k in range(n-1):
    x[k+1] = 1.1*x[k] - b*y[k]   #antall sauer ved neste år
    y[k+1] = 0.1*x[k] + 0.8*y[k] #antall ulver ved neste år
    
plt.plot(t,x)
plt.plot(t,y)
plt.xlabel('antall år')
plt.ylabel('antall dyr')
plt.legend(['sauer','ulver'])
plt.show()

plt.plot(x,y)
plt.xlabel('sauer')
plt.ylabel('ulver')
plt.show()
