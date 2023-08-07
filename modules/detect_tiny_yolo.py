# detect_tiny_yolo.py
import cv2
import darknet

class Tiny_YOLO:
    def __init__(self):
        config_file = "/path/to/yolov4-tiny.cfg"
        weights_file = "/path/to/yolov4-tiny.weights"
        class_names_file = "modules\detector_configs\coco.names"

        self.network, self.class_names, self.class_colors = darknet.load_network(config_file, weights_file, class_names_file)

    def detect(self, image):
        detections = darknet.detect_image(self.network, self.class_names, image)
        pedestrians = [d for d in detections if d[0] == 'person']
        return pedestrians

    def draw_boxes(self, image, detections):
        for label, confidence, bbox in detections:
            x, y, w, h = darknet.bbox2points(bbox)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return image
