import os 
import sys
import json
from time import sleep
from w3lib.url import parse_data_uri

sys.stdout.reconfigure(encoding = 'utf-8')
output = {}
uri = sys.argv[1] # 0是python檔名 1是檔案
# uri = "data:image/jpeg;base64,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…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"


#寫入拍攝圖片資訊
f = open("./prepation/uri.txt","w",encoding="utf-8")
f.write(uri)
f.close()

# 多這行
with open("./prepation/sickans.json", "w") as filename:
    json.dump({"name": "999"}, filename)
     

#嘗試讀取檔案
n = 1
while( n):
    with open ("./prepation/sickans.json","r",encoding='utf-8') as f:
        ans =json.load(f)
        if (ans['name'] != '999'):
            ans=json.dumps(ans)
            print(ans)
            # os.remove("./prepation/sickans.json")
            n = 0
            break

        
            # f.seek(0)
            # f.truncate()
            # json.dump({"name":"999"},f)
    # with open ("./prepation/sickans.json","w",encoding='utf-8') as f1:
    #     f1.seek(0)
    #     f1.truncate()
    #     json.dump({"name":"999"},f1)

    

