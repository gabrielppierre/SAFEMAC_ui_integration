import os
import cv2
import numpy as np

from vispy import gloo
from plyfile import PlyData
from scipy.spatial.distance import pdist


F = os.path.dirname(os.path.abspath(__file__))

def draw_corners(image, points, color=(0, 255, 0), front=(255, 255, 0),
                 back=(0, 255, 255), size=5, text=False, use_same_color=False):
    image_cp = image.copy()

    p = []

    if use_same_color:
        front, back = color, color

    for i, point in enumerate(points):
        if len(point) == 1:
            x, y = int(point[0][0]), int(point[0][1])
            if i != 0 or len(points) == 8:
                p.append([x, y])
        else:
            x, y = int(point[0]), int(point[1])
            if i != 0 or len(points) == 8:
                p.append([x, y])

        if i == 0:
            current_color = color
        elif i < 5:
            current_color = back
        else:
            current_color = front
        cv2.circle(image_cp, (x, y), size, current_color, -1)
        if text:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image_cp, str(i), (x, y - 5),
                        font, 1, color, 3, cv2.LINE_AA)

    cv2.line(image_cp, (p[0][0], p[0][1]), (p[1][0], p[1][1]), back, 4)
    cv2.line(image_cp, (p[0][0], p[0][1]), (p[2][0], p[2][1]), back, 4)
    cv2.line(image_cp, (p[3][0], p[3][1]), (p[1][0], p[1][1]), back, 4)
    cv2.line(image_cp, (p[3][0], p[3][1]), (p[2][0], p[2][1]), back, 4)

    cv2.line(image_cp, (p[0][0], p[0][1]), (p[4][0], p[4][1]), color, 4)
    cv2.line(image_cp, (p[5][0], p[5][1]), (p[1][0], p[1][1]), color, 4)
    cv2.line(image_cp, (p[6][0], p[6][1]), (p[2][0], p[2][1]), color, 4)
    cv2.line(image_cp, (p[7][0], p[7][1]), (p[3][0], p[3][1]), color, 4)

    cv2.line(image_cp, (p[5][0], p[5][1]), (p[4][0], p[4][1]), front, 4)
    cv2.line(image_cp, (p[6][0], p[6][1]), (p[4][0], p[4][1]), front, 4)
    cv2.line(image_cp, (p[7][0], p[7][1]), (p[5][0], p[5][1]), front, 4)
    cv2.line(image_cp, (p[7][0], p[7][1]), (p[6][0], p[6][1]), front, 4)

    return image_cp


def print_points_and_bb(frame, points, points2d=None):

    cv2.imshow('Original', frame)
    
    corners = draw_corners(frame, points, text=True)
    cv2.imshow('Bound 3D', corners)
    
    if points2d is not None:
        corners2d = frame.copy()
        cv2.rectangle(corners2d, (points2d[0], points2d[1]), (points2d[2], points2d[3]), (0,0,255), 1)
        cv2.imshow('Bound 2D', corners2d)
    
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        exit(1)


if __name__ == '__main__':

    
    DATASET = F + '\\rsc2\\dataset\\urna\\train'
    
    IMGFOLDER     = 'images'
    CORNERSFOLDER = 'labels'
    
    images  = os.listdir(os.path.join(DATASET, IMGFOLDER))
    
    resize_image = (680, 680)
    
    for name in images:
        
        imagePath = os.path.join(DATASET, IMGFOLDER, name) 
        image = cv2.imread(imagePath)
        H, W, C = image.shape
        image = cv2.resize(image, resize_image)

        cfile = imagePath.replace(IMGFOLDER, CORNERSFOLDER).replace('jpg', 'txt').replace('png', 'txt')
        values = np.loadtxt(cfile).flatten()
        corners = values[1:-2].reshape((9,2))
        corners[:, 0] = corners[:, 0] * image.shape[1]
        corners[:, 1] = corners[:, 1] * image.shape[0]
    
        OW, OH = values[-2] * image.shape[1], values[-1] * image.shape[0]
    
        xmin = min(corners[:, 0]) 
        ymin = min(corners[:, 1])
        
        points2d = [int(xmin), int(ymin), int(xmin+OW), int(ymin+OH)]

        print(corners)
        print(points2d)

        print_points_and_bb(image, corners, points2d=points2d)
