import numpy as np
import time

#����һ��numpy����
a = np.array([1,2,3,4])
print a

#�������͵��������
b = np.random.rand(1000000)
c = np.random.rand(1000000)

#����ʹ��numpy��������˵�ʱ��
start = time.time()
d = np.dot(b,c)
end = time.time()
print("����һ����ά�ȵľ���ʹ��numpy�������Ҫ��ʱ�䣺" + str(1000*(end-start)) + "����")

#����ʹ��forѭ����˵�ʱ��

d = 0
start = time.time()
for i in range(1000000):
    d = d + b[i] * c[i]
end = time.time()
print("����һ����ά�ȵľ���ʹ��forѭ���������Ҫ��ʱ�䣺" + str(1000*(end-start)) + "����")  
