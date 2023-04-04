# messingwithhist.py
# Author: Linda Grealish

import numpy as np
import matplotlib.pyplot as plt
'''
normData = np.random.normal(size=100)

plt.hist(normData)
plt.show()
'''

fruit = np.array(['Apples','Orange','Banana'])
numbers = np.array([23,77,500])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()