import numpy as np
import time

#创建一个numpy矩阵
a = np.array([1,2,3,4])
print a

#创建大型的随机矩阵
b = np.random.rand(1000000)
c = np.random.rand(1000000)

#计算使用numpy把他们相乘的时间
start = time.time()
d = np.dot(b,c)
end = time.time()
print("两个一百万维度的矩阵，使用numpy相乘所需要的时间：" + str(1000*(end-start)) + "毫秒")

#计算使用for循环相乘的时间

d = 0
start = time.time()
for i in range(1000000):
    d = d + b[i] * c[i]
end = time.time()
print("两个一百万维度的矩阵，使用for循环相乘所需要的时间：" + str(1000*(end-start)) + "毫秒")  
