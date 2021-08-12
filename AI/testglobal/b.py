import time
import matplotlib.pyplot as plt
from w3lib.url import parse_data_uri
from io import BytesIO
from tensorflow import keras
import os
import sys
import json
import cv2
import numpy as np
import mysql.connector
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# from PIL import Image

import os

gg = 0
# global model
# model = keras.models.load_model(
#     '../model/DenseNet201_for_15_category_origin')
# print('模型載入完畢')
while(gg < 50000000000000000000000):
    print("等待使用中...")
    gg = gg+1
    print(str(gg))
    time.sleep(2)
    if (gg % 2) == 0:
        f = open("test.txt", "r")
        txt = f.read()
        f.close
        print(txt)
