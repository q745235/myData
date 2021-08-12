import pandas as pd
import mysql.connector # pip install mysql-connector-python

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hos"
        )
mycursor = mydb.cursor()
sql = 'insert into disease values (%s, %s, %s, %s, %s)' # 每台電腦都不一樣

with open('disease.txt', "r") as txtfile:
    for line in txtfile:  
        line = line.strip('\n')
        line = line.split('\t')
        if line[0] == "name":
            pass
        else:
            val = (line[0], line[1], line[2], line[3], line[4])
            mycursor.execute(sql, val)
            mydb.commit()
    mydb.close()
        