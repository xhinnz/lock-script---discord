import requests
import json
import time

f = open('config.json')
token = json.load(f)['token']

payload = {'content':'PEGA NOIS KKJ'}
headers = {'Authorization':token,'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.12 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'}

print("First blood do biel4 fofo?")

channelId = input() # ID depois do "@me/"


for _ in range(999999999): # biel4
    r = requests.post(f'https://discord.com/api/v8/channels/{channelId}/messages', headers=headers, json=payload)
    if r.status_code == 200:
        print('kill | kill him')
    elif r.status_code == 429:
        data = json.loads(r.text)
        print(f'Morto | Ilimitado, perai esses {data["retry_after"]} segundos')
        time.sleep(data['retry_after'])
    else:
        print(f'Erro do Biel4 | {r.status_code} | {r.text}')
