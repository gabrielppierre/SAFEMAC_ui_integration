import cv2
import numpy as np
import time
import camera_utils

# Carrega a rede neural YOLO pré-treinada
net = cv2.dnn.readNetFromDarknet('yolo.cfg', 'yolo.weights')

# Define as classes de objetos a serem detectadas
classes = ['worker']

# Configurações da rede neural
conf_threshold = 0.5
nms_threshold = 0.4

# Carrega os dados de calibração da câmera
calibration_file_path = 'calibration_data.npz'
camera_matrix, dist_coeffs = camera_utils.load_calibration_data(calibration_file_path)

# Captura a imagem da câmera
camera_indices = {0: 'frontal'}
images = camera_utils.image_capture(camera_indices)
img = images['frontal']

# Obtém as dimensões da imagem
(h, w) = img.shape[:2]

# Cria um blob de entrada de imagem para a rede neural
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

# Configura a entrada para a rede neural
net.setInput(blob)

# Obtém as camadas de saída da rede neural
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Executa a detecção de objetos na imagem
outputs = net.forward(output_layers)

# Inicializa as listas de caixas delimitadoras, confiança e IDs de classe
boxes = []
confidences = []
class_ids = []

# Inicializa a variável de contagem de trabalhadores
worker_count = 0

# Itera pelas saídas da rede neural
for output in outputs:
    # Itera pelas detecções
    for detection in output:
        # Obtém as probabilidades de classe e as coordenadas da caixa delimitadora
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > conf_threshold and classes[class_id] == 'worker':
            # Incrementa a contagem de trabalhadores
            worker_count += 1

            # Calcula as coordenadas da caixa delimitadora na imagem original
            box = detection[0:4] * np.array([w, h, w, h])
            (center_x, center_y, width, height) = box.astype('int')
            x = int(center_x - (width / 2))
            y = int(center_y - (height / 2))
            # Adiciona as informações da detecção às listas
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Aplica a supressão não máxima para remover detecções redundantes
indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

# Desenha as caixas delimitadoras na imagem original
for i in indices:
    i = i[0]
    box = boxes[i]
    x, y, w, h = box[0], box[1], box[2], box[3]
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Obtém os pontos 2D e 3D da detecção
    points_2D, points_3D = camera_utils.get_2D_and_3D_points(detection)

    # Calcula as coordenadas 3D médias dos pontos
    mean_3D = np.mean(points_3D, axis=1)

    # Exibe as coordenadas 3D
    print(f"Coordenadas 3D da detecção {i}: ({mean_3D[0]:.2f}, {mean_3D[1]:.2f}, {mean_3D[2]:.2f})")

# Exibe a imagem com as detecções
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Salva a imagem de saída
cv2.imwrite('output.jpg', img)
