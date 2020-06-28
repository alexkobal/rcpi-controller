import signal
import pigpio
import math
import time
import sys
from xbox360controller import Xbox360Controller

SERVO_PIN = 18
ESC_PIN = 17
pi = pigpio.pi()
MAX_TURN_THROTTLE = 500
MAX_MOVE_THROTTLE = 500
turn_throttle = MAX_TURN_THROTTLE
move_throttle = MAX_MOVE_THROTTLE

def finalize():
    pi.set_servo_pulsewidth(SERVO_PIN, 1500)
    time.sleep(0.1)
    pi.write(SERVO_PIN, 0)
    pi.write(ESC_PIN, 0)
    print('Everything turned off, shutting down...')

def restore_throttle(button):
    global turn_throttle
    global move_throttle
    global MAX_TURN_THROTTLE
    global MAX_MOVE_THROTTLE
    turn_throttle = MAX_TURN_THROTTLE
    move_throttle = MAX_MOVE_THROTTLE

def set_throttle(axis):
    global turn_throttle
    global move_throttle
    if axis.x==1:
        if turn_throttle < MAX_TURN_THROTTLE:
            turn_throttle+=20
    if axis.x==-1:
        if turn_throttle > 0:
            turn_throttle-=20
    if axis.y==1:
        if move_throttle < MAX_MOVE_THROTTLE:
            move_throttle+=10
    if axis.y==-1:
        if move_throttle > 0:
            move_throttle-=10

def turn(axis):
    global turn_throttle
    pulsewidth = math.floor(round(1500 + turn_throttle * axis.x * -1))
    pi.set_servo_pulsewidth(SERVO_PIN, pulsewidth)

def forward(axis):
    global move_throttle
    pulsewidth = math.floor(round(1500 + move_throttle * axis.value))
    pi.set_servo_pulsewidth(ESC_PIN, pulsewidth)

def backward(axis):
    global move_throttle
    pulsewidth = math.floor(round(1500 - move_throttle * axis.value))
    pi.set_servo_pulsewidth(ESC_PIN, pulsewidth)

def stop(button):
    finalize()

try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        controller.info()

        controller.axis_l.when_moved = turn
        controller.hat.when_moved = set_throttle

        controller.trigger_l.when_moved = backward
        controller.trigger_r.when_moved = forward

        controller.button_mode.when_pressed = stop
        controller.button_select.when_pressed = restore_throttle

        print('\nControlls>>>>>>>>>>>>\nRT: Move forward\nLT: Move backward\nXbox: Reset\nBack: Reset throttle\nHat Up/Down: Movement throttle\nHat Left/Right: Turn throttle')

        signal.pause()
except (KeyboardInterrupt, SystemExit) as e:
    pass
finally:
    finalize()

