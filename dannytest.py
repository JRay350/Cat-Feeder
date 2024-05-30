import RPi.GPIO as GPIO
import time
import sys
# Define the GPIO pins connected to the stepper motor
PIN1 = 5
PIN2 = 6
PIN3 = 13
PIN4 = 19
BUTTON  = 26
# Define the sequence of signals for 4-phase stepping
sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]
# check = False
def pressed(channel):
    global check
    print("button pressed")
    setup()
    openfood()
    cleanup()
    # check = True


def setup():
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)
    # Set the motor pins as output
    GPIO.setup(PIN1, GPIO.OUT)
    GPIO.setup(PIN2, GPIO.OUT)
    GPIO.setup(PIN3, GPIO.OUT)
    GPIO.setup(PIN4, GPIO.OUT)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


def cleanup():
    # Clean up GPIO settings
    GPIO.cleanup()

def step_motor(direction, steps):
    for j in range(steps):
        if direction == 1:  # Forward
            for i in range(8):
                GPIO.output(PIN1, sequence[i][0])
                GPIO.output(PIN2, sequence[i][1])
                GPIO.output(PIN3, sequence[i][2])
                GPIO.output(PIN4, sequence[i][3])
                time.sleep(0.002)
        else:  # Reverse
            for i in range(7, -1, -1):
                GPIO.output(PIN1, sequence[i][0])
                GPIO.output(PIN2, sequence[i][1])
                GPIO.output(PIN3, sequence[i][2])
                GPIO.output(PIN4, sequence[i][3])
                time.sleep(0.002)

def openfood():
    # Step motor forward for 200 steps
    step_motor(1, 200)
    time.sleep(0.5)  # Pause for 1 second
    
    # Step motor reverse for 200 steps
    step_motor(-1, 200)
    time.sleep(0.5)  # Pause for 0.5 seconds

# if __name__ == '__main__':
#     try:
#         setup()
#         GPIO.add_event_detect(BUTTON, GPIO.RISING, callback = pressed, bouncetime=100)
#         while (True):
#             if check:
#                 openfood()
#             else:
#                 print("")
#     except KeyboardInterrupt:
#         pass
#     finally:
#         cleanup()