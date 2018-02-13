posData = []
posFile = open("D:\\正负样本数据\\positive.txt")             
posLine = posFile.readline()

while posLine:    
    #按行切分并转换成浮点
    posLine = posLine.strip('\n')  
    posLineArray = posLine.split(" ")
    for i in range(len(posLineArray)):
        posLineArray[i] = float(posLineArray[i])
        
    #加入到正样本数据集中
    posData.append(posLineArray)

    #读取下一行
    posLine = posFile.readline()

    print len(posData)

