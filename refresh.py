import json
import requests
import threading

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "refresh_token",
    "client_id"  : "bf46c47a18a2e1e0679ee3a14fe49ab3",
    "refresh_token" : "IvP-hk2Bdx3yk6h16cj43x_aUMEoaKvGpO0fmQo9dNkAAAF6r50f9w"
}
response = requests.post(url, data=data)

print(response.json())