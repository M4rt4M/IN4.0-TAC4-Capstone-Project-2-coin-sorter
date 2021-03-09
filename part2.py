############################
# ******** PART 2 ******** #
############################

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

#Possible input for GBP
#Dropped generating the input automatically depending on currency
two = ["£2", "£2.0", "£ 2", "2", "2.0", "2.00", "2 pounds", "2pounds", "2GBP", "2.00GBP", "2 GBP", "2gbp", "2.00gbp", "2 gbp", "two", "two pounds", "two GBP", "two gbp"]
one = ["£1", "£1.0", "£ 1", "1", "1.0", "1.00", "1 pound", "1pound", "1GBP", "1.00GBP", "1 GBP", "1gbp", "1.00gbp", "1 gbp", "one", "one pound", "one GBP", "one gbp"]
fifty = ["50p", "£0.5", "£ 0.5", "£ 0.50", "0.50", "0.5", "50 pence", "50pence", "0.5GBP", "0.50GBP", "0.50 GBP", "0.5gbp", "0.50gbp", "0.50 gbp", "fifty", "fifty pence"]
twenty = ["20p", "£0.2", "£ 0.2", "£ 0.20", "0.20", "0.2", "20 pence", "20pence", "0.2GBP", "0.20GBP", "0.20 GBP", "0.2gbp", "0.20gbp", "0.20 gbp", "twenty", "twenty pence"]
ten = ["10p", "£0.1", "£ 0.10", "£ 0.1", "0.10", "0.1", "10 pence", "10pence", "0.1GBP", "0.10GBP", "0.10 GBP", "0.1gbp", "0.10gbp", "0.10 gbp", "ten", "ten pence"]

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
        if choice in two:
          choice = coins[0]
        if choice in one:
          choice = coins[1]
        if choice in fifty:
          choice = coins[2]
        if choice in twenty:
          choice = coins[3]
        if choice in ten:
          choice = coins[4]
        if choice in coins: #This code will only run if user inputs one of pre-defined values
          print(str(p//values[coins.index(choice)]) + " " + choice + " coin(s)")
          print(str(p%values[coins.index(choice)]) + " pennies remaining")
          break #Ends the while loop after 1 calculation
        else: #This code will run if the value given by user is NOT in pre-defined list
          print("Sorry, you cannot choose this value. Try writing in one of the following formats: £2.00, 1GBP, 50p, £0.2, 0.1GBP")
      break
    else:
      print("Sorry, this value is out of range.")
      
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
        if skip in two:
          skip = coins[0]
        if skip in one:
          skip = coins[1]
        if skip in fifty:
          skip = coins[2]
        if skip in twenty:
          skip = coins[3]
        if skip in ten:
          skip = coins[4]
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
      
def available_coins()
  print ("\nHere are the available coins: ")
  for i in range(len(coins)):
    print(coins[i])
    
def display_program_config():
  print (31 * '-')
  print("Program configuration")
  print (31 * '-')
  print("The currency is set to GBP.")
  print("The minimum coin input value is set to ", p_min)
  print("The maximum coin input value is set to", p_max)

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
  Entry = int(input('\nEnter an option between 1-6:'))
  if Entry == 1:
    ####Here the code for coin sorter goes
    single_coin()
    ####End of coin sorter    
  elif Entry == 2:
    ####Here the code for coin sorter goes
    multiple_coins()
    ####End of coin sorter 
  elif Entry == 3:
     available_coins()
  elif Entry == 4:
    #This is the sub-menu
    while True:
      try:
        submenu()
        option = int(input("Enter your option: "))
        if option == 1:
          while True:
            curr = input("Type the currency code (GBP, USD or EUR): ")
            curr = curr.upper()
            if curr in currency_dict:
              currency = curr
              print(currency, " currency is set.")
              ## The code on 4 lines below would overwrite default coin list with a list made with newly set currency
              #coins = []
              #for i in range(len(values)):
              #  temp = currency_dict[currency] + str(values[i]/100) + str(0)
              #  coins.append(temp)
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
              print("Invalid option. Try again.")
      except ValueError:
        print("This needs to be whole number. Try again.")
  #This is where sub menu ends, and main menu is shown again
  elif Entry == 5:
    display_program_config()
  elif Entry == 6:
    print("Goodbye")
    break
  else:    ## default ##
    print ("Invalid number. Try again...")
