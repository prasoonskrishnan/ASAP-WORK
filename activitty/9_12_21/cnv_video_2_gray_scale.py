import cv2
cap = cv2.VideoCapture('C:\\Users\\admin\\Documents\\document\\opencv\\vdo.avi')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('C:\\Users\\admin\\Documents\\document\\opencv\\myvdo.avi',fourcc,30,(720,528))
while cap.isOpened():
    ret,img=cap.read()
    if ret==True:
        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Output',gray_img)
        out.write(gray_img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()