import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_crypto_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    query_params = {"symbol": "BTCUSDT"}
    try:
        response = requests.get(url, params=query_params)
        if response.status_code == 200:
            return float(response.json().get("price"))
    except Exception as e:
        print(f"Network Error: {e}")
    return None

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Failed to send notification to TG: {e}")

def run_tracker():
    ALERT_PRICE_THRESHOLD = 98000.0  
    
    print("🚀 The continuous monitoring script has been launched...")
    print("Trigger threshold: $", ALERT_PRICE_THRESHOLD)
    print("To stop the script, press Ctrl + C in the terminal.")
    print("-" * 40)
    
    while True:
        current_price = get_crypto_price()
        
        if current_price:
            local_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"[{local_time}] Current BTC rate: ${current_price:,.2f}")
            
            if current_price < ALERT_PRICE_THRESHOLD:
                alert_msg = f"⚠️ ALERT! BTC has fallen below the threshold! Price: ${current_price:,.2f}"
                send_telegram_alert(alert_msg)
                print("🚨 Message sent to Telegram!")
                
        time.sleep(10)

if __name__ == "__main__":
    try:
        run_tracker()
    except KeyboardInterrupt:
        print("\n🛑 Monitoring has been successfully stopped by the user.")