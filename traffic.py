import cv2
 
# capture frames from a video
cap = cv2.VideoCapture('video.avi')
 
car_cascade = cv2.CascadeClassifier('cars.xml')
 
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
     
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
 
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
     
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
 
    cv2.imshow('video2', frames)
     
    if cv2.waitKey(33) == 27:
        break
 
cv2.destroyAllWindows()