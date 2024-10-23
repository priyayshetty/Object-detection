import cv2 as cv
import numpy as np

img= cv.imread("women.jpg")    #full path of the image
cv.imshow("originalimg", img)
cv.waitKey(0)
out="facerect.jpg"     #add output store path

eye_har_cascade= cv.CascadeClassifier("haar_eye.xml")    #full path of the haar cascade
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face=eye_har_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))

for (ex,ey, ew,eh) in face:
    rect=cv.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,0,255),3)
cv.imshow("img", rect)
cv.waitKey()
cv.imwrite(out, img)
cv.destroyAllWindows()
