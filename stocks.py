import requests
import pprint as pp
import time

currency_endpoint = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_DKK&compact=y"
usd_to_dkk = requests.get(currency_endpoint).json()["USD_DKK"]["val"]
print("exchange rate: {}".format(usd_to_dkk))

stocks = {"NVDA":{"amount":9, "initial_price":156.5}}
api_key = "7Y0MMM6DVO9P1O19"

while True:
	for i in stocks.keys():
		endpoint = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}".format(i,api_key)
		r = requests.get(endpoint).json()["Time Series (Daily)"]
		date = list(r.keys())[0]
		# print(r[date])

		closing_price = float(r[date]["4. close"])
		start_kapital = stocks[i]["amount"] * stocks[i]["initial_price"] * usd_to_dkk
		current_kapital = stocks[i]["amount"] * closing_price * usd_to_dkk

		print("{} = {} USD, {} DKK".format(i,closing_price, closing_price*usd_to_dkk))
		print("DKK = {} kr, gain = {}%".format(round(current_kapital), round((current_kapital - start_kapital) / start_kapital * 100,2) ))
		print()
	time.sleep(60)	
