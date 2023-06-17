
import os
import numpy
import shutil
import random

def main(blender_images_path, blender_labels_path, output_dataset_path, training_percentage=.7):

    images_names = os.listdir(blender_images_path)
    
    # create the output folder
    if not os.path.exists(output_dataset_path):
        os.makedirs(output_dataset_path)

    out_train_im = os.path.join(output_dataset_path, 'train/images')
    out_train_lb = os.path.join(output_dataset_path, 'train/labels')
    out_test_im  = os.path.join(output_dataset_path, 'test/images')
    out_test_lb  = os.path.join(output_dataset_path, 'test/labels')

    try:        
        os.makedirs(out_train_im)
        os.makedirs(out_train_lb)
        os.makedirs(out_test_im)
        os.makedirs(out_test_lb)
    except:
        pass

    random.shuffle(images_names)

    training_images = images_names[:int(training_percentage*len(images_names)) + 1]
    test_images     = images_names[int(training_percentage*len(images_names)):]

    for idx, partition in enumerate([training_images, test_images]):
        if idx == 0:
            out_im = out_train_im
            out_lb = out_train_lb
        else:
            out_im = out_test_im
            out_lb = out_test_lb

        for image_name in partition:

            class_id = '0'

            labelfile = image_name.replace('.jpg', '.txt').replace('.png', '.txt')

            out_image_name = os.path.join(out_im, image_name)
            out_label_name = os.path.join(out_lb, labelfile)

            org_image_name = os.path.join(blender_images_path, image_name)
            org_label_name = os.path.join(blender_labels_path, labelfile)

            shutil.copy2(org_image_name, out_image_name)

            corners = numpy.loadtxt(org_label_name)

            xmin = max(min(corners[:,0]),0.)
            xmax = min(max(corners[:,0]),1.)
            ymin = max(min(corners[:,1]),0.)
            ymax = min(max(corners[:,1]),1.)

            W = xmax - xmin
            H = ymax - ymin

            corners = corners.flatten()
            
            centroidx = xmin + W/2.
            centroidy = ymin + H/2.

            with open(out_label_name, 'w') as LB:
                LB.write(class_id + ' ')
                LB.write(str(centroidx) + ' ' + str(centroidy) + ' ')
                for corner in corners:
                    LB.write(str(corner) + ' ')
                LB.write(str(W) + ' ' + str(H))


if __name__ == '__main__':

    this_ = os.path.abspath(os.path.dirname(__file__))

    blender_dataset_images = os.path.join(this_, '../../dr-render/render/images')
    blender_dataset_labels = os.path.join(this_, '../../dr-render/render/corners')
    output_dataset_path    = os.path.join(this_, 'rsc2/dataset/urna')

    main(blender_dataset_images, blender_dataset_labels, output_dataset_path, training_percentage=.7)