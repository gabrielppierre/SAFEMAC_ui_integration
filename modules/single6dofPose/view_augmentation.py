from image import augment_without_mask_2

import os
import cv2
import numpy as np

from vispy import gloo
from plyfile import PlyData
from scipy.spatial.distance import pdist


F = os.path.dirname(os.path.abspath(__file__))


def view_aug(frame, frame_name):

    cv2.imshow('Original', frame)
    
    frame2 = augment_without_mask_2(frame_name, (416, 416), 0.2, 0.1, 1.5, 1.5)

    cv2.imshow('augmented', frame2)
    
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        exit(1)


if __name__ == '__main__':

    
    DATASET = F + '\\rsc2\\dataset\\urna\\train'
    
    IMGFOLDER     = 'images'
    
    images  = os.listdir(os.path.join(DATASET, IMGFOLDER))
    
    resize_image = (680, 680)
    
    for name in images:
        
        imagePath = os.path.join(DATASET, IMGFOLDER, name) 
        image = cv2.imread(imagePath)
        H, W, C = image.shape
        image = cv2.resize(image, resize_image)
        view_aug(image, imagePath)
