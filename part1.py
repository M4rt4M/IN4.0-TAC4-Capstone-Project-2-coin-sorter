############################
# ******** PART 1 ******** #
############################
import requests

# Define variables
values = [200, 100, 50, 20, 10]
currency_dict = {  #This is a list of available currencies. Added currencies must be decimal, i.e. 1USD = 100 cents. Add new currencies after a comma, in the following format: "currency_code" : "currency_symbol"
  "GBP": "£", 
  "USD": "$",
  "EUR": "€"
  }

#These are default settings 
currency = "GBP" #This must be one of the currency codes in the currency_dict above  
p_min = 0
p_max = 10000

#This takes the default currency and makes the list of available coins according to their values
coins = []
for i in range(len(values)):
  temp = currency_dict[currency] + str(values[i]/100) + str(0)
  coins.append(temp)


#Possible input for GBP
###QUESTION: Can we generate these lists depending on the currency?
two = ["£2", "£2.0", "£ 2", "2", "2.0", "2.00", "2 pounds", "2pounds", "2GBP", "2.00GBP", "2 GBP", "2gbp", "2.00gbp", "2 gbp", "two", "two pounds", "two GBP", "two gbp"]
one = ["£1", "£1.0", "£ 1", "1", "1.0", "1.00", "1 pound", "1pound", "1GBP", "1.00GBP", "1 GBP", "1gbp", "1.00gbp", "1 gbp", "one", "one pound", "one GBP", "one gbp"]
fifty = ["50p", "£0.5", "£ 0.5", "£ 0.50", "0.50", "0.5", "50 pence", "50pence", "0.5GBP", "0.50GBP", "0.50 GBP", "0.5gbp", "0.50gbp", "0.50 gbp", "fifty", "fifty pence"]
twenty = ["20p", "£0.2", "£ 0.2", "£ 0.20", "0.20", "0.2", "20 pence", "20pence", "0.2GBP", "0.20GBP", "0.20 GBP", "0.2gbp", "0.20gbp", "0.20 gbp", "twenty", "twenty pence"]
ten = ["10p", "£0.1", "£ 0.10", "£ 0.1", "0.10", "0.1", "10 pence", "10pence", "0.1GBP", "0.10GBP", "0.10 GBP", "0.1gbp", "0.10gbp", "0.10 gbp", "ten", "ten pence"]

###QUESTION: Can we generate these lists depending on the currency?
###ANSWER: Yes, but cannot implement it in the same way :(
d = {}
def input_generator(currency, values):
  for i in range(len(values)):
    temp = []
    temp.append(currency_dict[currency] + str(values[i]/100) + str(0))
    temp.append(currency_dict[currency] + str(values[i]/100))
    temp.append(currency_dict[currency] + " " + str(values[i]/100))
    temp.append(str(values[i]/100) + currency)
    temp.append(str(values[i]/100) + " " + currency)
    temp.append(str(values[i]/100) + currency.lower())
    temp.append(str(values[i]/100) + " " + currency.lower())
    temp.append(str(values[i]/100) + "0" + currency)
    temp.append(str(values[i]/100) + "0 " + currency)
    temp.append(str(values[i]/100) + "0" + currency.lower())
    temp.append(str(values[i]/100) + "0 " + currency.lower())
    temp.append(str(values[i]/100))
    temp.append(str(values[i]/100) + "0")
    if values[i] >= 100:
      temp.append(str(int(values[i]/100)))
      temp.append(currency_dict[currency] + str(int(values[i]/100)))
      temp.append(currency_dict[currency] + " " + str(int(values[i]/100)))
      temp.append(str(int(values[i]/100)) + currency)
      temp.append(str(int(values[i]/100)) + " " + currency)
    d["value{0}".format(i)] = temp

input_generator(currency, values)

###############################
# 1 - Single coin calculator  #
###############################

### Calculates coins of one chosen denomination; user forced to choose one 

