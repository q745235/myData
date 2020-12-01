from tensorflow import keras
import cv2
import mysql.connector
import json
import sys


# img = sys.argv[1]
sys.stdout.reconfigure(encoding='utf-8')
def load_image(imgname, width, height):

    img = cv2.imread(imgname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (width, height))
    img = (img / 255.0).reshape((-1, height, width, 3))
    return img

model = keras.models.load_model('./falldown/falldown/d1')
img = load_image("./img/test7.jpg", 200, 200)
percentage = model.predict(img)
print('圖片 : test7')
print('機率 : ' + str(percentage[0][0]))
# print(type(percentage[0][0]))

disease_number = percentage.argmax()

# print(disease_number)

def fall_notfall(b):
    a = ''
    if b < 0.6:
        a = '跌倒'
    else:
        a = '沒跌倒'
    return a
print(fall_notfall(percentage[0][0]))