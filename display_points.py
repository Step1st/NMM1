import numpy as np
import matplotlib.pyplot as plt

points = np.genfromtxt("test.csv", delimiter=',', skip_header=1 )
x, y = points.T

plt.scatter(x, y, s=0.1)
plt.show()