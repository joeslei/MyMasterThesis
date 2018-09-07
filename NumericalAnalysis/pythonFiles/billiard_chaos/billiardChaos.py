import numpy as np
import matplotlib.pyplot as plt

def ellasticCollision(theta):
    return -theta


# the radius of the semi-circles
radius = 1

# the length of a side of a  rectangle
l = 1

# the speed of a particle
speed = 1

def borderOfStadium(x, y):
    circle = np.sqrt(radius ** 2 - (x - l) ** 2)
    if np.abs(x) <= l:
        return r if y > 0 else -r
    else:
        return circle if  y > 0 else -circle


