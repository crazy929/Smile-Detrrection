import cv2
image=cv2.imread("girl.jpg")

smile_cascade=cv2.CascadeClassifier("smile.xml")

smiles=smile_cascade.detectMultiScale(image,scaleFactor=1.8,minNeighbors=20)

for (x,y,w,h) in smiles:
    cv2.rectangle(image,(x,y),((x+w),(y+h)),(0,500,0,),5)

cv2.imshow("girl_image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()