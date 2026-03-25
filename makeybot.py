# MakeyBot
# ============================================================================
# Raspberry Pi Global Setting
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import RGBLED
from gpiozero import Servo
from time import sleep
import time
# Raspberry Pi Pins
# YOUR PINS ARE DIFFERENT!!!!!!!!!!!!!!!!!!!!!!!!!!!

right_eye_led = RGBLED(red="BOARD3", green="BOARD5", blue="BOARD7")
left_eye_led = RGBLED(red="BOARD8", green="BOARD10", blue="BOARD12")
red_led = LED("BOARD11")
yellow_led = LED("BOARD13")
green_led = LED("BOARD16")
SERVO_PIN = "BOARD32"


def blink():
    print("LED on")
    red_led.on()
    time.sleep(1)
    print("LED off") 
    red_led.off()
    time.sleep(1)
    yellow_led.on()
    time.sleep(1)
    print("LED on") 
    yellow_led.off()
    time.sleep(1)
    print("LED off")
    green_led.on()
    time.sleep(1)
    print("LED off") 
    green_led.off()
    time.sleep(1)

def wave():
    arm_servo = Servo(SERVO_PIN)
    for i in range (5):
        print('moving to min')
        arm_servo.min()
        sleep(2)
        print('moving to mid')
        arm_servo.mid()
        sleep(2)
        print('moving to max')
        arm_servo.max()
        sleep(2)
        print('moving to mid')
        arm_servo.mid()
        sleep(2)
        print('moving to max')
        arm_servo.max()
        #sleep(2)
        arm_servo.detach()

def rgb_225_to_1(rgb):
    r,g,b = rgb
    r_convert = r/255
    g_convert = g/255
    b_convert = b/255
    print(r_convert,g_convert,b_convert)
    return(r_convert,g_convert,b_convert)

def LEDtest():
    print("Starting Program")
    eye_command = {"set_left_rgb_eye_color": [30,17,55]}
    print(eye_command)
    
    eye_rgb = eye_command["set_left_rgb_eye_color"]
    eye_rgb = rgb_225_to_1(eye_rgb)
    left_eye_led.color = eye_rgb
    sleep(2)
    left_eye_led.color = (0,0,0)
    sleep(2)
    right_eye_led.color = eye_rgb
    sleep(2)
    right_eye_led.color = (0,0,0)
    sleep(2)


def run_boot_test():
    print("running boot test")
    wave()
    blink()
    LEDtest()
    print('finished boot test')

def main():
    print("Starting Program")
    run_boot_test()
    
    command = {"robot": "Bob",  "features": {"eyes": {"set_left_rgb_eye_color": [0, 17, 5]}}}
    print(command)
    
    command = {"robot": "Bob", "features": {"stop_light": {"traffic": "stop"}}}
    # command = {"robot": "Bob", "features": {"stop_light": {"traffic": "caution"}}}
    # command = {"robot": "Bob", "features": {"stop_light": {"traffic": "go"}}}
    # command = {"robot": "Bob", "features": {"stop_light": {"traffic": {"mode": "cycle", "red_duration": 5000, "yellow_duration": 2000, "green_duration": 4000}}}}
    print(command)
    print("Ending Program")

main()
