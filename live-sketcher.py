import cv2
import numpy as np
def sketch(image):
    imggray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imggrayblur=cv2.GaussianBlur(imggray, (5,5), 0)
    canny=cv2.Canny(imggrayblur, 10, 70)
    ret, mask=cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
    
