#coding:utf-8
"""
    普通AM波调制
"""
import numpy as np
import matplotlib.pyplot as plt

plt.ion()
for  i in range(100):
    #定义参数
    k = i/100.          #调制深度
    Ucm = 1             #直流分量
    Um = 1              #载波分量
    W  = 2*np.pi*2      #基波频率
    Wc = 2*np.pi*20    #载波频率

    t = np.linspace(-3,3,5000)
    y = (Ucm+k*Um*np.cos(W*t))*np.cos(Wc*t)

    plt.cla()
    plt.plot(t,y,linestyle='--',color='r')
    plt.xlabel(r'Time/s')
    plt.ylabel(r'Amplitude/V')
    plt.show()
    plt.pause(0.1)

plt.ioff()
plt.show()