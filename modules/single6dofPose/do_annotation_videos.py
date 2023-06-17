import re
import os
import cv2
import torch
import tqdm

import numpy as np

from PIL import Image
from darknet import Darknet
from torchvision import transforms
from utils import get_region_boxes
from torch.autograd import Variable
from vispy import gloo
from plyfile import PlyData
from scipy.spatial.distance import pdist


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


class Model3D(object):
    def __init__(self, file_to_load=None):
        self.vertices = None
        self.centroid = None
        self.indices = None
        self.colors = None
        self.texcoord = None
        self.texture = None
        self.collated = None
        self.vertex_buffer = None
        self.index_buffer = None
        self.bb = None
        self.bb_vbuffer = None
        self.bb_ibuffer = None
        self.diameter = None

        if file_to_load:
            self.load(file_to_load)

        self._compute_bbox()

    def _compute_bbox(self):
        self.bb = []

        minx, maxx = min(self.vertices[:, 0]), max(self.vertices[:, 0])
        miny, maxy = min(self.vertices[:, 1]), max(self.vertices[:, 1])
        minz, maxz = min(self.vertices[:, 2]), max(self.vertices[:, 2])

        self.bb.append([minx, miny, minz])
        self.bb.append([minx, miny, maxz])
        self.bb.append([minx, maxy, minz])
        self.bb.append([minx, maxy, maxz])
        self.bb.append([maxx, miny, minz])
        self.bb.append([maxx, miny, maxz])
        self.bb.append([maxx, maxy, minz])
        self.bb.append([maxx, maxy, maxz])
        self.bb = np.asarray(self.bb, dtype=np.float32)

        self.diameter = max(pdist(self.bb, 'euclidean'))

        colors  = [[1, 0, 0],[1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1], [0, 1, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]]
        indices = [0, 1, 0, 2, 3, 1, 3, 2, 4, 5, 4, 6, 7, 5, 7, 6, 0, 4, 1, 5, 2, 6, 3, 7]

        vertices_type = [('a_position', np.float32, 3), ('a_color', np.float32, 3)]
        collated = np.asarray(list(zip(self.bb, colors)), vertices_type)

        self.bb_vbuffer = gloo.VertexBuffer(collated)
        self.bb_ibuffer = gloo.IndexBuffer(indices)

    def load(self, path, demean=False, scale=1.0):
        data = PlyData.read(path)
        self.vertices = np.zeros((data['vertex'].count, 3))
        self.vertices[:, 0] = np.array(data['vertex']['x'])
        self.vertices[:, 1] = np.array(data['vertex']['y'])
        self.vertices[:, 2] = np.array(data['vertex']['z'])
        self.vertices *= scale
        self.centroid = np.mean(self.vertices, 0)

        if demean:
            self.centroid = np.zeros((1, 3), np.float32)
            self.vertices -= self.centroid

        self._compute_bbox()

        self.indices = np.asarray(list(data['face']['vertex_indices']), np.uint32)

        filename = path.split('/')[-1]
        abs_path = path[:path.find(filename)]
        tex_to_load = None
        if os.path.exists(abs_path + filename[:-4] + '.jpg'):
            tex_to_load = abs_path + filename[:-4] + '.jpg'
        elif os.path.exists(abs_path + filename[:-4] + '.png'):
            tex_to_load = abs_path + filename[:-4] + '.png'

        if tex_to_load is not None:
            image = cv2.flip(cv2.imread(tex_to_load, cv2.IMREAD_UNCHANGED), 0)
            self.texture = gloo.Texture2D(image)

            if 'texcoord' in str(data):
                self.texcoord = np.asarray(list(data['face']['texcoord']))
                assert self.indices.shape[0] == self.texcoord.shape[0]
                temp = np.zeros((data['vertex'].count, 2))
                temp[self.indices.flatten()] = self.texcoord.reshape((-1, 2))
                self.texcoord = temp

            elif 'texture_u' in str(data):
                self.texcoord = np.zeros((data['vertex'].count, 2))
                self.texcoord[:, 0] = np.array(data['vertex']['texture_u'])
                self.texcoord[:, 1] = np.array(data['vertex']['texture_v'])

        if self.texcoord is not None:
            vertices_type = [('a_position', np.float32, 3), ('a_texcoord', np.float32, 2)]
            self.collated = np.asarray(list(zip(self.vertices, self.texcoord)), vertices_type)

        else:
            self.colors = 0.5*np.ones((data['vertex'].count, 3))
            if 'blue' in str(data):
                self.colors[:, 0] = np.array(data['vertex']['blue'])
                self.colors[:, 1] = np.array(data['vertex']['green'])
                self.colors[:, 2] = np.array(data['vertex']['red'])
                self.colors /= 255.0
            else:
                pass
            vertices_type = [('a_position', np.float32, 3), ('a_color', np.float32, 3)]
            self.collated = np.asarray(list(zip(self.vertices, self.colors)), vertices_type)

        self.vertex_buffer = gloo.VertexBuffer(self.collated)
        self.index_buffer = gloo.IndexBuffer(self.indices.flatten())
        
