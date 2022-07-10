import cv2
import numpy as np
#Black image
arr1 = np.zeros((250,250,3))
cv2.imshow('Black',arr1)

#White image
arr2 = np.ones((250,250,3))
cv2.imshow('White',arr2)

#Blue image
arr3 = np.zeros((250,250,3))
arr3[:,:,:] = [255,0,0]
cv2.imshow('Blue',arr3)

#Green image
arr4 = np.zeros((250,250,3))
arr4[:,:,:] = [0,255,0]
cv2.imshow('Green',arr4)

#Red image
arr5 = np.zeros((250,250,3))
arr5[:,:,:] = [0,0,255]
cv2.imshow('Red', arr5)
cv2.waitKey(0)
cv2.destroyAllWindows()
