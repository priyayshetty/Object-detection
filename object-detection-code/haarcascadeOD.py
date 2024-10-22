import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread("D:/program-work/opencv/facedetection/women.jpg")
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
resize_img= cv.resize(img, (640,480))
plt.imshow(resize_img)
plt.show()
cv.waitKey()
face_haar_cascade=cv.CascadeClassifier("C:/Users/joejo/Downloads/python-practice/Projects/haar_face.xml")
eye_haar_cascade=cv.CascadeClassifier("C:/Users/joejo/Downloads/python-practice/Projects/haar_eye.xml")

def detecte_face(img):
    face_img=img.copy()
    
    face_detect= face_haar_cascade.detectMultiScale(face_img, scaleFactor=1.1,minNeighbors=5, minSize=(40,40))
    print(f"number of face detect={len(face_detect)}")

    for (x,y,w,h) in face_detect:
        cv.rectangle(face_img, (x,y), (x+w, y+h),(255,0,0), 3)
    return face_img
    
def detect_eye(img):
    eye_img= img.copy()
    
    eye_detect=eye_haar_cascade.detectMultiScale(eye_img, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))
    print(f"num of eyes found={len(eye_detect)}")
    
    for (ex,ey,eh,ew) in eye_detect:
        cv.rectangle(eye_img, (ex,ey), (ex+ew, ey+eh),(255,0,0),3)
    return eye_img

imgcopy1=img.copy()
imgcopy2=img.copy()
imgcopy3=img.copy()

face=detecte_face(imgcopy1)
eye=detect_eye(imgcopy2)
face_eye= detecte_face(imgcopy3)
face_eye=detect_eye(face_eye)

plt.figure(figsize=(9,3))

plt.subplot(131)
plt.title("Face",c="green")
plt.imshow(face)

plt.subplot(132)
plt.title("Eye", c="green")
plt.imshow(eye)

plt.subplot(133)
plt.title("Face and Eye",c="green")
plt.imshow(face_eye)


plt.show()
cv.waitKey()
cv.destroyAllWindows()
