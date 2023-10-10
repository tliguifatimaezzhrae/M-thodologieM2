import os
from PIL import Image
import numpy as np

def load_images(folder_path):
    images = []
    labels = []
    class_labels = {"NORMAL": 0, "PNEUMONIA": 1}
    
    for folder in os.listdir(folder_path):
        img_folder = os.path.join(folder_path, folder)
        label = class_labels[folder]
        for img_file in os.listdir(img_folder):
            img_path = os.path.join(img_folder, img_file)
            # load image if not corrupted
            try:
                img = Image.open(img_path)
                # resize image
                img = img.resize((128, 128))
                images.append(img)
                labels.append(label)
            except Exception as e:
                print(f"Error loading image {img_path}")

    
    return images, labels

def load_image(img_path):
    img_list = []
    try:
        img = Image.open(img_path)
        # resize image
        img = img.resize((128, 128))
        img_list.append(img)
    except Exception as e:
        print(f"Error loading image {img_path}")
    return img_list