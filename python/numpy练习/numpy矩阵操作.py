import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])
print("初始矩阵A：")
print A

#按列求和
cal = A.sum(axis = 0)
print("按列求和的结果:")
print cal

#每个值除以该列的总和，计算百分比
percentage = 100*A/cal
print("每个数占各自的列的百分比为：")
print percentage

x = np.array([[1,2,3],[4,5,6]])
y = np.array([1,2,3])
print x.shape[0]
