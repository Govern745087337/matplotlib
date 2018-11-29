import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,linewidth=1.0,linestyle='--')
plt.xlim((-1,2))
plt.ylim((-2,3))

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],['$really bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])

ax = plt.gca() #获取当前坐标轴信息
ax.spines['right'].set_color('none') #改变坐标轴颜色
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')  #设置x 坐标轴文字显示位置
ax.spines['bottom'].set_position(('data',0))  #设置坐标轴位置

ax.yaxis.set_ticks_position('none')    #设置y 坐标轴文字显示位置
ax.spines['left'].set_position(('data',0))  #设置坐标轴位置

plt.show()