# equations.py>
import numpy as np

def derivatives(x, y, t):
    dir_x_1 = np.gradient(x,t)
    dir_x_2 = np.gradient(dir_x_1,t)
    dir_y_1 = np.gradient(y,t)
    dir_y_2 = np.gradient(dir_y_1,t)
    return dir_x_1, dir_x_2, dir_y_1, dir_y_2


def lemniscate(t, a, frac):
    x = a*np.cos(frac*t) * 1/(1+np.sin(frac*t)**2)
    y = a*np.sin(frac*t)*np.cos(frac*t) * 1/(1+np.sin(frac*t)**2)
    return x, y


def circle(t, a, frac):
    x = a*np.cos(frac * t)
    y = a*np.sin(frac * t)
    return x, y


def line(t, a, frac):
    x = t
    y = frac*t
    return x, y


def lissajous(t, a, b, fracx, fracy):
    x = a*np.cos(fracx*t)
    y = b*np.sin(fracy*t)
    return x, y


def cardioid(t, a, frac):
    x = a*np.cos(frac*t)*(1-np.cos(frac*t))
    y = a*np.sin(frac*t)*(1-np.cos(frac*t))
    return x, y
