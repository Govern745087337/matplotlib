#coding:utf-8
"""
plot a image
"""
import matplotlib.pyplot as plt
import numpy as np

a = np.random.uniform(0,1,9).reshape((3,3))

# origin='lower'代表的就是选择的原点的位置
#白色代表值最大的地方，颜色越深值越小。
#内插法中的 Nearest-neighbor
plt.imshow(a,interpolation='nearest',cmap='bone',origin='lower')

#添加一个shrink参数，使colorbar的长度变短为原来的92%：
plt.colorbar(shrink = .92)
plt.xticks(())
plt.yticks(())
plt.show()