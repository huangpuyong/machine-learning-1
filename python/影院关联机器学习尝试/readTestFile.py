testData = []
testFile = open("D:\\正负样本数据\\testdata.txt")             
testLine = testFile.readline()

while testLine:    
    #按行切分并转换成浮点
    testLine = testLine.strip('\n')  
    testLineArray = testLine.split(" ")
    for i in range(len(testLineArray)):
        testLineArray[i] = float(testLineArray[i])
        
    #加入到正样本数据集中
    testData.append(testLineArray)

    #读取下一行
    testLine = testFile.readline()

    print len(testData)

