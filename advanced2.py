import numpy as np
import matplotlib.pyplot as plt
arr = np.random.normal(size=100)
print(arr)
plt.hist(arr, bins=100, normed=1)
plt.show()

from pylab import *
hist(arr)
show()