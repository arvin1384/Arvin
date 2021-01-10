import requests 
import time
bitcoin_api = "https://api.coindesk.com/v1/bpi/currentprice.json"
while True :
    data_ = requests.get(bitcoin_api)
    data = eval(data_.text)
    print(data['bpi']['USD']['rate'])
    time.sleep(60)

