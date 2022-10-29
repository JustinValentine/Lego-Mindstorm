import numpy as np
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_D, MoveTank

#tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)

# -- Constants --
d = 5.25 # distance between wheels // 2
VelDrive = 30 # Constant speed
maxSpeed = 50 # maximum speed
TotSteps = 50 # Number of time steps
Time = 4*np.pi
v_l, v_r = [], []


# == Eq's ==
t = np.linspace(0, Time, TotSteps) # time
# ===========================================
# -- Lemniscate -
a = 100
x = a*np.cos(1/2*t) * 1/(1+np.sin(1/2*t)**2)
y = a*np.sin(1/2*t)*np.cos(1/2*t) * 1/(1+np.sin(1/2*t)**2)
# -- line --
"""x = t
y = 0*t"""
# -- Circle --
"""x = 5*np.cos(t)
y = 5*np.sin(t)"""
# -- Lissajous curve --
"""x = 4*np.cos(3*t)
y = 4*np.sin(2*t)"""
# -- Test 1 --
"""x = 2*np.cos(t)+1
y = 5*np.sin(2*t)"""
# -- cardioid --
"""x = 2*np.cos(t)*(1-np.cos(t))
y = 2*np.sin(t)*(1-np.cos(t))"""


def WheelSpeed(t,x,y):
    # == derivatives ==
    dir_x_1 = np.gradient(x,t)
    dir_x_2 = np.gradient(dir_x_1,t)
    dir_y_1 = np.gradient(y,t)
    dir_y_2 = np.gradient(dir_y_1,t)

    R = abs((dir_x_1**2 + dir_y_1**2)**(3/2)/
        (dir_x_1*dir_y_2 - dir_x_2*dir_y_1))


    v_l = VelDrive + VelDrive*d/R
    v_r = VelDrive - VelDrive*d/R

    """v_l, v_r = wheelSpeedLimit(v_l, v_r)"""

    return v_l, v_r


def wheelSpeedLimit(v_l, v_r):
    for i in range(len(v_l)):
        if abs(v_l[i]) > maxSpeed:
            s = np.sign(v_r[i])
            factor = v_l[i]/maxSpeed

            v_l[i] /= factor
            v_r[i] /= s*factor

    for i in range(len(v_r)):
        if abs(v_r[i]) > maxSpeed:
            s = np.sign(v_l[i])
            factor = v_r[i]/maxSpeed

            v_l[i] /= s*factor
            v_r /= factor

    return v_l, v_r


def drive():
    v_l, v_r = WheelSpeed(t, x, y)
    StepTime = Time/TotSteps

    lines = []

    with open('c312-lab1/Lemniscate.txt', 'w') as f:
        for i in range(len(t)):
            f.write(str(v_l[i]) + ' ' + str(v_r[i]) + ' ' + str(StepTime))
            f.write('\n')
    f.close()

    print(str(v_l))
    print(str(v_r))
    print(str(t))

    StepTime = Time/TotSteps
    for i in range(TotSteps):
        pass
        #tank_drive.on_for_seconds(v_l[i], v_r[i], StepTime)

drive()
