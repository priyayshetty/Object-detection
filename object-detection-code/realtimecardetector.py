import cv2 as cv

fourcc=cv.VideoWriter_fourcc(*"XVID")
out= cv.VideoWriter("output.avi", fourcc, 20.0, (640,480))

cap=cv.VideoCapture("D:/program-work/opencv/cardetection/vehical.mp4")

har_car_cascade=cv.CascadeClassifier("C:/Users/joejo/Downloads/python-practice/Projects/haar_car.xml")

def detect_car(video):
    gray= cv.cvtColor(video, cv.COLOR_BGR2GRAY)
    car=har_car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))
    for (x,y,w,h) in car:
        cv.rectangle(video, (x,y),(x+w, y+h), (255,0,0), 3)
    return car

if cap.isOpened():
    print("cam opened sucessfully")
while cap.isOpened():
    ret, frame= cap.read()
    if not ret:
        print("error to reading the frames")
        break
    car=detect_car(frame)
    frame=cv.resize(frame, (640,480))
    frame=cv.flip(frame, 1)
    out.write(frame)

    cv.imshow(" Detecting Car", frame)

    key=cv.waitKey(60)
    if key== ord("q"):
        break
cap.release()
out.release()
cv.destroyAllWindows()

    
