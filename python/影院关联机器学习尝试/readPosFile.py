posData = []
posFile = open("D:\\������������\\positive.txt")             
posLine = posFile.readline()

while posLine:    
    #�����зֲ�ת���ɸ���
    posLine = posLine.strip('\n')  
    posLineArray = posLine.split(" ")
    for i in range(len(posLineArray)):
        posLineArray[i] = float(posLineArray[i])
        
    #���뵽���������ݼ���
    posData.append(posLineArray)

    #��ȡ��һ��
    posLine = posFile.readline()

    print len(posData)

