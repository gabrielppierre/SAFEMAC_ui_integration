import cv2
import yaml
from .single6dofPose.model3d import Model3D
import numpy
import json

class Darknet_dummy():
    def __init__(self, labels_file, camera_matrix_file, obj_model):
        self.cont = 0
        self.labels = self.read_json(labels_file)
        self.cameras = self.read_json(camera_matrix_file)
        self.mesh = Model3D(obj_model)

    def detect(self, image_id):
        image_id = str(self.cont)
        camera = numpy.array(self.cameras[image_id]['cam_K']).reshape((3,3))
        dist = numpy.array([0.,0.,0.,0.,0.])
        R = numpy.array(self.labels[image_id][0]['cam_R_m2c']).reshape((3,3))
        t = numpy.array(self.labels[image_id][0]['cam_t_m2c']).reshape((1,3))
        image_points, _ = cv2.projectPoints(numpy.asarray(self.mesh.vertices), R, t, camera, dist)
        image_points = numpy.squeeze(image_points, axis=1)
        self.cont += 1
        return image_points

    def read_yaml(self, filename):
        with open(filename) as f:
            yml_data = yaml.load(f, Loader=yaml.SafeLoader)
        return yml_data
        
    def read_json(self, filename):
        with open(filename) as f:
            data = json.load(f)
        return data
