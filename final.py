import numpy as np
import cv2 
import matplotlib.pyplot as plt
from PIL import Image
import psutil 
import time

start = "\033[1m"
end = "\033[0;0m"


print(start + "\n                 *****Welcome to Face Recognization*****\n\n"  + end)
test_image1 = cv2.imread('1.jpg')
test_image2 = cv2.imread('2.jpg')
test_image3 = cv2.imread('3.jpg')
test_image4 = cv2.imread('4.jpg')
test_image5 = cv2.imread('5.jpg')
test_image6 = cv2.imread('6.jpg')
test_image7 = cv2.imread('7.jpg')
test_image8 = cv2.imread('8.jpg')
test_image9 = cv2.imread('9.jpg')
test_image10 = cv2.imread('10.jpg')
test_image11 = cv2.imread('11.jpg')
test_image12 = cv2.imread('12.jpg')
test_image13 = cv2.imread('13.jpg')
test_image14 = cv2.imread('14.jpg')
test_image15 = cv2.imread('15.jpg')
test_image = []

im1 = Image.open("1.jpg") 
im2 = Image.open("2.jpg") 
im3 = Image.open("3.jpg")
im4 = Image.open("4.jpg")
im5 = Image.open("5.jpg")
im6 = Image.open("6.jpg")
im7 = Image.open("7.jpg")
im8 = Image.open("8.jpg")
im9 = Image.open("9.jpg")
im10 = Image.open("10.jpg")
im11 = Image.open("11.jpg")
im12 = Image.open("12.jpg")
im13 = Image.open("13.jpg")
im14 = Image.open("14.jpg")
im15 = Image.open("15.jpg")
im = []

n = int(input("Enter number of images : "))
print("Enter name of images:")
for i in range(0, n): 
    ele = input()
    if ele == "1.jpg":
        test_image.append(test_image1)
        im.append(im1)
    elif ele == "2.jpg":
        test_image.append(test_image2)
        im.append(im2)
    elif ele == "3.jpg":
        test_image.append(test_image3)
        im.append(im3)
    elif ele == "4.jpg":
        test_image.append(test_image4)
        im.append(im4)
    elif ele == "5.jpg":
        test_image.append(test_image5)
        im.append(im5)
    elif ele == "6.jpg":
        test_image.append(test_image6)
        im.append(im6)
    elif ele == "7.jpg":
        test_image.append(test_image7)
        im.append(im7)
    elif ele == "8.jpg":
        test_image.append(test_image8)
        im.append(im8)
    elif ele == "9.jpg":
        test_image.append(test_image9)
        im.append(im9)
    elif ele == "10.jpg":
        test_image.append(test_image10)
        im.append(im10)
    elif ele == "11.jpg":
        test_image.append(test_image11)
        im.append(im11)
    elif ele == "12.jpg":
        test_image.append(test_image12)
        im.append(im12)
    elif ele == "13.jpg":
        test_image.append(test_image13)
        im.append(im13)
    elif ele == "14.jpg":
        test_image.append(test_image14)
        im.append(im14)
    elif ele == "15.jpg":
        test_image.append(test_image15)
        im.append(im15)
        
def green(text):
	print('\033[32m', text, '\033[0m', sep='')

def blue(text):
	print('\033[34m', text, '\033[0m', sep='')
    
def red(text):
	   print('\033[31m', text, '\033[0m', sep='')
            
    
    
    
def facereco(i):
    test_image_gray = cv2.cvtColor(test_image[i], cv2.COLOR_BGR2GRAY)

    def convertToRGB(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    haar_cascade_face = cv2.CascadeClassifier('/home/aryan/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
    faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);
    m = len(faces_rects)
    print(' is - ',end="", flush=True)
    green(m)

    def detect_faces(cascade, test_image, scaleFactor = 1.1):
        image_copy = test_image[i].copy()
        gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors = 5)
    return len(faces_rects)



