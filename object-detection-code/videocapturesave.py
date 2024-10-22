#capturing video from camera

# import numpy as np
# import cv2 as cv

# cap=cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Error to open the camera")
#     exit()
# while True:
#     ret, frame= cap.read()
#     if not ret:
#         print("Error to recieve the frame")
#         break
#     gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow("Frame", gray)
#     if cv.waitKey(1)==ord("q"):
#         break

# cap.release()
# cv.destroyAllWindows()




# #playing video from file

# import cv2 as cv
# import numpy as np

# cap=cv.VideoCapture("C:/Users/joejo/Downloads/1234.mp4")

# if not cap.isOpened:
#     print("Error to open the camera")
#     exit()
# while True:
#     ret, frame= cap.read()
#     if not ret:
#         print("Error recieving the frame")
#         break
#     resize_frame= cv.resize(frame, (640, 480))
#     gray= cv.cvtColor(resize_frame, cv.COLOR_RGB2BGR)
#     cv.imshow("Frame", gray)
#     if cv.waitKey(25)==ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()


import cv2 as cv

fourcc= cv.VideoWriter_fourcc(*'XVID')
out= cv.VideoWriter("output.mp4", fourcc, 20.0, (640,480))

cap= cv.VideoCapture(0)

if not cap.isOpened():
    print("error to opening the camera")

while cap.isOpened():
    ret, frame= cap.read()
    if not ret:
        print("error to reciveing the frame")
        break
    
    frame=cv.flip(frame, 1)
    out.write(frame)
    
    frame_resize= cv.resize(frame, (640, 480))
    # gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow("frame", frame_resize)

    if cv.waitKey(25)==ord("q"):
        break

cap.release()
out.release()
cv.destroyAllWindows()

