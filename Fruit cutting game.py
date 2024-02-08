import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import mouse
import pyautogui




cap=cv2.VideoCapture(0)
w=512
h=512
cap.set(3,w)
cap.set(4,h)
detector=HandDetector()
k=50
while (True):
    _,image=cap.read()
    image=cv2.flip(image,1)
    cv2.rectangle(image,(k,k),(w-k,h-k),(0,0,255),3)


    hand,new_image=detector.findHands(image)
    if hand:
        lmlist=hand[0]["lmList"]
        x,y=lmlist[8][0],lmlist[8][1]
        con_x=int(np.interp(x,(0,w-k),(0,1365)))
        con_y=int(np.interp(y,(0,h-k),(0,762)))
        mouse.move(con_x,con_y)
        up=detector.fingersUp(hand[0])
        if lmlist[8][1]<lmlist[7][1]:

            pyautogui.mouseDown()




    cv2.imshow("image",image)
    if cv2.waitKey(1) == ord("s"):
        break
