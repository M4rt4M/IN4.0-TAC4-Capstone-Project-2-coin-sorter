# Define variables
values = [200, 100, 50, 20, 10]
coins = ["£2", "£1", "50p", "20p", "10p"]

###############################
# 1 - Single coin calculator  #
###############################

### Calculates coins of one chosen denomination; user forced to choose one 

# Create functions
def single_coin(p, choice):
  if p<=0 and p>=10000:
    print("Sorry, this value is out of range.")
  else:
    print(str(p//values[coins.index(choice)]) + " " + choice + " coin(s)")
    print(str(p%values[coins.index(choice)]) + " pennies remaining")

# Ask user for input
p=int(input("Please enter an amount of pennies between 0-10000:"))
print("Here are available denominations: £2, £1, 50p, 20p, 10p")
choice = "nothing"

# Run
while choice:
  choice=str(input("Please enter one denomination of choice: "))
  if choice in coins:
    single_coin(p, choice)
    break
  else:
    print("Sorry, you cannot choose this value.")

#################################
# 2 - Multiple coin calculator  #
#################################

### Skips a coin of choice; uses all coins if nothing is skipped or wrong value given

# Create functions
def multiple_coins(p):
  if p<=0 and p>=10000:
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
if skip:
  if skip in coins:
    values.remove(values[coins.index(skip)])
    coins.remove(skip)
  else:
    print("\nSorry, you cannot skip this value")

# Run calculator
multiple_coins(p)

########################
# 3 - Print coin list  #
########################

### What it does



####################
# 4 - Set details  #
####################

### What it does

# Create functions

# Ask user for input

# Run

####################
# 5 -   #
####################

### What it does

# Create functions

# Ask user for input

# Run

####################
# 6 -   #
####################

### What it does

# Create functions

# Ask user for input

# Run
