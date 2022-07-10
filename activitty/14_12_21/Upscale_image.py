import cv2
img = cv2.imread('C:\\Users\\admin\\Documents\\document\\opencv\\fish.jpg')
cv2.imshow('Original',img)
dim = (500, 500)
#Upscaling
up = cv2.resize(img,dim,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Up',up)
cv2.waitKey(0)
cv2.destroyAllWindows()