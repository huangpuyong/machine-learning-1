from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB  
import numpy as np
import math

#读取正样本
print '开始读取正样本'
posData = []
posTag = []
posFile = open("D:\正负样本数据\positive.txt")             
posLine = posFile.readline()

while posLine:    
    #按行切分并转换成浮点
    posLine = posLine.strip('\n')  
    posLineArray = posLine.split(" ")
    for i in range(len(posLineArray)):
        posLineArray[i] = np.float64(posLineArray[i])
        
    #加入到正样本数据集中
    if len(posLineArray) != 4:
        posLine = posFile.readline()
        continue
    posData.append(posLineArray)
    posTag.append(1)

    #读取下一行
    posLine = posFile.readline()
print '结束读取正样本数目：' + str(len(posData))


#读取负样本（暂时先读100W）
print '开始读取负样本'
negData = []
negTag = []
negFile = open("D:\\正负样本数据\\negative.txt")             
negLine = negFile.readline()
count = 0

while negLine:
    count = count + 1
    flag = True
    if count > 1000000:
        break
    
    #按行切分并转换成浮点
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
        
    #加入到负样本数据集中
    if len(negLineArray) != 4:
        negLine = negFile.readline()
        continue
        
    negData.append(negLineArray)
    negTag.append(0)

    #读取下一行
    negLine = negFile.readline()
print '结束读取负样本数目：' + str(len(negData))

#拼接正负样本
posData.extend(negData)
posTag.extend(negTag)

sampleData = np.array(posData)
sampleTag = np.array(posTag)

print '开始训练'
clf = MultinomialNB().fit(sampleData, sampleTag)
print '结束训练'

print '开始读取测试集'
testData = []
testFile = open("D:\\正负样本数据\\testdata.txt")             
testLine = testFile.readline()

while testLine:    
    #按行切分并转换成浮点
    testLine = testLine.strip('\n')  
    testLineArray = testLine.split(" ")
    for i in range(len(testLineArray)):
        testLineArray[i] = float(testLineArray[i])
        
    #加入到测试样本数据集中
    if len(testLineArray) != 4:
        testLine = testFile.readline()
        continue
    testData.append(testLineArray)

    #读取下一行
    testLine = testFile.readline()
print '结束读取测试集数目：' + str(len(testData))

print '开始预测测试样本'
zeroCount = 0
nonZeroCount = 0
for i in range(len(testData)):
    result = clf.predict(np.array(testData[i]).reshape(1, -1))
    if result == 0:
        zeroCount = zeroCount + 1
    else:
        nonZeroCount = nonZeroCount + 1
print '结束预测测试样本'
print '预测结果中共有' + str(zeroCount) + '个0，共有' + str(nonZeroCount) + '个1。'

z = np.array([0, 0, 0, 1]).reshape(1, -1)
