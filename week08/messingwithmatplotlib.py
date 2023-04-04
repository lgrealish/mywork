# messing with matplotlib
# Author: Linda Grealish

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label="xsquared", color="red")
plt.legend()
plt.show()

