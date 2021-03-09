##Before you run the program, type the following two commands in Shell
##In Shell: pip install --upgrade pip
##In Shell: pip install dearpygui

from dearpygui.core import *
from dearpygui.simple import *

text = "2GBP"

# Define functions
def log_data1(sender, data):
  log_info(get_value("source1"))

def log_data2(sender, data):
  log_info(get_value("source2"))

def single_coin_window(sender, data):
    add_window("Single coin calculator")
    add_text("Please enter the number of between 1-10000:")
    add_input_int("input1", label="##pennies", source="source1")
    add_text("Or use slider below")
    add_slider_int("input1#slider", label="##slide", default_value=0, max_value=10000, source="source1")
    add_button("Compute##1", callback=log_data1)
    
    add_input_text("choosen coin", label = text, readonly=True, default_value="0")

    end()

def multiple_coin_window(sender, data):
    add_window("Multiple coin calculator")
    add_text("Please enter the number of between 1-10000:")
    add_input_int("input2", label="##pennies", source="source2")
    add_text("Or use slider below")
    add_slider_int("input2#slider", label="##slide", default_value=0, max_value=10000, source="source2")
    add_button("Compute##2", callback=log_data2)
    add_text("Here is where the code would do its thing")
    add_input_text("2GBP##inputtext", readonly=True, default_value="0")
    add_input_text("1GBP##inputtext", readonly=True, default_value="0")
    add_input_text("0.50GBP##inputtext", readonly=True, default_value="0")
    add_input_text("0.20GBP##inputtext", readonly=True, default_value="0")
    add_input_text("0.10GBP##inputtext", readonly=True, default_value="0")
    end()

#set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30,30)

#Design main menu
with window("Main menu", width=400, height=500):
    add_image("Image", "Penguins.jpg")
    add_text("Welcome to the coin calculator")
    add_spacing(count=5, name="spacing1")
    add_button("Button1", label="Single coin calc", callback=single_coin_window)
    add_button("Button2", label="Multiple coin calc", callback=multiple_coin_window)
    add_button("Button3", label="Display coin list")
    add_button("Button4", label="Set details")
    add_button("Button5", label="Display program configurations")
    add_spacing(count=5, name="spacing1")
    


show_logger()
show_documentation()
setup_dearpygui()
while True:
    # do other stuff
    render_dearpygui_frame()
cleanup_dearpygui()