def single_coin():
  while True:
    try:
      p=int(input("\nPlease enter an amount of pennies between 0-10000:"))
    except ValueError:
      print("This needs to be a whole number. Try again")
      single_coin() #This is a recursive function. It will be triggered again and again, unless the user inputs the accepted number of pennies
      return
    if p>=p_min and p<=p_max:
      choice = "nothing"
      while choice: #This while loop will run for as long as string <choice> is not empty
        print("\nHere are available denominations: ")
        for i in range(len(coins)):
            print(coins[i])
        choice=str(input("\nPlease enter one denomination of choice: "))
        if currency == "GBP":  
          if choice in two:
            choice = "£2.00"
          if choice in one:
            choice = "£1.00"
          if choice in fifty:
            choice = "£0.50"
          if choice in twenty:
            choice = "£0.20"
          if choice in ten:
            choice = "£0.10"
        if choice in coins: #This code will only run if user inputs one of pre-defined values
          print(str(p//values[coins.index(choice)]) + " " + choice + " coin(s)")
          print(str(p%values[coins.index(choice)]) + " pennies remaining")
          break #Ends the while loop after 1 calculation
        else: #This code will run if the value given by user is NOT in pre-defined list
          print("Sorry, you cannot choose this value. Try writing in one of the following formats: £2.00, 1GBP, 50p, £0.2, 0.1GBP")
      break
    else:
      print("Sorry, this value is out of range.")

# Run
single_coin()

#################################
# 2 - Multiple coin calculator  #
#################################

### Skips a coin of choice; uses all coins if nothing is skipped or wrong value given

# Create functions
def multiple_coins():
  while True:
    try:
      p=int(input("\nPlease enter an amount of pennies between 0-10000:"))
    except ValueError:
      print("This needs to be a whole number. Try again")
      multiple_coins()
      return
    if p>=p_min and p<=p_max:
      print("\nHere are available denominations: ")
      for i in range(len(coins)):
        print(coins[i])
      skip=str(input("\nPlease enter the value you would like to skip. If you don't choose anything, all coins will be displayed: "))
      if skip:
        if currency == "GBP":  
          if skip in two:
            skip = "£2.00"
          if skip in one:
            skip = "£1.00"
          if skip in fifty:
            skip = "£0.50"
          if skip in twenty:
            skip = "£0.20"
          if skip in ten:
            skip = "£0.10"
        if skip in coins: 
          values.remove(values[coins.index(skip)])
          coins.remove(skip)
        else:
          print("\nSorry, you cannot skip this value")
      else:
        print("\nDisplaying all available coins")    
      for i in range(len(values)):
        print(str(p//values[i]) + " " + coins[i] + " coin(s)")
        p = p%values[i]
      print(str(p) + " pennies remaining")
      break
    else:
      print("\nSorry, this value is out of range.")

# Run calculator
multiple_coins()

########################
# 3 - Print coin list  #
########################

### Prints available coins
print ("\nHere are the available coins: ")
for i in range(len(coins)):
  print(coins[i])

####################
# 4 - Set details  #
####################

### Allows you to set details such as currency, adjust max and mimimum input of coins.
def submenu():
    print(31 * '-')
    print("***Set Details - Submenu***")
    print(31 * '-')
    print("1. Set currency")
    print("2. Set minimum coin input value (Default minimum = 0)")
    print("3. Set maximum coin input value (Default minimum = 10000)")
    print("4. Return to Main Menu")
    print(31 * '-')
    
def set_details():
  #This is the sub-menu
    while True:
      try:
        submenu()
        option = int(input("Enter your option: "))
        if option == 1:
          while True:
            curr = input("Type the currency code (GBP, USD or EUR: ")
            curr = curr.upper()
            if curr in currency_dict:
              currency = curr
              print(currency, " currency is set.")
              break
            else:
              print("Sorry, you cannot select this currency. Try again!")
          
        elif option == 2:
          p_min= int(input("Enter an amount between 0 to 10000 to set the minimum value: "))
          print("The minimum value is set to ", p_min)

        elif option == 3:
          p_max= int(input("Enter an amount between 0 to 10000 to set the maximum value: "))
          while True:
            if p_max <= p_min:
              print("The maximum value must be higher than the minimum value " + str(p_min) + ". Try again.")
              p_max= int(input("Enter an amount between 0 to 10000 to set the maximum value: "))
            else:
              break
          print("The maximum value is set to ", p_max)
          
        elif option == 4:
          break
        else:
              print("invalid option. Try again.")
      except ValueError:
        print("This needs to be whole number. Try again.")


set_details()


#######################################
# 5 - Display program configurations  #
#######################################

### Displays program configurations
def display_program_config():
  print (31 * '-')
  print("Program configuration")
  print (31 * '-')
  print("The currency is set to GBP.")
  print("The minimum coin input value is set to ", p_min)
  print("The maximum coin input value is set to", p_max)

#Run
display_program_config()

############################
# 6 - Currency conversion  #
############################
api_key = 'B1CRPD0B1HSR22CV'
#The amount variable will be the user's input of the amount needed to be converted
print("\nThis is the currency converter. Please enter the amount of money you would like to exchange.")Amount = float(input("Amount: ")) 
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
else:
    print(format(Answer, ".2f") + to_c)

