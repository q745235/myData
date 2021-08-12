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

model = keras.models.load_model('./model/modelvgg16')
img = load_image("./img/test1.jpg", 224, 224)
percentage = model.predict(img)
disease_number = percentage.argmax()
# print(disease_number)
print()

def select_disease(disease_number):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hos"
        )
    mycursor = mydb.cursor()
    sql = f'select * from disease where id = {disease_number}'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # da = []
    disease = [{
        "name" : myresult[0][0],
        "symptom" : myresult[0][3], 
        "urgency" : myresult[0][4]
    }]
    # da.append(disease)
        # print(dt)
    mydb.close()
    jsonOutput = json.dumps(disease, ensure_ascii = False)
    # sys.stdout.flush()
    # print(jsonOutput)
    return jsonOutput

print(select_disease(disease_number))
