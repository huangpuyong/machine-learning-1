import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])
print("��ʼ����A��")
print A

#�������
cal = A.sum(axis = 0)
print("������͵Ľ��:")
print cal

#ÿ��ֵ���Ը��е��ܺͣ�����ٷֱ�
percentage = 100*A/cal
print("ÿ����ռ���Ե��еİٷֱ�Ϊ��")
print percentage

x = np.array([[1,2,3],[4,5,6]])
y = np.array([1,2,3])
print x.shape[0]
