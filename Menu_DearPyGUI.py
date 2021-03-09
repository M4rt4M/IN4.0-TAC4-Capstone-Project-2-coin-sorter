##Before you run the program, type the following two commands in Shell
##In Shell: pip install --upgrade pip
##In Shell: pip install dearpygui

from dearpygui.core import *
from dearpygui.simple import *

values = [200, 100, 50, 20, 10]
currency_dict = {  #This is a list of available currencies. Added currencies must be decimal, i.e. 1USD = 100 cents. Add new currencies after a comma, in the following format: "currency_code" : "currency_symbol"
  "GBP": "£", 
  "USD": "$",
  "EUR": "€"
  }

currency = "GBP" #This must be one of the currency codes in the currency_dict above  
p_min = 0
p_max = 10000

#This takes the default currency and makes the list of available coins according to their values
coins = []
for i in range(len(values)):
  temp = currency_dict[currency] + str(values[i]/100) + str(0)
  coins.append(temp)
  
choosen_coin = coins[1]

# Define functions
def log_data1(sender, data):
  log_info(get_value("source1")) #log in the number 

def log_data2(sender, data):
  log_info(get_value("source2"))

def settings(sender, data):
  currency = get_value("currency")
  log_info(get_value("currency")) #logs in the currency code from the list
  p_min = get_value("source4")
  p_max = get_value("source4")

def single_coin_window(sender, data):
    add_window("Single coin calculator")
    add_text("Please enter the number of between 1-10000:")
    add_input_int("input1", label="##pennies", source="source1")
    add_text("Or use slider below")
    add_slider_int("input1#slider", label="##slide", default_value=p_min, max_value=p_max, source="source1")
    add_button("Compute##1", callback=log_data1)
    
    add_input_text("choosen coin", label = choosen_coin, readonly=True, default_value="0")

def multiple_coin_window(sender, data):
    add_window("Multiple coin calculator")
    add_text("Please enter the number of between 1-10000:")
    add_input_int("input2", label="##pennies", source="source2")
    add_text("Or use slider below")
    add_slider_int("input2#slider", label="##slide", default_value=p_min, max_value=p_max, source="source2")
    add_button("Compute##2", callback=log_data2)
    add_text("Here is where the code would do its thing")
    add_input_text("inputtext1", label = coins[0], readonly=True, default_value="0")
    add_input_text("inputtext2", label = coins[1], readonly=True, default_value="0")
    add_input_text("inputtext3", label = coins[2], readonly=True, default_value="0")
    add_input_text("inputtext4", label = coins[3], readonly=True, default_value="0")
    add_input_text("inputtext5", label = coins[4], readonly=True, default_value="0")
    
def settings_window(sender, data):
    add_window("Settings")
    add_text("Choose the currency")
    add_listbox("##demolistbox1", items=["GBP", "USD", "EUR"], default_value=0, width=100, source="currency")
    add_text("Choose minimum number of pennies to exchange")
    add_input_int("input3", label="##pennies_min", source="source4", default_value=p_min)
    add_text("Choose maximum number of pennies to exchange")
    add_input_int("input4", label="##pennies_max", source="source5", default_value=p_max)
    add_button("Save", callback=settings)

#set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30,30)

#Design main menu
with window("Main menu", width=500, height=500):
    add_image("Image", "coins.jpg")
    add_text("Welcome to the coin calculator")
    add_spacing(count=5, name="spacing1")
    add_button("Button1", label="Single coin calculator", callback=single_coin_window)
    add_button("Button2", label="Multiple coin calculator", callback=multiple_coin_window)
    add_button("Button4", label="Set details", callback=settings_window)
    add_spacing(count=5, name="spacing2")
    add_collapsing_header("Display coin list")
    add_text(coins[0])
    add_text(coins[1])
    add_text(coins[2])
    add_text(coins[3])
    add_text(coins[4])
    end()
    add_collapsing_header("Display setings")
    add_text("Currency is set to "+ currency)
    add_text("Minimum number of coins to exchange is "+ str(p_min))
    add_text("Maximum number of coins to exchange is "+ str(p_max))
    end()
    
#show_logger()
#show_documentation()
setup_dearpygui()
while True:
    # do other stuff
    render_dearpygui_frame()
cleanup_dearpygui()
