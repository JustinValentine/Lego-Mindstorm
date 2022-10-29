#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_D, MoveTank
from time import sleep, time
import sys

tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)

def main():
    file1 = open('curve.txt', 'r')
    Lines = file1.readlines()
    print(len(Lines[25:-25]), file=sys.stderr)

    for line in Lines[15:-15]: # skip 30 non-clean timesteps
        t1 = time()
        v_l, v_r, TimeStep = map(float, line.split(' '))
        tank_drive.on_for_seconds(v_l, v_r, seconds=TimeStep, block=False, brake=True)
        #print('v_left: {:.3f} v_right: {:.3f}'.format(v_l, v_r), file=sys.stderr)
        t2 = time()
        sleep(TimeStep - (t2-t1))


if __name__ == "__main__":
    main()
