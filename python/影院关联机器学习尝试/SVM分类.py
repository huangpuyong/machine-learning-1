from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB  
import numpy as np
import math

#��ȡ������
print '��ʼ��ȡ������'
posData = []
posTag = []
posFile = open("D:\������������\positive.txt")             
posLine = posFile.readline()

while posLine:    
    #�����зֲ�ת���ɸ���
    posLine = posLine.strip('\n')  
    posLineArray = posLine.split(" ")
    for i in range(len(posLineArray)):
        posLineArray[i] = np.float64(posLineArray[i])
        
    #���뵽���������ݼ���
    if len(posLineArray) != 4:
        posLine = posFile.readline()
        continue
    posData.append(posLineArray)
    posTag.append(1)

    #��ȡ��һ��
    posLine = posFile.readline()
print '������ȡ��������Ŀ��' + str(len(posData))


#��ȡ����������ʱ�ȶ�100W��
print '��ʼ��ȡ������'
negData = []
negTag = []
negFile = open("D:\\������������\\negative.txt")             
negLine = negFile.readline()
count = 0

while negLine:
    count = count + 1
    flag = True
    if count > 1000000:
        break
    
    #�����зֲ�ת���ɸ���
    negLine = negLine.strip('\n')  
    negLineArray = negLine.split(" ")
    for i in range(len(negLineArray)):
        try:
            negLineArray[i] = np.float64(negLineArray[i])
        except:
            flag = False
            break
        
    if flag == False:
        negLine = negFile.readline()
        continue
        
    #���뵽���������ݼ���
    if len(negLineArray) != 4:
        negLine = negFile.readline()
        continue
        
    negData.append(negLineArray)
    negTag.append(0)

    #��ȡ��һ��
    negLine = negFile.readline()
print '������ȡ��������Ŀ��' + str(len(negData))

#ƴ����������
posData.extend(negData)
posTag.extend(negTag)

sampleData = np.array(posData)
sampleTag = np.array(posTag)

print '��ʼѵ��'
clf = MultinomialNB().fit(sampleData, sampleTag)
print '����ѵ��'

print '��ʼ��ȡ���Լ�'
testData = []
testFile = open("D:\\������������\\testdata.txt")             
testLine = testFile.readline()

while testLine:    
    #�����зֲ�ת���ɸ���
    testLine = testLine.strip('\n')  
    testLineArray = testLine.split(" ")
    for i in range(len(testLineArray)):
        testLineArray[i] = float(testLineArray[i])
        
    #���뵽�����������ݼ���
    if len(testLineArray) != 4:
        testLine = testFile.readline()
        continue
    testData.append(testLineArray)

    #��ȡ��һ��
    testLine = testFile.readline()
print '������ȡ���Լ���Ŀ��' + str(len(testData))

print '��ʼԤ���������'
zeroCount = 0
nonZeroCount = 0
for i in range(len(testData)):
    result = clf.predict(np.array(testData[i]).reshape(1, -1))
    if result == 0:
        zeroCount = zeroCount + 1
    else:
        nonZeroCount = nonZeroCount + 1
print '����Ԥ���������'
print 'Ԥ�����й���' + str(zeroCount) + '��0������' + str(nonZeroCount) + '��1��'

z = np.array([0, 0, 0, 1]).reshape(1, -1)
