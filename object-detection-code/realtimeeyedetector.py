import cv2 as cv

fourcc= cv.VideoWriter_fourcc(*"XVID")
out= cv.VideoWriter("output.avi", fourcc, 20.0, (640,480))

 
cap= cv.VideoCapture(0,cv.CAP_DSHOW)

haar_cascade= cv.CascadeClassifier("C:/Users/joejo/Downloads/python-practice/Projects/haar_eye.xml")

def detect_Video_bbox(video):
    gray= cv.cvtColor(video, cv.COLOR_BGR2GRAY)
    face_rect= haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))
    
    for (ex,ey,ew,eh) in face_rect:
        rect=cv.rectangle(video, (ex,ey), (ex+ew, ey+eh), (255,0,0), 3)
        return face_rect
       
if cap.isOpened:
    print("cam opened sucessfully")
while True:
    ret, frame= cap.read()
    if not ret:
        print("error to reading the frame")
        break
    face= detect_Video_bbox(frame)
    frame= cv.resize(frame, (640,480))
    frame=cv.flip(frame,1)
    # out.write(frame)

    cv.imshow("Vide detect Rect", frame)

    if cv.waitKey(30)== ord("q"):
        break
cap.release()
# out.release()
cv.destroyAllWindows()




    

