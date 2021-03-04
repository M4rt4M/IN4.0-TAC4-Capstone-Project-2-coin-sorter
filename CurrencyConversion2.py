import requests

api_key = 'B1CRPD0B1HSR22CV'

Amount = float(input("Amount: "))
from_c = input("From (type the currency code in all caps. E.g. USD for $): ")
to_c = input("To (type the currency code in all caps. E.g. USD for $): ")

base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + from_c + '&to_currency=' + to_c + '&apikey=' + api_key

response = requests.get(main_url)
result = response.json()

key = result['Realtime Currency Exchange Rate']
Exrate = key['5. Exchange Rate']

Answer = (float(Exrate)*Amount)


if to_c == 'GBP':
    print("£",format(Answer, ".2f"))  
elif to_c == 'USD':
    print("$",format(Answer, ".2f"))
elif to_c == 'MGA':
    print("Ar",format(Answer, ".2f"))



    















  