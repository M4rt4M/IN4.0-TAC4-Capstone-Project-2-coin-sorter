# Define variables
values = [200, 100, 50, 20, 10]
currency_dict = {
  "GBP": "£", 
  "USD": "$"
  }
#These will be displayed in settings 
currency = "GBP" #so that it can be updated
p_min = 0
p_max = 10000

#This takes the currency and makes the list of available coins
coins = []
for i in range(len(values)):
  temp = currency_dict[currency] + str(values[i]/100) + str(0)
  coins.append(temp)
print(str(coins))

#Possible input for GBP
two = ["£2", "£2.0", "£ 2", "2", "2.0", "2.00", "2 pounds", "2pounds", "2GBP", "2.00GBP", "2 GBP", "2gbp", "2.00gbp", "2 gbp", "two", "two pounds", "two GBP", "two gbp"]
one = ["£1", "£1.0", "£ 1", "1", "1.0", "1.00", "1 pound", "1pound", "1GBP", "1.00GBP", "1 GBP", "1gbp", "1.00gbp", "1 gbp", "one", "one pound", "one GBP", "one gbp"]
fifty = ["50p", "£0.5", "£ 0.5", "£ 0.50", "0.50", "0.5", "50 pence", "50pence", "0.5GBP", "0.50GBP", "0.50 GBP", "0.5gbp", "0.50gbp", "0.50 gbp", "fifty", "fifty pence"]
twenty = ["20p", "£0.2", "£ 0.2", "£ 0.20", "0.20", "0.2", "20 pence", "20pence", "0.2GBP", "0.20GBP", "0.20 GBP", "0.2gbp", "0.20gbp", "0.20 gbp", "twenty", "twenty pence"]
ten = ["10p", "£0.1", "£ 0.10", "£ 0.1", "0.10", "0.1", "10 pence", "10pence", "0.1GBP", "0.10GBP", "0.10 GBP", "0.1gbp", "0.10gbp", "0.10 gbp", "ten", "ten pence"]

###############################
# 1 - Single coin calculator  #
###############################

### Calculates coins of one chosen denomination; user forced to choose one 

def single_coin():
  while True:
    try:
      p=int(input("Please enter an amount of pennies between 0-10000:"))
    except ValueError:
      print("This needs to be a whole number. You have one more try.")
      try:
        p=int(input("Please enter an amount of pennies between 0-10000:"))
      except ValueError:
        print("This needs to be a whole number. Terminating calculator.")
        return
    if p>=p_min and p<=p_max:
      choice = "nothing"
      while choice: #This while loop will run for as long as string <choice> is not empty
        print("Here are available denominations: ")
        for i in range(len(coins)):
            print(coins[i])
      ####UPDATE for other calc!!!
        choice=str(input("Please enter one denomination of choice: "))
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
def multiple_coins(p):
  if p<=p_min and p>=p_max:
    print("\nSorry, this value is out of range.")
  else:
    for i in range(len(values)):
      print(str(p//values[i]) + " " + coins[i] + " coin(s)")
      p = p%values[i]
    print(str(p) + " pennies remaining")

# Ask user for input
p=int(input("\nPlease enter an amount of pennies between 0-10000: "))
print("Here are available denominations: £2, £1, 50p, 20p, 10p")
skip=str(input("\nPlease enter the value you would like to skip. If you don't choose anything, all coins will be displayed: "))
if skip: #This code will runonly if user inputs a value (any)
  if skip in coins: #This code will run only if the value given by user is in pre-defined list
    values.remove(values[coins.index(skip)])
    coins.remove(skip)
  else: #This code will run if the value given by user is NOT in pre-defined list
    print("\nSorry, you cannot skip this value")

# Run calculator
multiple_coins(p)

########################
# 3 - Print coin list  #
########################

### Prints available coins
print("Here are available coins:")

####################
# 4 - Set details  #
####################

### What it does

# Create functions

# Ask user for input

# Run

#######################################
# 5 - Display program configurations  #
#######################################

### Displays program configurations

####################
# 6 -   #
####################

### What it does

# Create functions

# Ask user for input

# Run
