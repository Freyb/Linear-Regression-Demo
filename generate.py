from random import uniform

import numpy as np

# Config
MIN_X = -1.
MAX_X = 1.
NUM_POINTS = 30
NOISE_X = .02
NOISE_Y = .03


def f(x):
    return 1.53 * x + 100


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
