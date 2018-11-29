import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y1)
plt.plot(x,y2,color='red',linewidth=2.0,linestyle='--')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am X')
plt.ylabel('I am Y')
#plt.show()

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)    #设置X轴刻度 范围是（-1，2）个数为5
#设置Y轴刻度 刻度为[-2, -1.8, -1, 1.22, 3]；对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’]
plt.yticks([-2,-1,8.-1,1.22,3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()
