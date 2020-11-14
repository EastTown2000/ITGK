from math import sin
import matplotlib.pyplot as plt

x_verdier = []
for i in range(301):
    x_verdier.append(i/10)

y_verdier = []
for x in x_verdier:
    y_verdier.append(sin(x))
    
plt.plot(x_verdier, y_verdier, c='r')
plt.show()