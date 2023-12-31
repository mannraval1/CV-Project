# -*- coding: utf-8 -*-
"""ObjectDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nRVbErswbFLyZfbwk61VEQvbxKmw1WwK
"""

from google.colab import drive

drive.mount('/content/gdrive')

ROOT_DIR = '/content/gdrive/My Drive/Project2'

!pip install ultralytics

import os

from ultralytics import YOLO


# Load a model
model = YOLO("yolov8m.yaml")  # build a new model from scratch

# Use the model
results = model.train(data=os.path.join(ROOT_DIR, "google_colab_config.yaml"), epochs=125)  # train the model

!cp -r /content/runs '/content/gdrive/My Drive/Project2'