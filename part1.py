# Define variables
values = [200, 100, 50, 20, 10]
coins = ["£2", "£1", "50p", "20p", "10p"]
p_min = 0
p_max = 10000

###############################
# 1 - Single coin calculator  #
###############################

### Calculates coins of one chosen denomination; user forced to choose one 

# Create functions
def single_coin(p, choice):
  if p<=p_min and p>=p_max:
    print("Sorry, this value is out of range.")
  else:
    print(str(p//values[coins.index(choice)]) + " " + choice + " coin(s)")
    print(str(p%values[coins.index(choice)]) + " pennies remaining")

# Ask user for input
p=int(input("Please enter an amount of pennies between 0-10000:"))
print("Here are available denominations: £2, £1, 50p, 20p, 10p")
choice = "nothing"

# Run
while choice: #This while loop will run for as long as string <choice> is not empty
  choice=str(input("Please enter one denomination of choice: "))
  if choice in coins: #This code will only run if user inputs one of pre-defined values
    single_coin(p, choice)
    break #Ends the while loop after 1 calculation
  else: #This code will run if the value given by user is NOT in pre-defined list
    print("Sorry, you cannot choose this value.")

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
for i in range(len(coins)):
  print(coins[i])

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
