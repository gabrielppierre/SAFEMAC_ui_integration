
import re
import os
import cv2

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def image_to_video(SUBFOLDERS, PATH_IMAGES):

    for SUBFOLDER in SUBFOLDERS:
        VIDEO_PATH  = PATH_IMAGES + '_' + SUBFOLDER.upper() + '.mp4'
        
        IMAGESPATH  = os.path.join(PATH_IMAGES, SUBFOLDER)
        
        imagesnames = os.listdir(IMAGESPATH)
        imagesnames.sort(key=natural_keys)
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
        video = cv2.VideoWriter(VIDEO_PATH, fourcc, 30, (416, 416))
        
        for name in imagesnames:
            image = cv2.imread(os.path.join(IMAGESPATH, name))
            video.write(image)
        
        video.release()
        

if __name__ == '__main__':
    
    SUBFOLDERS  = ['bb', 'frame', 'mesh']
    
    #PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_BUNNY'
    #image_to_video(SUBFOLDERS, PATH_IMAGES)
    
    PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_BUNNY_BASIC'
    image_to_video(SUBFOLDERS, PATH_IMAGES)
    
    PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_BUNNY_FAST'
    image_to_video(SUBFOLDERS, PATH_IMAGES)

    PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_BUNNY_OCCLUSION'
    image_to_video(SUBFOLDERS, PATH_IMAGES)

    PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_CAR_BASIC'
    image_to_video(SUBFOLDERS, PATH_IMAGES)
    
    PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_CAR_FAST'
    image_to_video(SUBFOLDERS, PATH_IMAGES)

    #PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_CAR_OCCLUSION'
    #image_to_video(SUBFOLDERS, PATH_IMAGES)
    
    PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_SQUIRREL_BASIC'
    image_to_video(SUBFOLDERS, PATH_IMAGES)
    
    PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_SQUIRREL_FAST'
    image_to_video(SUBFOLDERS, PATH_IMAGES)

    PATH_IMAGES = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\OUTPUT_DETECTED\\FT_X_SQUIRREL_OCCLUSION'
    image_to_video(SUBFOLDERS, PATH_IMAGES)

