# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:45:28 2018

@author: DELL
"""

import cv2
import numpy as np
img=cv2.imread("C:\\Users\\DELL\\Desktop\\opencv_operations\\histogram.jpg",0)
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cll=clahe.apply(img)
while True:
    key=cv2.waitKey(1)&0xFF
    if key==27:
        break
    img1 = cv2.resize(img,(500,500),2)
    cv2.imshow('original_img',img1)
    hst_equalized = cv2.resize(cll,(500,500),2)
    cv2.imshow('histogram_equalized_img',hst_equalized)
    cv2.imwrite("C:\\Users\\DELL\\Desktop\\opencv_operations\\histogram_equalisation\\original_img.jpg",img1)
    cv2.imwrite("C:\\Users\\DELL\\Desktop\\opencv_operations\\histogram_equalisation\\histogram_equalised_image.jpg",hst_equalized)
cv2.destroyAllWindows()    
    