from PIL import Image
import psutil 
import time
import subprocess


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

im = []

n = int(input("Enter number of images : "))
print("Enter name of images:")
for i in range(0, n): 
    ele = input()
    if ele == "1.jpg":
        im.append(im1)
    if ele == "2.jpg":
        im.append(im2)
    if ele == "3.jpg":
        im.append(im3)
    if ele == "4.jpg":
        im.append(im4)
    if ele == "5.jpg":
        im.append(im5)
    if ele == "6.jpg":
        im.append(im6)
    if ele == "7.jpg":
        im.append(im7)
    if ele == "8.jpg":
        im.append(im8)
    if ele == "9.jpg":
        im.append(im9)
    if ele == "10.jpg":
        im.append(im10)

a = len(im)        
        
for i in range(0,a):
    im[i].show()
    time.sleep(2)
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()

        
