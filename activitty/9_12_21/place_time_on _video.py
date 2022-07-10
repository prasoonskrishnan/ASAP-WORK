import cv2
from datetime import date, datetime

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while cap.isOpened():
    ret,img=cap.read()
    cv2.circle(img, (30, 30), 7, (0, 0, 255), -1)

    cv2.line(img,(20, 20), (270,20),(255,255,255),2)
    cv2.line(img,(620, 20), (370,20),(255,255,255),2)
    cv2.line(img,(20, 460), (270,460),(255,255,255),2)
    cv2.line(img, (620, 460), (370, 460), (255, 255, 255), 2)
    cv2.line(img, (20, 20), (20, 160), (255, 255, 255), 2)
    cv2.line(img, (620, 20), (620, 160), (255, 255, 255), 2)
    cv2.line(img, (20, 460), (20, 300), (255, 255, 255), 2)
    cv2.line(img, (620, 460), (620, 300), (255, 255, 255), 2)

    cv2.putText(img, "Rec", (40, 37), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (255, 255, 255), 1)
    cv2.putText(img,str(date.today()),(22,450),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,255,255),1)
    cv2.putText(img, str(datetime.now().replace(microsecond=0)), (425, 450), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 255), 1)

    cv2.imshow('Output',img)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()