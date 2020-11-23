import numpy as np
import cv2 
import matplotlib.pyplot as plt


test_image = cv2.imread('1.jpg')
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

def convertToRGB(image):
    return cv2.cvtC6lor(image, cv2.COLOR_BGR2RGB)

haar_cascade_face = cv2.CascadeClassifier('/home/aryan/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

print('Faces found: ', len(faces_rects))

def detect_faces(cascade, test_image, scaleFactor = 1.1):
    image_copy = test_image.copy()
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors = 5)
