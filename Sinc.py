import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,7,100)

for i in range(7):
    yi = np.sinc(x-i)
    plt.plot(x,yi,c='blue')

plt.xlim([0,7])
plt.ylim([-0.5,1])
plt.xlabel('Subcarrier')
plt.ylabel('Amplitude')
plt.grid()
plt.show()