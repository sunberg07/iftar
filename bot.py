import requests
import time

print("BOT BAŞLADI")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

send_message("Bot Railway'de aktif 🟢")

while True:
    time.sleep(60)
