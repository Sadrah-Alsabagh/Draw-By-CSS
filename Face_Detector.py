import cv2

#Load some pre-trained data on face frontals from opencv (haar cascade algorithim)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
img = cv2.imread('smith.jpg')

#Convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces
face_coordinates = face_cascade.detectMultiScale(grayscaled_img)
# print(face_coordinates)

#Draw rectangles around the faces 
cv2.rectangle(img,(747,233),(747+1004,233+1004), (0,255,0),2)

#

cv2.imshow('Face Detector' , img )
cv2.waitKey()
print('code completed')