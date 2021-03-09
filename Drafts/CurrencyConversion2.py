# To import the
import requests

api_key = 'B1CRPD0B1HSR22CV'
#The amount variable will be the user's input of the amount needed to be converted
Amount = float(input("Amount: ")) 
# from_c is the currency from which the user is converting from
from_c = input("From (type the currency code in all caps. E.g. USD for $): ") 
# to_c is the currency to which the user is converting to
to_c = input("To (type the currency code in all caps. E.g. USD for $): ") 

# base_url variable store base url 
base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
# main_url variable store complete url 
main_url = base_url + '&from_currency=' + from_c + '&to_currency=' + to_c + '&apikey=' + api_key

# get method of requests module  
# return response object  
response = requests.get(main_url)
result = response.json()
#The 'key' variable key will store the 'Realtime currency Exchange Rate' contents
# Exrate variable will store the exchange rate which is inside the key
key = result['Realtime Currency Exchange Rate']
Exrate = key['5. Exchange Rate']

#The answer is the variable in which you get the converted amount you need
Answer = (float(Exrate)*Amount)

#The if statements print the answer with the appropriate currency symbol
if to_c == 'GBP':
    print("£",format(Answer, ".2f"))  
elif to_c == 'USD':
    print("$",format(Answer, ".2f"))
elif to_c == 'MGA':
    print("Ar",format(Answer, ".2f"))



    















  
