import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
T = 0.005
K1 = 3000
K2 = 6000

# 参考信号
y_d = np.zeros(K2)
for k in range(K1):
    y_d[k] = np.sin(PI*k*T/2)
for k in range(K1,K2):
    y_d[k] = 0.5*np.cos(PI*k*T) + 0.5*np.sin(PI*k*T/2)


# 控制信号为参考信号的系统动态
xr = np.zeros((K2, 2))
xr[0] = [0, 0.3]
for k in range(K2-1):
    xr[k+1, 0] = 0.2 * np.square(xr[k, 0]) * xr[k, 1] / (1 + np.square(xr[k, 0])) + 0.5 * xr[k, 1]
    xr[k+1, 1] = xr[k, 0] / (1 + np.square(xr[k, 0]) + np.square(xr[k, 1])) + y_d[k] + 0.05*np.cos(0.01*k)*np.cos(xr[k, 0])

y = xr[:, 1]
e = y - y_d

# 画图
fig, axs = plt.subplots(3, 1)
fig.set_size_inches(20, 15)

axs[0].plot(y_d)
axs[0].set_title("y_d")

axs[1].plot(xr)
axs[1].set_title("States")
axs[1].legend(["x1", "x2 = y"])

axs[2].plot(e)
axs[2].set_title("y - y_d")
