import cv2 as cv
import numpy as np

img= cv.imread("D:/program-work/opencv/facedetection/women.jpg")
cv.imshow("originalimg", img)
cv.waitKey(0)
out="D:/program-work/opencv/facedetection/facerect.jpg"

eye_har_cascade= cv.CascadeClassifier("C:/Users/joejo/Downloads/python-practice/Projects/haar_eye.xml")
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face=eye_har_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))

for (ex,ey, ew,eh) in face:
    rect=cv.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,0,255),3)
cv.imshow("img", rect)
cv.waitKey()
cv.imwrite(out, img)
cv.destroyAllWindows()