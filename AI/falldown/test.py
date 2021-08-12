import cv2 as cv
import numpy as np
import argparse
from PIL import ImageFont, ImageDraw, Image
import requests
import time
import datetime
from tensorflow import keras
import json
import os

#frame = np.zeros((400, 400, 3), np.uint8)
#frame.fill(90)
#text = 'Fall-Detection!'

# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='Path to image or video. Skip to capture frames from camera')
# parser.add_argument('--thr', default=0.2, type=float, help='Threshold value for pose parts heat map')
# parser.add_argument('--width', default=368, type=int, help='Resize input to specific width.')
# parser.add_argument('--height', default=368, type=int, help='Resize input to specific height.')

# args = parser.parse_args()

BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,"LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
"RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

cap = cv.VideoCapture('./falldown/cs4.mp4')


net = cv.dnn.readNetFromTensorflow("./falldown/graph_opt.pb")
inWidth = 368
inHeight = 368
#cap = cv.VideoCapture(args.input if args.input else 0)

model = keras.models.load_model('./falldown/saved_model/my_model/')
while cv.waitKey(1) < 0:
    hasFrame, frame = cap.read()
    if not hasFrame:
        cv.waitKey()
        break

    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    

    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()
    out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        # Slice heatmap of corresponging body's part.
        heatMap = out[0, i, :, :]

        # Originally, we try to find all the local maximums. To simplify a sample
        # we just find a global one. However only a single pose at the same time
        # could be detected this way.
        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        # Add a point if it's confidence is higher than threshold.
        points.append((int(x), int(y)) if conf > 0.2 else None)
        #print(int(x), int(y))

    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        assert(partFrom in BODY_PARTS)
        assert(partTo in BODY_PARTS)

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
            cv.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
            cv.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

    try:
        if points[6][1] >= points[8][1]:
            cv.imwrite("./falldown/always.png",frame)
            if (os.path.isfile("./falldown/check.png")==False): cv.imwrite("./falldown/check.png",frame)
            img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = cv.resize(img, (200, 200))
            img = (img / 255.0).reshape((-1, 200, 200, 3))
            percentage = model.predict(img)
            disease_number = percentage.argmax()
            # ab = model.predict('img')
            print(disease_number)
            cv.putText(frame, 'Fall-Detection!', (20, 60),cv.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 255), 2)
            
            if disease_number == 0:
                os.rename("./falldown/check.png","./falldown/final.png")
                headers = {
                "Authorization": "Bearer " + 'dGVduK61GB5tTMub9zwBJl7EbDzE52Zs1hRxsKKSEhB', "Content-Type": "application/x-www-form-urlencoded"}
                params = {"message" : "有危險發生，請前往支援"}
                # 傳LINE
                r = requests.post("https://notify-api.line.me/api/notify",
                    headers=headers, params=params)
                print(json.dumps(params))
                break
            else:
                pass

    except TypeError:
        pass

    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000
    cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))


    cv.imshow('OpenPose using OpenCV', frame)

