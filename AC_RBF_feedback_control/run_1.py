import numpy as np
import matplotlib.pyplot as plt

from actor import Actor
from critic import Critic

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


actor = Actor(n=1)
critic = Critic()

# 输入参考信号的系统动态
x = np.zeros((K2, 2))
y = np.zeros(K2)
e = np.zeros(K2)
x[0] = [0, 0.3]

for k in range(K2-1):
    x_k = x[k] 
    y_k = actor.get_output(x_k)
    e_k = y_k - y_d[k]
    
    # 更新critic
    critic.update(e_k, x_k)
    Q_k = critic.get_output(x_k)
    
    # 更新actor
    actor.update(Q_k, e_k, x_k)
    
    # 系统动态
    x[k+1, 0] = 0.2 * np.square(x[k, 0]) * x[k, 1] / (1 + np.square(x[k, 0])) + 0.5 * x[k, 1]
    x[k+1, 1] = x[k, 0] / (1 + np.square(x[k, 0]) + np.square(x[k, 1])) + y_k + 0.05*np.cos(0.01*k)*np.cos(x[k, 0])
    
    y[k] = y_k
    e[k] = e_k
    
y = x[:, 1]

# 画图
fig, axs = plt.subplots(3, 1)
fig.set_size_inches(20, 15)

axs[0].plot(y_d)
axs[0].set_title("y_d")

axs[1].plot(x)
axs[1].set_title("States")
axs[1].legend(["x1", "x2 = y"])

axs[2].plot(e)
axs[2].set_title("y - y_d")


