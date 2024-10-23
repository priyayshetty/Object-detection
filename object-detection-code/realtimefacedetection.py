import cv2 as cv

fourcc= cv.VideoWriter_fourcc(*"XVID")
out=cv.VideoWriter("Output.avi", fourcc,20.0, (640,480) )

cap=cv.VideoCapture(0)

har_cascade=cv.CascadeClassifier("haar_face.xml")    #full path of the haar cascade

def detect_bounding_box(vid):
    gray= cv.cvtColor(vid, cv.COLOR_BGR2GRAY)
    face_rect= har_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))
    for (x,y,w,h) in face_rect:
        rect=cv.rectangle(vid, (x,y), (x+w, x+h), (0,0,255), 3)
    return face_rect


if cap.isOpened():
    print("cam opened sucessfully")

while cap.isOpened():
    ret, frame= cap.read()
    if not ret:
        print("Error frame reading")
        break
    face= detect_bounding_box(frame)
    frame=cv.resize(frame, (640,480))
    frame=cv.flip(frame, 1)
    out.write(frame)

    cv.imshow("Video face detecting", frame)
    
    key=cv.waitKey(40)
    if key==ord("q"):
        break
cap.release()
out.release()
cv.destroyAllWindows()
