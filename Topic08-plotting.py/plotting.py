
# y=

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot (ypoints, xpoints)
plt.show()