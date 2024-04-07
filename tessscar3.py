import cv2

cap= cv2.VideoCapture("carpro/video.mp4")


while True:
    check , frame = cap.read()
    if check==True:
     cv2.imshow("Frame",frame)
     key = cv2.waitKey(300)
    if key ==300:
        break
    else:
        break



    cap.release()
    cv2.destroyAllWindows()
   
