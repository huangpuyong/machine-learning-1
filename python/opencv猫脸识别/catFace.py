import cv2
# ����è�������
catPath = "C:\Users\lenovo\Desktop\python\opencvè��ʶ��\haarcascade_frontalcatface.xml"
faceCascade = cv2.CascadeClassifier(catPath)
# ��ȡͼƬ���ҶȻ�
img = cv2.imread("cat.jpeg")  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# è�����
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor= 1.02,
    minNeighbors=3,
    minSize=(150, 150),
    flags=cv2.CASCADE_SCALE_IMAGE
)
# ���è������������˵��
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(img,'Cat',(x,y-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)
# ��ʾͼƬ������
cv2.imshow('Cat?', img)
cv2.imwrite("cat.jpg",img)
c = cv2.waitKey(0)
