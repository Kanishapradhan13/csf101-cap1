from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Bot
import asyncio
import requests

API_Key = "794630d84c221c1612f48c2ea7d21159"
bot_token = "6242971737:AAHSls4sFyFQnDzVCL4PnyannXG8iLK5PCQ"
chat_id = "-1001808680228"
city_name = "Thimphu"

async def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}"

    response = requests.get(url)
    res = response.json()

    if res["cod"] != "404":
        data = res["main"]
        live_temperature_k = data["temp"]
        live_humidity = data["humidity"]
        desc = res["weather"]
        weather_description = desc[0]["description"]
        
        # Convert temperature to Celsius
        live_temperature_c = live_temperature_k - 273.15
        message = f"Weather forecast for {city_name}:\nTemperature: {live_temperature_c}\nHumidity: {live_humidity}\nDescription: {weather_description}"
        
        #check if its raining
        if "rain" in weather_description.lower():
            reminder_message = f"Don't forget to take an umbrella in {city_name}!"
            bot = Bot(token=bot_token)
            await bot.send_message(chat_id=chat_id, text=reminder_message)

        bot = Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=message)
    else:
        print("Please enter a valid city name")

scheduler = AsyncIOScheduler()
scheduler.add_job(get_weather, 'interval', days=1, start_date='2023-10-07 07:00:00')
scheduler.start()

# Keep the script running
asyncio.get_event_loop().run_forever()