import pandas as pd
import requests
import mysql.connector
import sys
import json
# args=sys.argv[1]
args='皮膚'
sys.stdout.reconfigure(encoding='utf-8')
def place_detal(dd):
    mydb = mysql.connector.connect(
        # host="localhost",
        host="localhost",
        user="root",
        passwd="",
        database="hos"
        )

    mycursor = mydb.cursor()
    sql = 'SELECT DISTINCT name, address FROM hos WHERE name LIKE "%'+ dd + '%"'
    # sql = 'SELECT DISTINCT name, address FROM hos WHERE name LIKE "%皮膚%"'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()     # fetchall() 获取所有记录
    # print(myresult)
    da = []
    for x in myresult:
        dt = { "name": x[0], "address": x[1]}
        da.append(dt)
        # print(x[0], x[1])
    jsonOutput = json.dumps(da, ensure_ascii=False)
    print(jsonOutput)
    db = []
    for i in da[:30]:
        mycomm=[]
        sql = 'SELECT  comment FROM hos WHERE name LIKE "%'+ i['name'] + '%"'
        mycursor.execute(sql)
        myresult = mycursor.fetchall()     # fetchall() 获取所有记录




        mycomm.append(i['name'])
        # print(i['name'])
        for comment in myresult:
            mycomm.append(comment[0])
        # db.append(mycomm)

        mycomm={"name":mycomm[0],"data":mycomm[1:-1]}
        db.append(mycomm)
        # jsonOutput = json.dumps(mycomm, ensure_ascii=False)
        # print(jsonOutput)
    jsonOutput = json.dumps(db, ensure_ascii=False)
    print(jsonOutput)
    mydb.close()
    sys.stdout.flush()
place_detal(args)