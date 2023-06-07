import cv2
import urllib.request
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(maxHands =1, detectionCon=0.8)
cap = cv2.VideoCapture(0)
while True:
    ret, photo = cap.read()
    hand = detector.findHands(photo,draw=False)
    
    if hand != []:
        detectHand = hand[0]
        if detectHand:
            fingerup = detector.fingersUp(detectHand)
            if fingerup == [1, 0, 0, 0, 0]:
                print("Thumb finger ")
                
            elif fingerup == [1,1,0,0,0]:
                print("Thumb and index finger")
                
            elif fingerup == [1,1,1,0,0]:
                print("Thumb , index and middle finger")
                
            elif fingerup == [1,1,1,1,0]:
                print("Thumb , index , middle and ring finger")
                
            elif fingerup == [1,1,1,1,1]:
                print("all five fingers up")
                
            elif fingerup ==  [0,1,1,0,0]:
                print("index and middle finger")
                #AI model
                request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/unlock')
                print(request_url.read())
                break
            elif fingerup == [0,1,1,1,0]:
                print("middle three fingers up")
                request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/lock')
                print(request_url.read())
                break
                
        print(detector.fingersUp(detectHand))
    
    cv2.imshow("my photo", photo)
    if  cv2.waitKey(10) == 13:
        break
        
cv2.destroyAllWindows()
cap.release()