def facereco2(i):
    test_image_gray = cv2.cvtColor(test_image[i], cv2.COLOR_BGR2GRAY)

    def convertToRGB(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    haar_cascade_face = cv2.CascadeClassifier('/home/aryan/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
    faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

    def detect_faces(cascade, test_image, scaleFactor = 1.1):
        image_copy = test_image[i].copy()
        gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors = 5)
    return len(faces_rects)


def facereco3(tst_image):
    test_image_gray = cv2.cvtColor(tst_image, cv2.COLOR_BGR2GRAY)

    def convertToRGB(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    haar_cascade_face = cv2.CascadeClassifier('/home/aryan/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
    faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

    def detect_faces(cascade, test_image, scaleFactor = 1.1):
        image_copy = tst_image.copy()
        gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors = 5)
    return len(faces_rects)

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

        

        
while(1>0):
    print("\n           *****------*****            \n1)Find number of faces in each image\n2)Sort in order of number of faces\n3)Compare another imgae\n4)Find time complexity of sorting\n5)Find time complexity of comparing\n")
    start = "\033[1m"
    end = "\033[0;0m"
    y = int(input(start + "Enter Your Choice Number_  " + end))
    
    if y == 1:
        x = len(test_image)
        for j in range(0,x):
            print("Faces found in Image ",j+1,end="", flush=True)
            y = facereco(j)
            
    elif y == 2:
        x = len(test_image)
        facearray = []
        for j in range(0,x):
            y = facereco2(j)
            facearray.append(y)
        n = len(facearray) 
        print("Array of number of faces: ",facearray)
        print("\n")
        quickSort(facearray, 0, n-1)
        print("Sorted list in order of number of faces:",end="", flush=True)
        blue(facearray)
        time.sleep(1)
        for i in range(0,n):
            for j in range(0,x):
                if facereco2(j) == facearray[i]:
                    im[j].show()
                    time.sleep(2.7)
                    for proc in psutil.process_iter(): # traverse the current process
                             if proc.name() == "display": # If the name of the process is display
                                     proc.kill()

    elif y == 3:
        
        x = len(test_image)
        facearray = []
        for j in range(0,x):
            y = facereco2(j)
            facearray.append(y)
        
        def find(x,z,facearray):
            e =1
            print("Faces found in entered image: ",end="", flush=True)
            blue(z)
            for j in range(0,x):
                if facearray[j] != z:
                    continue
                else:
                    e = e+1
                    im[j].show()
            if e>1:
                green('\n====> Same number of faces found!')
            else:
                red('\n====> Match not found!')
        
        w = input("Enter image_ ")
        if w == "1.jpg":
            tst_image = cv2.imread('1.jpg')
            im1.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "2.jpg":
            tst_image = cv2.imread('2.jpg')
            im2.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "3.jpg":
            tst_image = cv2.imread('3.jpg')
            im3.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "4.jpg":
            tst_image = cv2.imread('4.jpg')
            im4.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "5.jpg":
            tst_image = cv2.imread('5.jpg')
            im5.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "6.jpg":
            tst_image = cv2.imread('6.jpg')
            im6.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "7.jpg":
            tst_image = cv2.imread('7.jpg')
            im7.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "8.jpg":
            tst_image = cv2.imread('8.jpg')
            im8.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "9.jpg":
            tst_image = cv2.imread('9.jpg')
            im9.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "10.jpg":
            tst_image = cv2.imread('10.jpg')
            im10.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "11.jpg":
            tst_image = cv2.imread('11.jpg')
            im11.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "12.jpg":
            tst_image = cv2.imread('12.jpg')
            im12.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "13.jpg":
            tst_image = cv2.imread('13.jpg')
            im13.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "14.jpg":
            tst_image = cv2.imread('14.jpg')
            im14.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "15.jpg":
            tst_image = cv2.imread('15.jpg')
            im15.show()
            z = facereco3(tst_image)
            find(x,z,facearray)
    
    elif y == 4:
        start = time.time()
        time.sleep(1)
        x = len(test_image)
        facearray = []
        for j in range(0,x):
            y = facereco2(j)
            facearray.append(y)
        n = len(facearray) 
        print("Array of number of faces: ",facearray)
        print("\n")
        quickSort(facearray, 0, n-1)
        blue("ARRAY SORTED" )
        end = time.time()
        print("Execution Time: ",end-start-1)
    
    elif y == 5:
        
        
        x = len(test_image)
        facearray = []
        for j in range(0,x):
            y = facereco2(j)
            facearray.append(y)
            
        
        def find(x,z,facearray):
            s = time.time()
            time.sleep(1)
            e =1
            print("Faces found in entered image: ",end="", flush=True)
            blue(z)
            for j in range(0,x):
                if facearray[j] != z:
                    continue
                else:
                    e = e+1
            if e>1:
                green('\n====> Same number of faces found!')
            else:
                red('\n====> Match not found!')
            e = time.time()
            print("Execution Time of Searching : ",e -s -1)
        
        w = input("Enter image_ ")
        if w == "1.jpg":
            tst_image = cv2.imread('1.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "2.jpg":
            tst_image = cv2.imread('2.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "3.jpg":
            tst_image = cv2.imread('3.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "4.jpg":
            tst_image = cv2.imread('4.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "5.jpg":
            tst_image = cv2.imread('5.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "6.jpg":
            tst_image = cv2.imread('6.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "7.jpg":
            tst_image = cv2.imread('7.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "8.jpg":
            tst_image = cv2.imread('8.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "9.jpg":
            tst_image = cv2.imread('9.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "10.jpg":
            tst_image = cv2.imread('10.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "11.jpg":
            tst_image = cv2.imread('11.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "12.jpg":
            tst_image = cv2.imread('12.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "13.jpg":
            tst_image = cv2.imread('13.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "14.jpg":
            tst_image = cv2.imread('14.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
        elif w == "15.jpg":
            tst_image = cv2.imread('15.jpg')
            z = facereco3(tst_image)
            find(x,z,facearray)
            
