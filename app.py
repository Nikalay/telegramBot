import requests

API_link = "https://api.telegram.org/bot1432585953:AAEwkOrcHOLCRcR-eTlPtAbm2tdnvFSSGeQ"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

message = updates['result'][0]['message']
chat_id = message['from']['id']
text = message['text']
send_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")