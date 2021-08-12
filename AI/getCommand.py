import os
import sys
import json
sys.stdout.reconfigure(encoding = 'utf-8')

args=[]
for i in sys.argv[1:]:
    args.append(i)

args = ','.join(args)

f = open("./prepation/command.txt","w",encoding="utf-8")
f.write(args)
f.close()
level =""
while( level == ""):
    with open ("./prepation/level.json","r+",encoding='utf-8') as f:
        level =json.load(f)
        if (level != "" ):
            print(json.dumps(level))
            f.close()
            with open("./prepation/level.json","w+",encoding='utf-8') as f:
                f.close()