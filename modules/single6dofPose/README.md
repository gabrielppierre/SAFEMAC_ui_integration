# 6DoF Detection using singleshotpose

## Introduction
This code is a part of Domain Augmentation from Randomized Knowledge (DARK) and provides a model to train and detect objects in 6DoF using Deep Learning and domain randomization.
The implementation was based on YOLO V2 PyToch implementation for 2D detection from [@marvis](https://github.com/marvis/pytorch-yolo2) and [@tekin](https://github.com/microsoft/singleshotpose)

## Features

* **Test a pretrained models**

* **Train and validate the model with own data**

* **Train models using different strategies to combine training sets from different domains (synthetic and real)**

* **Test new models for multiple scenes, cameras, and objects**

* **Generate datasets and annotation for multiple simulated cameras**

* **Detect objects from video or frames**


## Installation

### Prerequisites

The following dependencies are necessary:

* Ubuntu >= 16 or Windows >= 10
* Cuda >= 8.0
* **[Python](https://www.python.org/downloads/)**  == 3.x 
* **[PyTorch](https://pytorch.org/)** >= 1.2.0 
* (Optional) cuDNN >= v5.1

#### Python Libraries

The project contains a requirement.txt to easy installation with the pip package. 

To install all the python requirements run the command in the project folder:
 `sudo pip install -r requirements.txt`

After, for the Ubuntu, check if yaml library was correctly installed:
 `sudo apt-get install libyaml-dev`


## Resources

To train and run the model you'll need to get some files [Google Drive link]()

The Google Drive folder contains:

- Darknet_19: The YOLO V2 pre-trained weights on ImageNet.
- Models: The trained networks on C3PO dataset.
- VOC2012: Background images to generate the augmented train dataset.
- CAD: Folder containing the CAD model of each object.
- yolo-pose.cfg: Configuration file for the network architecture and parameters.
- CFGs: Folder containing the config-file to run the training and validation scripts.
- Cameras intrinsics: yaml files with the intrinsics parameters of each camera used.

### Files and structure description

#### CFGs (Config files)
These files contains the paths to all resources used during training and validation.

- **trainpaths** and **testpaths**: A list containing the paths to folders that will be used on training and test, respectively. Each folder must be inserted in one line, the data will be mixed during training or test.
- **trainpercentages** and **testpercentages**: The percentage of samples used for each folder in trainpaths and testpaths. During the training (or test) the samples of each folder will be sampled randomly.
- **mesh**: path to the object CAD model.
- **backup**: path to save the output model and training logs.
- **backimages**: path to the dataset with background images (applied for training with the real dataset)
- **modelcfg**: path to the network .cfg
- **initweights**: path to the initial weights

#### Dataset Format
For training, the directory of the dataset must contain a folder for each class (object).
Each folder must contain sub-folders for the RGB images, object masks (for real images), and labels (objects corners).
**The files for images, masks and labels must have the same name**.

#### Labels File
The labels file contains the ground-truth for each image in the training/validation set. Each label **must have the same name** as the image it refers to.
The files must be generated as specified below:
**class_id xc/w yc/h x1/w y1/h x2/w y2/h ... x8/w y8/h obj_width/w obj_height/h**

- class_id = object id in the dataset used; 
- (xc, yc) = object centroid projected in the 2D image; 
- (xi, yi) = object 3d bounding box corners projected in the image;  
- (obj_width, obj_height) = 2d bounding box of the object in the image.

Note that the x, y, obj_width and obj_height coordinates are normalized to the image width(w) and height(h).

#### Network config file (yolo-pose.cfg)
Configuration file that define the neural network architecture and hyper-parameters used for training/validation of the model.

#### Weights File
File generated during training containing the adjusted weights of the neural network, which will be used to perform the predictions. It'll be create with the .weights extension.

#### Camera parameters
File (.yml) that defines the intrinsics parameters of the camera used, must contain the values of fx, cx, fy, cx and the distortion coefficients.

## Usage
,
### Generatig the files with own dataset
To generate the dataset for use the detector use the scripts available in libs/util. Check the paths in the scripts and the files necessary to load the data correctly and run:
`python libs/util/convert_data_to_singleshot.py`

For check the dataset distribution to calculate the anchors run:
`python libs/util/generate_anchors_values.py`
Check if all needed files are generated correctly in the specified path.

#### training command line tool

To start a new training, check the config-file.yml that will be used and the resources necessaries. After, it is possible to train a new model using the command:

`python train.py --ymlcfg path/to/config/config-file.yml`

Also, if abspath is False on the config-file.yml you can set the source path from where the resources will be loaded.

`python train.py --ymlcfg path/to/config/config-file.yml --scrpath path/to/rsc`

The model will be trained and the log file and parameters file are generated in the process.
After each epoch interval, the script show in the terminal the metrics values for the model and save the parameters of the model with best accuracy reached.

#### Detection command line tool
A sample to detect objects from images or videos as also included (unlabeled data).
The file load the network parameters, the input data and predicts the pose for each frame in the video/folder.

To use the script run:
`python detect.py`
(Check the paths and arguments defined in the script to use the correct files)

## Authors
- kbc@cin.ufpe.br

## Links
[Reference paper for 6DoF detection](https://arxiv.org/abs/1711.08848)

[YOLO reference](https://www.google.com.br/search?q=yolo9000&ie=&oe=)


