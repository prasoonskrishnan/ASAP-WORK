import cv2
cv2.namedWindow('Image')

def print_val(x):
    pass

cv2.createTrackbar('min', 'Image', 0, 255, print_val)
cv2.createTrackbar('max', 'Image', 0, 255, print_val)
while True:
    img = cv2.imread('C:\\Users\\admin\\Documents\\document\\opencv\\lenna.jpg', 0)
    t1 = cv2.getTrackbarPos('min','Image')
    t2 = cv2.getTrackbarPos('max','Image')
    canny = cv2.Canny(img,t1,t2)
    cv2.imshow('Image',canny)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()