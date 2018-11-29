#coding:utf-8
"""
    普通AM波调制
"""
import numpy as np
import matplotlib.pyplot as plt

#定义参数
k = 0.99             #调幅深度
Ucm = 1             #直流分量
Um = 1              #载波分量
W  = 2*np.pi*2      #基波频率
Wc = 2*np.pi*20    #载波频率

t = np.linspace(-3,3,5000)
y = (Ucm+k*Um*np.cos(W*t))*np.cos(Wc*t)

plt.plot(t,y,linestyle='--',color='r')
plt.xlabel(r'Time/s')
plt.ylabel(r'Amplitude/V')
plt.show()