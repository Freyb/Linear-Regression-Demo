from random import uniform

import numpy as np
import matplotlib.pyplot as plt

# Config
MIN_X = -1.
MAX_X = 1.
NUM_POINTS = 100
NOISE_X = .1
NOISE_Y = .3


def f(x):
    return 1.53 * x + 10


# Generation
xs = list()
ys = list()

for i in np.linspace(MIN_X + NOISE_X, MAX_X - NOISE_X, NUM_POINTS):
    x = i + uniform(-NOISE_X, NOISE_X)
    y = f(x) + uniform(-NOISE_Y, NOISE_Y)
    xs.append(x)
    ys.append(y)

print("xs = ", xs)
print("ys = ", ys)

plt.plot(xs, ys, "bx")
plt.show()
