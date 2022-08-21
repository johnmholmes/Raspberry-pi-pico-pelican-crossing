# This code is for demonstration purposes only and is for shown how you could create a simple pelican crossing
# animation for your model railway layout.
#
# It is based on the Cytron Pi Pico maker board which has built in leds and switches which makes it a cheap
# development platform for your learning.
#
# I will use a total of 8 LEDs and 1 switch in the code which will simulate the two main banks of traffic lights
# and the 2 prodestrian warning lights

# We need to import 2 libaries for the program
# machine library gives us access to control the GP or input or outpins
#
# time gives a timer we can use within our code to cause delays

from machine import Pin
import utime

# Next we set up variables for the GP pins on the Pi Pico
# at this point we must tell the ide what the variable name is and then tell it which pin number we are goin to use.
# after the number we have a ( , ) and then we tell it is it anoutput or input. If its and input we can set a 3rd parameter
# Pull_UP or PULL_DOWN the pull up holds the pin at 3,3volts where as low holds it at 0volts

button = Pin(21, Pin.IN, Pin.PULL_UP)

button_state = 1

# Traffic light bank 1
red1 = Pin(7, Pin.OUT)
amber1 = Pin(28, Pin.OUT)
green1 = Pin(26, Pin.OUT)

# Traffic light bank 2
red2 = Pin(0, Pin.OUT)
amber2 = Pin(1, Pin.OUT)
green2 = Pin(2, Pin.OUT)

# Pedestrian head bank 1
p_red1 = Pin(3, Pin.OUT)
p_green1 = Pin(4, Pin.OUT)

# Pedestrian head bank 2
p_red2 = Pin(5, Pin.OUT)
p_green2 = Pin(6, Pin.OUT)

# sets the traffic lights to green and the pedestrian lights to red at startup
green1.high()
green2.high()
p_red1.high()
p_red2.high()

# These are the functions required for each state of the lights and will run when called in the while true loop
# each line in the function gets initated until the last line of the function is reached.
# Then it returns to the next line in the while loop
def traffic_go():
    green1.high()
    green2.high()
    amber1.low()
    amber2.low()
    red1.low()
    red2.low()
    
def traffic_caution():
    amber1.high()
    amber2.high()
    red1.low()
    red2.low()
    green1.low()
    green2.low()
    
def traffic_stop():
    red1.high()
    red2.high()
    green1.low()
    green2.low()
    amber1.low()
    amber2.low()
    
def ped_stop():
    p_red1.high()
    p_red2.high()
    p_green1.low()
    p_green2.low()
    
    
def ped_go():
    p_red1.low()
    p_red2.low()
    p_green1.high()
    p_green2.high()
    
                  
# Start of the for ever loop 

while True:
    button_state = button.value()
    if button_state == 0:
        utime.sleep(3)
        traffic_caution()
        utime.sleep(2)
        traffic_stop()
        utime.sleep(1)
        ped_go()
        utime.sleep(10)
        ped_stop()
        utime.sleep(2)
        traffic_caution()
        utime.sleep(2)
        traffic_go()
        utime.sleep(5)
