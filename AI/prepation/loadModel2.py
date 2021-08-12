from re import T, split
import tensorflow as tf
from ckiptagger import WS
import numpy as np
import re
import pandas as pd
from tensorflow.keras import backend as K
import sys
import json
import time

gpus=tf.config.experimental.list_physical_devices(device_type="GPU") 
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu,True)
    
# gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
# sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

ws = WS("../dataCheck/data/")
print("模型載入完畢")
def CommentCheck(commdata):
    print("start")
    data=[]
    data.append(commdata)
    # data = commdata
    # data = [['明星皮膚科診所', 
    #         "醫生還蠻厲害的，朋友的過敏有改善",
    #         "這間醫院醫生好厲害", "這間護士很狠", "醫師看病有耐心，對待患者很親切且熱絡。"],
    #         ['哈哈皮膚科診所', 
    #         "醫生還蠻厲害的，朋友的過敏有改善",
    #         "這間醫院醫生好厲害", "這間護士很狠", "醫師看病有耐心，對待患者很親切且熱絡。"]]
    
    # 獲取分析來源  
    
    print('[字元分解開始]')
    fTotal = []
    for TotalComm in data[0:5]:
        # hosName.append(TotalComm[0])
        TotalComm=TotalComm[:]
        for i in TotalComm:
            fKey = re.sub(
                "[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）～]+", "", i)
            fKey = ws([fKey])
            fTotal.append(fKey[0])
            xdata = i[0:9]
            xdata = xdata.ljust(10, "．")
            xtemp = str(fTotal.index((fKey[0]))+1)
            xtotal = str(len(TotalComm))
            print(f'[{xdata}] 分解完畢...... [ {xtemp.zfill(3)} / {xtotal.zfill(3)}]')
            print('[字元分解結束]')

        # 獲取分析來源
        dictionary = {}
        df = pd.read_csv("../dataCheck/encoding.csv", encoding="utf-8")
        df = df.iloc[:]  # 選取欲讀取資料筆數
        # print(df)
        dictionary = df.set_index('commit').T.to_dict('list')

        # 重新編譯分割後字串
        print('[字元編碼開始]')
        fileTrainSeg = []  # 編譯後資料及其原始評分
        # fileTrainSeg = np.empty(shape=(0,100))
        for text in fTotal:
            fKey = []
            for x in text:
                try:
                    fKey.append(dictionary[x][0])
                except KeyError:
                    print(f'字典尚無"{x}"')
                    pass
            fileTrainSeg.append(fKey)
        print('[字元編碼結束]')

        data = tf.keras.preprocessing.sequence.pad_sequences(fileTrainSeg, maxlen=100)

        # 載入訓練好模型
        reload_model = tf.keras.models.load_model('../dataCheck/saved_model/my_model')
        # reload_model.summary()
        fLevel = reload_model.predict(data)
        myCore=0
        for i in fLevel:
            myCore += i.argmax() 
        myCore = round(myCore/len(fLevel),1)
        dicTemp={
            # "name":hosName[0],
            "level":myCore
        }
        # dicTemp[hosName[0]]=myCore
        finalAnswer=json.dumps(dicTemp,ensure_ascii=False)
        # print(f'{hosName[0]}:{myCore}')
        print(finalAnswer) 
        return finalAnswer


# dicTemp={}
command =""
while(command ==""):
    
    f =open("command.txt","r+",encoding="utf-8")
    command = f.read()
    # print(uri)
    f.write("")
    f.close()
    f =open("command.txt","w+",encoding="utf-8")
    f.close()
    if (command !=""):
        #重新建立為需求陣列
        command=command.split(',')
        level =CommentCheck(command)
        print("資料讀寫完畢......")
        command =""
        with open('level.json', 'w', encoding='utf-8') as f:
            f.write(level)
            f.close()
            print(level)
            
            # break
    print("等待資料中.....")
    time.sleep(2)
# CommentCheck(123)
# print(CommentCheck())