import cv2
import numpy as np

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	eyes = eye_cascade.detectMultiScale(gray)
	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(gray,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
	cv2.imshow('img',gray)
	h = str(type(eyes))
	if h == "<class 'tuple'>":
		print("open your eyes")
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cv2.destroyAllWindows()
cap.release()
