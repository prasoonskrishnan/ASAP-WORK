import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\admin\\Documents\\document\\opencv\\smarties.png',0)
kernel = np.ones((5,5),np.uint8)
erodeImg = cv2.erode(img,kernel,iterations=1)
erodeImg2 = cv2.erode(img,kernel,iterations=2)
dilImg = cv2.dilate(img,kernel,iterations=1)
dilImg2 = cv2.dilate(img,kernel,iterations=2)
morphop = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
morphcl = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
morphgrad = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
morphth = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
morphbh = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

titles = ['Original','Erode iter=1','Erode iter=2','Dilate iter=1','Dilate iter=2','Opening','Closing','Gradient','Top Hat','Black Hat']
images = [img,erodeImg,erodeImg2,dilImg,dilImg2,morphop,morphcl,morphgrad,morphth,morphbh]
for i in range(len(titles)):
    plt.subplot(4,3,i+1)
    plt.subplots_adjust(hspace=0.400)
    plt.title(titles[i])
    plt.imshow(images[i],'gray')
    plt.xticks([])
    plt.yticks([])
plt.show()