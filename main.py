import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import fmin_bfgs


# #定义坐标轴
# fig = plt.figure()
# ax1 = plt.axes(projection='3d')
# #ax = fig.add_subplot(111,projection='3d')  #这种方法也可以画多个子图

def myfunc(x1, x2):
    return 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)


fig = plt.figure()  # 定义新的三维坐标轴
ax3 = plt.axes(projection='3d')

# 定义三维数据
x1 = np.arange(-3.0, 12.1, 0.5)
x2 = np.arange(4.1, 5.8, 0.5)
X, Y = np.meshgrid(x1, x2)
Z = 21.5 + 2*X

#
# result = fmin_bfgs(myfunc, x0=np.array([-3.0,4.1]))
# print("The maximum value occurs at:", result)
# 作图
ax3.plot_surface(X, Y, Z, cmap='rainbow')
# ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
plt.show()
