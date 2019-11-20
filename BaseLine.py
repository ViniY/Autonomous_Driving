import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2
from tqdm import tqdm  # _notebook as tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from functools import reduce
import os
from sklearn.model_selection import train_test_split
from scipy.optimize import minimize


PATH = '/Users/vini/Desktop/Autonomous_Driving'
os.listdir(PATH)


# Load data
def load_data():
    train = pd.read_csv(PATH + 'train.csv')
    test = pd.read_csv(PATH + 'sample_submission.csv')

    # From camera.zip
    camera_matrix = np.array([[2304.5479, 0, 1686.2379],
                              [0, 2305.8757, 1354.9849],
                              [0, 0, 1]], dtype=np.float32)
    camera_matrix_inv = np.linalg.inv(camera_matrix)

    train.head()


# **ImageId** column contains names of images:


def imread(path, fast_mode=False):
    img = cv2.imread(path)
    if not fast_mode and img is not None and len(img.shape) == 3:
        img = np.array(img[:, :, ::-1])
    return img


img = imread(PATH + 'train_images/ID_8a6e65317' + '.jpg')
IMG_SHAPE = img.shape

plt.figure(figsize=(15, 8))
plt.imshow(img);
