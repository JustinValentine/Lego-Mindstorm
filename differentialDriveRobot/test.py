import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# -- Graph of curve plt --
fig1, ax1 = plt.subplots()
ln, = plt.plot([], [], lw=2)
ln2, = plt.plot([], [], lw=2)
ln3, = plt.plot([], [], 'o')

# -- Wheel Speed plt --
fig2, ax2 = plt.subplots()
barcollection = plt.bar(['v_l', 'v_r', 'R'],[0, 0, 0])

# -- Constants --
d = 5 # distance between wheels over 2
VelDrive = 30 # constant speed
maxSpeed = 50
Rmax = 550 # max radius of curvatature before it is a line

# == Eq's ==
t = np.linspace(0, 4*np.pi, 200)
# ===========================================
# -- Lemniscate -
a = 50
x = a*np.cos(1/2*t) * 1/(1+np.sin(1/2*t)**2)
y = a*np.sin(1/2*t)*np.cos(1/2*t) * 1/(1+np.sin(1/2*t)**2)

# -- line --
"""x = t
y = 0*t"""

# -- Circle --
"""x = 5*np.cos(t)
y = 5*np.sin(t)"""

# -- Lissajous curve --
"""x = 4*np.cos(1.5*t)
y = 4*np.sin(t)"""

# -- Test 1 --
"""x = 2*np.cos(t)+1
y = 5*np.sin(2*t)"""

# -- cardioid --
"""x = 2*np.cos(t)*(1-np.cos(t))
y = 2*np.sin(t)*(1-np.cos(t))"""


# ===========================================
# == derivatives ==
dir_x_1 = np.gradient(x,t)
dir_x_2 = np.gradient(dir_x_1,t)
dir_y_1 = np.gradient(y,t)
dir_y_2 = np.gradient(dir_y_1,t)
# ===========================================

# -- radius of curvature at reach time step --
R = ((dir_x_1**2 + dir_y_1**2)**(3/2)/
        (dir_x_1*dir_y_2 - dir_x_2*dir_y_1))


def init():
    ax1.set_xlim(-120, 120)
    ax1.set_ylim(-120, 120)
    ln.set_data(x, y)
    return ln,ln2,ln3

def update(i):
    global R
    circle_center_x = ( x[i] +
                        R[i]/((dir_x_1**2 + dir_y_1**2)**(1/2)) *
                        -1 * dir_y_1 )

    circle_center_y = ( y[i] +
                        R[i]/((dir_x_1**2 + dir_y_1**2)**(1/2)) *
                        dir_x_1 )

    R = abs(R)

    circle_x = circle_center_x[i] + R[i]*np.cos(t)
    circle_y = circle_center_y[i] + R[i]*np.sin(t)

    ln2.set_data(circle_x, circle_y)
    ln3.set_data(x[i], y[i])

    return ln, ln2, ln3


def init2():
    ax2.set_ylim(-60, 60)

def update2(i):
    global R

    R = ((dir_x_1**2 + dir_y_1**2)**(3/2)/
        (dir_x_1*dir_y_2 - dir_x_2*dir_y_1))

    v_l = VelDrive + VelDrive*d/R[i]
    v_r = VelDrive - VelDrive*d/R[i]

    print(v_l, v_r)


    barcollection[0].set_height(v_l)
    barcollection[1].set_height(v_r)
    barcollection[2].set_height(R[i])

    return barcollection


ani1 = FuncAnimation(fig1, update, frames=200,
                    init_func=init, blit=True)

anim2 = FuncAnimation(fig2, update2, frames=200,
                      init_func=init2, repeat=True)

plt.show()
