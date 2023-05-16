import numpy as np

# 二维径向基函数
def rbf2d(x, c):
    width = 1;
    return np.exp(-1 * (np.linalg.norm(x - c)**2) / (2 * width**2))

class Critic():
    def __init__(self):
        self.W = np.zeros((5**2, 2)) # 需要储存k和k-1两个时刻的信息
        self.S = np.zeros((5**2, 2)) # 需要储存k和k-1两个时刻的信息
        self.Center = np.zeros((5**2, 2)) # 神经元中心点的坐标(2d)
        k = 0
        for i in [-1, -0.5, 0, 0.5, 1]:
            for j in [-1, -0.5, 0, 0.5, 1]:
                self.Center[k] = [i, j]
                k += 1
        self.Alpha_0 = 2 # 跟随误差增益
        self.Alpha_c = 0.1 # critic学习率
        self.Alpha = 0.515 # 衰减系数
        self.N = 4 # return函数考虑的未来步长
        
    def get_output(self, x):
        W_T = np.transpose(self.W[:, 0])
        S = np.zeros((5**2, 1))
        for i, value in enumerate(S):
            S[i] = rbf2d(x, self.Center[i])
        return np.dot(W_T, S)
    
    def update(self, e_k, x):
        # 计算S(k)
        S_k = np.zeros(5**2)
        for i, value in enumerate(S_k):
            S_k[i] = rbf2d(x, self.Center[i])
            
        # 更新S队列
        self.S[:, 1] = self.S[:, 0]
        self.S[:, 0] = S_k
        
        # 计算p_k
        p_k = self.Alpha_0 * abs(e_k)
        
        # 计算W(k+1)
        W_new = self.W[:, 0] - self.Alpha_c * self.S[:, 0] * (
            np.transpose(self.W[:, 0]) * self.S[:, 0] 
            + self.Alpha**(self.N + 1) * p_k
            - self.Alpha * np.transpose(self.W[:, 1]) * self.S[:, 1]
        )
        
        # 更新W队列
        self.W[:, 1] = self.W[:, 0]
        self.W[:, 0] = W_new
        
        
        
        
        
        
    
    

