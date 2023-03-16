from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def myfunc(x, y):
    return 21.5 + x * np.sin(4 * np.pi * x) + y * np.sin(20 * np.pi * y)


fig = plt.figure()

# 需要用到Axes3D库进行绘图，但是出现了问题，代码没有报错，但是图像显示不出来
# 将自身添加到图像中，自3.4版本之后被弃用。
# 使用如下代码替换 ax = Axes3D(fig) 即可：
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

X, Y = np.mgrid[-3:12.1:100j, 4.1:5.8:100j]
Z = myfunc(X, Y)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
