#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import ColorSensor, LightSensor
import ev3dev2
import sys
from time import sleep
from enum import Enum

class BBMode(Enum):
    AGGRESSION = 1
    FEAR = 2
    LOVE = 3

steer_pair = MoveTank(OUTPUT_A, OUTPUT_D, motor_class=LargeMotor)
light_sens_left = ColorSensor(INPUT_1)
light_sens_right = ColorSensor(INPUT_4)
light_sens_left.mode = ColorSensor.MODE_COL_AMBIENT
light_sens_right.mode = ColorSensor.MODE_COL_AMBIENT

mode = BBMode.LOVE
while True:
    left = light_sens_left.ambient_light_intensity
    right = light_sens_right.ambient_light_intensity
    print('Light intensity -- Left: {} Right: {}'.format(left, right), file=sys.stderr)
    if mode == BBMode.AGGRESSION:
        steer_pair.on(min(2*right, 70), min(2*left, 70))
    elif mode == BBMode.FEAR:
        steer_pair.on(left, right)
    elif mode == BBMode.LOVE:
        threshold = 17
        steer_pair.on(max(threshold -left, 0), max(threshold-right, 0))
    sleep(0.2)
