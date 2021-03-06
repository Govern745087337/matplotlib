#coding:utf-8
"""
plot one picture with two Y axis
"""
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)

y1 = 0.05 * x**2
y2 = -1 * y1

fig, ax1 = plt.subplots()
#生成镜面坐标轴
ax2 = ax1.twinx()

ax1.plot(x, y1, 'g-')   # green, solid line
ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')

ax2.plot(x, y2, 'b-') # blue
ax2.set_ylabel('Y2 data', color='b')

plt.show()