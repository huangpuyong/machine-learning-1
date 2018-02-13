negData = []
negFile = open("D:\\正负样本数据\\negative.txt")             
negLine = negFile.readline()
count = 0

while negLine:
    count = count + 1
    if count > 100000:
        break
    
    #按行切分并转换成浮点
    negLine = negLine.strip('\n')  
    negLineArray = negLine.split(" ")
    for i in range(len(negLineArray)):
        negLineArray[i] = float(negLineArray[i])
        
    #加入到负样本数据集中
    negData.append(negLineArray)

    #读取下一行
    negLine = negFile.readline()
