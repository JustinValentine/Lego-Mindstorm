#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_D, MoveTank
from time import sleep
from drive import draw_curve
import sys

steer_pair = MoveSteering(OUTPUT_D, OUTPUT_A, motor_class=LargeMotor)
tank = MoveTank(OUTPUT_D, OUTPUT_A, motor_class=LargeMotor)

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


# commands tweaked by trial and error to approximate a lemniscate
def manual_lemniscate():
    for i in range(10):
        steer_pair.on_for_seconds(steering=i/10 * 35, speed=30, seconds=0.2, brake=False)
    steer_pair.on_for_seconds(35, speed=30, seconds=2.3, brake=False)
    for i in range(1, 11):
        steer_pair.on_for_seconds(steering=35 - 35*i/10, speed=30 - 5*i/10, seconds=0.2, brake=False)


    for i in range(10):
        steer_pair.on_for_seconds(steering=-( i/10 * 45 ), speed=30, seconds=0.2, brake=False)
    steer_pair.on_for_seconds(-38, speed=30, seconds=2.3, brake=False)
    for i in range(1, 11):
        steer_pair.on_for_seconds(steering=-(35 - 35*i/10), speed=30 - 15*i/10, seconds=0.2, brake=False)

# using commands computed in oscillatingcircle.py to draw a lemniscate
def lemniscate():
    draw_curve()

def turn_90_degrees():
    steer_pair.on_for_seconds(steering=84, speed=10, seconds=1.6)
    # tank.on_for_seconds(36, -36, 0.25)

def rectangle():
    for step in range(4):
        debug_print('step {}'.format(step))
        steer_pair.on_for_seconds(steering=0, speed=30, seconds=1.5)
        steer_pair.on_for_seconds(steering=84, speed=10, seconds=1.6)


def line():
    # lower or raise speed/seconds to adjust line length
    steer_pair.on_for_seconds(steering=0, speed=30, seconds=3, block=True)

# uncomment to run the respective shape
# rectangle()
# lemniscate()
# line()

