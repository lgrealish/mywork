# salaries.py
# Author: Linda Grealish

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100


'''
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
#salariesPlus = salaries + 5000
salariesMult = salaries * 1.1075
print (salaries)
print(salariesMult)
'''
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.show()