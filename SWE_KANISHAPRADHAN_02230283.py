
import requests
import schedule
import time

TOKEN = "6242971737:AAHSls4sFyFQnDzVCL4PnyannXG8iLK5PCQ"
chat_id = "-1001808680228"
message = "good moring!!!Have a great day.Remenber,everything is fated."
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message


def job():
    requests.get(url)
    schedule.every().day.at("19:47").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

