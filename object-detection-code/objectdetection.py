import cv2 
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cvlib as cv
from cvlib.object_detection import draw_bbox


img= cv.imread("D:/program-work/opencv/facedetection/object.jpg")
# img_resize= cv.resize(img, (600,350))

img=np.array(img)


img = Image.open('car.jpg')
img = np.array(img)


bbox, label, conf = cv.detect_common_objects(img, model='yolov3')
output_image = draw_bbox(img, bbox, label, conf)

plt.imshow(output_image)
