negData = []
negFile = open("D:\\������������\\negative.txt")             
negLine = negFile.readline()
count = 0

while negLine:
    count = count + 1
    if count > 100000:
        break
    
    #�����зֲ�ת���ɸ���
    negLine = negLine.strip('\n')  
    negLineArray = negLine.split(" ")
    for i in range(len(negLineArray)):
        negLineArray[i] = float(negLineArray[i])
        
    #���뵽���������ݼ���
    negData.append(negLineArray)

    #��ȡ��һ��
    negLine = negFile.readline()
