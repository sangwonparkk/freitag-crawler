import json
import requests
import schedule
import time
import threading

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type": "refresh_token",
    "client_id": "bf46c47a18a2e1e0679ee3a14fe49ab3",
    "refresh_token": "t9XTb0Bez9OxQvDSZKTlkaEFiixmDoEX2p1WRQo9cusAAAF6ucJgfA"
}


def job():
    r = requests.post(url, data=data)
    print("Refreshed")
    threading.Timer(19800, job).start()
    return r


response = job()
tokens = response.json()

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)
