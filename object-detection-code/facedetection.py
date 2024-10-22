import cv2 as cv

img= cv.imread("D:/program-work/opencv/facedetection/faces.jpg")
# img_resize= cv.resize(img, (600,350))
print(img.shape)
cv.imshow("Face", img)
cv.waitKey()

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)
# cv.waitKey()

haar_cascade= cv.CascadeClassifier("C:/Users/joejo/Downloads/python-practice/Projects/haar_face.xml")
face_rect=haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=3, minSize=(10,10))

print(f"Number of faces found={len(face_rect)}")

for (x,y,w,h) in face_rect:
    rect=cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
    cv.imshow("Rect", rect)
    cv.waitKey()