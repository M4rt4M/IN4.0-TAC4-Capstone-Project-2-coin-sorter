#####################
# Define variables  #
#####################
values = [200, 100, 50, 20, 10]
coins = ["£2", "£1", "50p", "20p", "10p"]
p_min = 0
p_max = 10000

#####################
# Define functions  #
#####################



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
    print("Here is where user can try to set details")
    Entry2 = input("")
    if Entry2 == 0:
      print("Pressed 0")
    else:
      print("Something else")
    #This is where sub menu ends, and main menu is shown again
  elif Entry == 5:
    print("Display program configuration")
  else:    ## default ##
    print ("Invalid number. Try again...")