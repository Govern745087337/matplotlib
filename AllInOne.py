#coding:utf-8
"""
plot many frame in one picture
"""
import matplotlib.pyplot as plt

plt.figure()
"""画均匀图"""
# plt.subplot(2,2,1)
# plt.plot([0,2],[0,2])
#
# plt.subplot(2,2,2)
# plt.plot([0,2],[0,1])
#
# # plt.subplot(2,2,3)
# # plt.plot([0,2],[0,3])
#
# plt.subplot(2,2,4)
# plt.plot([0,2],[0,4])
#
# plt.show()

"""画不均匀图"""
plt.subplot(2,1,1)
plt.plot([0, 2], [0, 2])

plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(2,3,5)
plt.plot([0,1],[0,4])

plt.subplot(2,3,6)
plt.plot([0,1],[0,2])

plt.show()