import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y = 2*x+1

plt.figure()  #新建一个窗口
plt.plot(x,y)
plt.show()
