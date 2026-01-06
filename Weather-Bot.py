import requests
from dotenv import load_dotenv
import os

load_dotenv()

my_token = os.getenv("TELEGRAM_BOT_TOKEN")
my_chat = os.getenv("TELEGRAM_CHAT_ID")
my_api = os.getenv("OPENWEATHER_API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"

city = input("enter your city:")
new_city = city.title()

params ={
    "q": new_city,     
    "appid": my_api,   
    "units": "metric"  
}

headers = headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url , params=params,headers=headers)

    if response.status_code == 200:
        request = response.json()
        data = request
        temp = data["main"]["temp"]

        weather_desc = data["weather"][0]["description"]
        weather_main = data["weather"][0]["main"]
    
        print(f"Temp: {temp}°C")
        print(f"Condition: {weather_desc}")

        if "rain" in weather_desc.lower() or "rain" in weather_main.lower():
            print("Chhata Lelo!")
            msg = f"Umbrella Alert!\nCity: {new_city}\nTemp: {temp}°C\nCondition: {weather_desc}\nChhata Lelo!"
            tele_url = f"https://api.telegram.org/bot{my_token}/sendMessage"
        
            requests.get(tele_url, params={"chat_id": my_chat, "text": msg})
            print("Telegram Sent!")
        else:
            print("Mausam Saaf Hai")

    elif response.status_code == 404:
        print(f"not found or check spelling : {new_city}")

    elif response.status_code == 429 :
        print("invalid api key")
    else:
        print(f"Something went wrong. Status: {response.status_code}")

except Exception as e :
    print(f" ERROR : {e}")

