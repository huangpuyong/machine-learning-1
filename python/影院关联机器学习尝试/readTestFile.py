testData = []
testFile = open("D:\\������������\\testdata.txt")             
testLine = testFile.readline()

while testLine:    
    #�����зֲ�ת���ɸ���
    testLine = testLine.strip('\n')  
    testLineArray = testLine.split(" ")
    for i in range(len(testLineArray)):
        testLineArray[i] = float(testLineArray[i])
        
    #���뵽���������ݼ���
    testData.append(testLineArray)

    #��ȡ��һ��
    testLine = testFile.readline()

    print len(testData)