def draw_corners(image, points, color=(0, 255, 0), front= (255, 255, 0), 
                 back= (0, 255, 255), size=5, text=False, use_same_color=False):
    image_cp = image.copy()
    
    p = []

    if use_same_color:
        front, back = color, color

    for i, point in enumerate(points):
        if len(point) == 1:
            x, y = int(point[0][0]), int(point[0][1])
            if i != 0 or len(points) == 8:
                p.append([x,y])
        else:
            x, y = int(point[0]), int(point[1])
            if i != 0 or len(points) == 8:
                p.append([x,y])

        if i == 0:
            current_color = color
        elif i < 5:
            current_color = back
        else:
            current_color = front
        cv2.circle(image_cp, (x, y), size, current_color, -1)
        if text:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image_cp , str(i), (x, y - 5), font, 1, color, 3, cv2.LINE_AA)

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

def draw_triangle(image, vertices, color=(0, 255, 0)):
    image_copy = image.copy()
    points = vertices.reshape((-1,1,2))
    cv2.polylines(image_copy, [points], True, color)
    return image_copy

def draw_mesh(image, vertices2d, indices):
    img = image.copy()
    for index in indices:
        triangle = np.array([vertices2d[index[0]], vertices2d[index[1]], vertices2d[index[2]]], dtype='int32')
        img = draw_triangle(img, triangle)
    return img

def print_annotation(imagespath, labelpath, target_shape=(680, 680), modelCAD=None, outputpath=None, video_name='video', max_number_frames=270):
    
    imageslist = os.listdir(imagespath)
    imageslist.sort(key=natural_keys)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
	
    frames_video_writer = cv2.VideoWriter(os.path.join(outputpath, f'{video_name}_frames.mp4'), fourcc, 30.0, target_shape)
    bbs_video_writer = cv2.VideoWriter(os.path.join(outputpath, f'{video_name}_bounding_box.mp4'), fourcc, 30.0, target_shape)
    pose_video_writer = cv2.VideoWriter(os.path.join(outputpath, f'{video_name}_poses.mp4'), fourcc, 30.0, target_shape)

    if len(imageslist) > max_number_frames:
        imageslist = imageslist[:max_number_frames]
 
    for imagename in tqdm.tqdm(imageslist):
        
        labelvalues = np.loadtxt(os.path.join(labelpath, imagename.replace('.jpg', '.txt')))
        corners2D = labelvalues[1:-2].reshape((9,2))
        
        corners2D[:, 0] = corners2D[:, 0] * target_shape[0]
        corners2D[:, 1] = corners2D[:, 1] * target_shape[1]
        
        import numpy 
        noise = numpy.random.uniform(low=-1.0, high=5.0, size=(9,2))
        corners2D = corners2D + noise
        
        cvImage = cv2.imread(os.path.join(imagespath, imagename))
        cvImage = cv2.resize(cvImage, dsize=target_shape)
        cornersImage = draw_corners(cvImage, corners2D)
        
        modelObj = Model3D(modelCAD)
        vertices = modelObj.vertices
        
        # iphone x
        camera = np.array([[1.8124700969190962e+03, 0., 9.3398674640549461e+02], [0., 1.8053196305605904e+03, 4.9850903539305631e+02], [0., 0., 1.]])
        coeffs = np.array([2.2248648661554429e-01, -1.3546714869588965e+00, -8.4965799864005973e-04, -4.6325679386822975e-03, 2.7111820270639861e+00])
        
        camera[0, 0] = camera[0, 0] * target_shape[0] / 1920
        camera[0, 2] = camera[0, 2] * target_shape[0] / 1920
        camera[1, 1] = camera[1, 1] * target_shape[1] / 1080
        camera[1, 2] = camera[1, 2] * target_shape[1] / 1080
        
        _, rvec, tvec = cv2.solvePnP(modelObj.bb, corners2D[1:], camera, coeffs)
        vertices2D, _ = cv2.projectPoints(vertices, rvec, tvec, camera, coeffs)
        meshImage = draw_mesh(cvImage, vertices2D, modelObj.indices)
         
        frames_video_writer.write(cvImage)
        bbs_video_writer.write(cornersImage)
        pose_video_writer.write(meshImage)
        
    frames_video_writer.release()
    bbs_video_writer.release()
    pose_video_writer.release()


def do_annotation_videos(objects, scenes, cameras, datasetpath, outputpath, cadpath):
    
    for camera in cameras:
        for obj in objects:
            for scene in scenes:
                objcadpath = os.path.join(cadpath, obj, f'{obj}.ply')
                imagespath = os.path.join(datasetpath, camera, scene, obj, 'images')
                labelspath = os.path.join(datasetpath, camera, scene, obj, 'labels')
                print_annotation(imagespath, labelspath, modelCAD=objcadpath, outputpath=outputpath, video_name=f'{camera}_{scene}_{obj}')

if __name__ == '__main__':
    
    DATASETPATH = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\data\\TEST'
    OUTPUTPATH  = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\POSE_ANNOTATIONS2'
    CADPATH     = 'E:\\kbc\\PRL21\\dr2pe\\rsc\\CAD'
    CAMERAS     = ['X']
    
    OBJECTS    = ['bunny']
    SCENES     = ['color']
    
    do_annotation_videos(OBJECTS, SCENES, CAMERAS, DATASETPATH, OUTPUTPATH, CADPATH)
    
    OBJECTS     = ['bunny']
    CAMERAS     = ['S8', 'EOS']
    SCENES      = ['basic']
    
    #do_annotation_videos(OBJECTS, SCENES, CAMERAS, DATASETPATH, OUTPUTPATH, CADPATH)
    
    