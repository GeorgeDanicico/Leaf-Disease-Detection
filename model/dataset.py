import os

import torch
from PIL import Image
import numpy as np
from torchvision import datasets, models, transforms
from torch.utils import data
from torchvision.datasets.folder import pil_loader


class LeafDiseaseClassifierDataset(data.Dataset):
    def __init__(self, images, labels, transform=None):
        self.images = images
        self.labels = labels
        self.classes = list(set(labels))
        self.class_to_label = {c: i for i, c in enumerate(self.classes)}
        self.image_size = 224
        self.transform = transform
        # self.transforms = transforms.Compose([transforms.Resize(self.image_size),
        #                                       transforms.CenterCrop(self.image_size),
        #                                       transforms.ToTensor(),
        #                                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        #                                       ])

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        # Read the image and label from the list
        loaded_image = pil_loader(self.images[index]).convert("RGB")
        image_label = self.labels[index]
        if self.transform:
            loaded_image = self.transform(loaded_image)

        return loaded_image, image_label


def load_data(root_dir):
    images = []
    plant_labels = []
    disease_labels = []
    image_size = 224

    # Iterate over the files in the root directory
    for subdir, dirs, files in os.walk(root_dir):
        for dir in dirs:
            dir_path = root_dir + "/" + dir
            [plant, disease] = dir.split("___")
            for _, _, photos in os.walk(dir_path):
                for index in range(0, len(photos), 2):
                    images.append(dir_path + "/" + photos[index])
                    plant_labels.append(plant)
                    disease_labels.append(disease)

    transform = transforms.Compose([transforms.Resize(image_size),
                                    transforms.CenterCrop(image_size),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                    ])

    return LeafDiseaseClassifierDataset(images, plant_labels, transform=transform), LeafDiseaseClassifierDataset(images, disease_labels, transform=transform)
