import time
dir=input("enter the direction:")
def east():
    east.st=1
    east.r=1
    print('east side can go straight')
    print('east side can go north')
    west.st=0
    west.r=0
    north.st=0
    north.r=0
    south.st=0
    south.r=0
def west():
    east.st=0
    east.r=0
    west.st=1
    west.r=1
    print('west side can go straight')
    print('west side can go south')
    north.st=0
    north.r=0
    south.st=0
    south.r=0
def north():
    east.st=0
    east.r=0
    west.st=0
    west.r=0
    north.st=1
    north.r=1
    print('north side can go straight')
    print('north side can go west')
    south.st=0
    south.r=0
def south():
    east.st=0
    east.r=0
    west.st=0
    west.r=0
    north.st=0
    north.r=0
    south.st=1
    south.r=1
    print('south side can go straight')
    print('south side can go east')

# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import cv2
 
# capture frames from a video
cap = cv2.VideoCapture('snow.mp4')
 
# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')
 
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
     
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
 
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    t=0
    # To draw a rectangle in each cars
    #east=1
    #west=2
    #north=3
    #soutn=4
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        t=1
 
   # Display frames in a window 
    cv2.imshow('video2', frames)
     
    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
def countdown(n):
    for i in range(n):
        print(n - i)
        time.sleep(1)
while t==1:
    if dir=='east':
        countdown(3)
        east()
        time.sleep(3)
        break;
    if dir=='west':
        countdown(3)
        west()
        time.sleep(3)
        break;
    if dir=='north':
        #countdown(3)
        #north()
        #time.sleep(3)
        break;
    if dir=='south':
        countdown(3)
        south()
        time.sleep(3)
        break;
# De-allocate any associated memory usage
cv2.destroyAllWindows()