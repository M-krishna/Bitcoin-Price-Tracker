import requests
import schedule
import time
from datetime import datetime


def track_bitcoin_price():
    coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice/inr.json"
    response = requests.get(coindesk_api)
    response_json = response.json()
    print("""############################################""")
    print("Name: Bitcoin\n")
    print(str(response_json['bpi']['USD']['description'])+ ": " + response_json['bpi']['USD']['rate'] + " $" )
    print("USD price in float: " + str(response_json['bpi']['USD']['rate_float']) + " $" + "\n")
    print(str(response_json['bpi']['INR']['description']) + ": " + response_json['bpi']['INR']['rate'] + " Rs")
    print("INR price in float: " + str(response_json['bpi']['INR']['rate_float']) + " Rs")
    print("""############################################""")
    print()
    print()
    print()


schedule.every(6).seconds.do(track_bitcoin_price)

while 1:
    schedule.run_pending()
    time.sleep(1)
    
    
