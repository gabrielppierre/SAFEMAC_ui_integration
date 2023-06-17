#!/usr/bin/python
# encoding: utf-8

import os
import glob
import random
from PIL import Image
import numpy as np
from image import *
import torch

from torch.utils.data import Dataset
from utils import read_truths_args, read_truths, get_all_files


class listDataset(Dataset):

    def __init__(self, imagespath, 
                 percentages, 
                 ext='.jpg', shape=None, 
                 shuffle=True, transform=None, 
                 target_transform=None, train=False, 
                 seen=0, batch_size=64, num_workers=4, 
                 cell_size=32, bg_file_names=None, num_keypoints=9, max_num_gt=50, labels_dir=None, masks_dir=None):
        
        print(f'PATHS:       {imagespath}')
        print(f'PERCENTAGES: {percentages}')
        
        images = []
        for idx, datapath in enumerate(imagespath):
            dataimages = [os.path.join(datapath, imname) for imname in os.listdir(datapath)]
            if shuffle:
                random.shuffle(dataimages)
            num_images = int(len(dataimages)*percentages[idx])
            print(f'number_of_images: {num_images}')
            dataimages = dataimages[:num_images]
            images = images + dataimages

        # Initialize variables
        self.lines = images
        
        self.images_path = imagespath

        #if not labels_dir is None:
        #    self.labels_dir = labels_dir
        #else:
        #    self.labels_dir = imagespath.replace('images', 'labels').replace('JPEGImages', 'labels')
        
        #if not masks_dir is None:
        #    self.masks_dir = masks_dir
        #else:
        #    self.masks_dir = imagespath.replace('images', 'masks').replace('JPEGImages', 'masks')
        
        self.nSamples = len(self.lines)
        self.transform = transform
        self.target_transform = target_transform
        self.train = train
        self.shape = shape
        self.seen = seen
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.bg_file_names = bg_file_names
        self.cell_size = cell_size
        self.nbatches = self.nSamples // self.batch_size
        self.num_keypoints = num_keypoints
        self.max_num_gt = max_num_gt 

    # Get the number of samples in the dataset
    def __len__(self):
        return self.nSamples

    def set_samples_size(self, index):

        if self.train and index % self.batch_size == 0:
            if self.seen < 10*self.nbatches*self.batch_size:
                width = 13*self.cell_size
                self.shape = (width, width)
            elif self.seen < 20*self.nbatches*self.batch_size:
                width = (random.randint(0, 7) + 13)*self.cell_size
                self.shape = (width, width)
            elif self.seen < 30*self.nbatches*self.batch_size:
                width = (random.randint(0, 9) + 12)*self.cell_size
                self.shape = (width, width)
            elif self.seen < 40*self.nbatches*self.batch_size:
                width = (random.randint(0, 11) + 11)*self.cell_size
                self.shape = (width, width)
            elif self.seen < 50*self.nbatches*self.batch_size:
                width = (random.randint(0, 13) + 10)*self.cell_size
                self.shape = (width, width)
            elif self.seen < 60*self.nbatches*self.batch_size:
                width = (random.randint(0, 15) + 9)*self.cell_size
                self.shape = (width, width)
            elif self.seen < 70*self.nbatches*self.batch_size:
                width = (random.randint(0, 17) + 8)*self.cell_size
                self.shape = (width, width)
            else:
                width = (random.randint(0, 19) + 7)*self.cell_size
                self.shape = (width, width)

    # Get a sample from the dataset
    def __getitem__(self, index):

        # Ensure the index is smallet than the number of samples in the dataset, otherwise return error
        assert index <= len(self), 'index range error'

        # Get the image path
        imgpath = self.lines[index].rstrip()

        # Decide which size you are going to resize the image depending on the epoch (10, 20, etc.)
        self.set_samples_size(index)

        sample_name = os.path.basename(imgpath)
        #labelfilename = os.path.join(self.labels_dir, sample_name.replace('png', 'txt').replace('jpg', 'txt'))
        labelfilename  = imgpath.replace('png', 'txt').replace('jpg', 'txt')
        labelfilename  = labelfilename.replace('images', 'labels').replace('JPEGImages', 'labels')

        jitter = 0.2
        hue = 0.1
        saturation = 1.5
        exposure = 1.5
        aug_chance = random.uniform(0,1)

        onlySythetic = True
        if self.train and not ('synthetic' in imgpath) and not onlySythetic:
            
            #maskfilename = os.path.join(self.masks_dir, sample_name.replace('jpg', 'png'))
            maskfilename = imgpath.replace('jpg', 'png')
            maskfilename = maskfilename.replace('images', 'masks').replace('JPEGImages', 'masks')
            
            # Get background image path
            random_bg_index = random.randint(0, len(self.bg_file_names) - 1)
            bgpath = self.bg_file_names[random_bg_index]

            # Get the data augmented image and their corresponding labels
            img, label = load_data_detection(
                imgpath, labelfilename, maskfilename, 
                self.shape, jitter, hue, saturation, exposure, 
                bgpath, self.num_keypoints, self.max_num_gt)

            # Convert the labels to PyTorch variables
            label = torch.from_numpy(np.array(label, dtype=np.float32))

        elif self.train and aug_chance > .3:  
            img, label = augment_without_mask(imgpath, labelfilename, 
            self.shape, jitter, hue, saturation, exposure,
            self.num_keypoints, self.max_num_gt)
            label = torch.from_numpy(np.array(label, dtype=np.float32))

        else:       
            # Get the validation image, resize it to the network input size
            img = Image.open(imgpath).convert('RGB')
            if self.shape:
                img = img.resize(self.shape)

            # Read the validation labels, allow upto 50 ground-truth objects in an image
            labpath = imgpath.replace('images', 'labels').replace('JPEGImages', 'labels').replace('.jpg', '.txt').replace('.png', '.txt').replace('frames', 'labels')
            num_labels = 2*self.num_keypoints + 3  
            label = torch.zeros(self.max_num_gt*num_labels)
            if os.path.getsize(labpath):
                ow, oh = img.size
                tmp = torch.from_numpy(read_truths_args(labpath))
                tmp = tmp.view(-1)
                tsz = tmp.numel()
                if tsz > self.max_num_gt*num_labels:
                    label = tmp[0:self.max_num_gt*num_labels]
                elif tsz > 0:
                    label[0:tsz] = tmp

        # Tranform the image data to PyTorch tensors
        if self.transform is not None:
            img = self.transform(img) 

        # If there is any PyTorch-specific transformation, transform the label data
        if self.target_transform is not None:
            label = self.target_transform(label)

        # Increase the number of seen examples
        self.seen = self.seen + self.num_workers

        # Return the retrieved image and its corresponding label
        return (img, label)
