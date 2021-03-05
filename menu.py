
#####################
# Define variables  #
#####################
values = [200, 100, 50, 20, 10]
currency_dict = {  
  "GBP": "£", 
  "USD": "$",
  "EUR": "€"
  }
#This is a list of available currencies. Added currencies must be decimal, i.e. 1USD = 100 cents. Add new currencies after a comma, in the following format: "currency_code" : "currency_symbol"

#These are default settings 
currency = "GBP" #This must be one of the currency codes in the currency_dict above  
p_min = 0
p_max = 10000

#This takes the default currency and makes the list of available coins according to their values
coins = []
for i in range(len(values)):
  temp = currency_dict[currency] + str(values[i]/100) + str(0)
  coins.append(temp)

#####################
# Define functions  #
#####################
def submenu():
          print(31 * '-')
          print("***Set Details - Submenu***")
          print(31 * '-')
          print("1. Set currency")
          print("2. Set minimum coin input value (Default minimum = 0)")
          print("3. Set maximum coin input value (Default minimum = 10000)")
          print("4. Return to Main Menu")
          print(31 * '-')

####################
# Responsive menu  #
####################

###User presses a 1-6 key to navigate

while True: 
  #This loop will run until break is triggered
  print (31 * '-')
  print ("*** Coin Sorter - Main Menu ***")
  print (31 * '-')
  print ("1. Coin calulator")
  print ("2. Multiple Coin Calculator")
  print ("3. Print Coin List")
  print ("4. Set Details")
  print ("5. Display Program Configurations")
  print ("6. Quit The Program")
  print (31 * '-')
  Entry = int(input('\nPlease enter an amount between 1-6:'))
  if Entry == 6:
    print("Goodbye")
    break
  elif Entry == 1:
    ####Here the code for coin sorter goes
    print("This is where the coin sorter would be")
    ####End of coin sorter    
  elif Entry == 2:
    ####Here the code for coin sorter goes
    print("Here is where the multiple coin calculator would go")
    ####End of coin sorter 
  elif Entry == 3:
     print ("Here are the available coins: ")
     for i in range(len(coins)):
        print(coins[i])
  elif Entry == 4:
    #This is the sub-menu
    while True:
      submenu()
      option = int(input("Enter your option: "))
      if option == 1:
        while True:
          curr = input("Type the currency code (e.g. 'gbp' or 'usd', in small caps): ")
          if curr == 'gbp':
            print("GBP currency is set.")
            break
          else:
            print("Sorry, you cannot select this currency. Try again!")
        
      elif option == 2:
        p_min= int(input("Enter an amount between 0 to 10000: "))
        print("The minimum value is set to ", p_min)
      elif option == 3:
        p_max= int(input("Enter an amount between 0 to 10000: "))
        print("The maximum value is set to ", p_max)
      elif option == 4:
            break
      else:
            print("invalid option. Try again.")
    #This is where sub menu ends, and main menu is shown again
  elif Entry == 5:
    print("Display program configuration")
  else:    ## default ##
    print ("Invalid number. Try again...")
