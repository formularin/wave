"""Useful functions for "AM and FM Radio Waves.ipynb"
"""


import math


# ========== Trigonometry ========== #


class SinExpression:
    """A class that allows sine expression outputs to also contain their inputs.
    """

    def __init__(self, x):
        self.input = x
        self.multiplier = 1
        self.adden = 0

    def __float__(self):
        return self.multiplier * math.sin(math.radians(self.input)) + self.adden

    def __add__(self, other):
        s = SinExpression(self.input)
        s.multiplier = self.multiplier
        s.adden = self.adden + other
        return s

    def __mul__(self, other):
        s = SinExpression(self.input)
        s.mutliplier = self.multiplier * other
        return s
    
    def __truediv__(self, other):
        s = SinExpression(self.input)
        s.mutliplier = self.multiplier / other
        return s


def sin(x):
    """Returns the sine of `x` degrees.
    """
    return SinExpression(x)


def asin(x):
    """Returns the arcsine of `x` in degrees.

    `x` must be a SinExpression object.
    """
    if round(x.multiplier, 6) == 1:
        return x.input
    else:
        return math.degrees(math.asin(float(x)))


# ========== Visualization ========== #


def draw_graph(func):
    """Generates a matplotlib graph of a function `func`

    Performs `func` on x-vals incrementing by hundreths from -90 to 450.
    """

    # Import inside of function so that `plt` of this cell does not
    # interfere with that of later cells.
    import matplotlib.pyplot as plt

    # Generate list of function outputs.
    X = [x / 100 for x in range(54000)]
    Y = [func(x) for x in X]
    
    # Draw graph.
    plt.plot(X, Y)
    plt.show()


def draw_wave(wave):
    """Draws a graph from a list in the format of the output of `create_wave`.
    """
    
    import matplotlib.pyplot as plt

    X = []
    Y = []
    for i, point in enumerate(wave):
        X.append(i / 100)
        Y.append(point[1])

    plt.plot(X, Y)
    plt.show()


# ========== Lists and such things ========== #


def create_wave(func):
    """Generates a 2-d list of (x, y) coordinate pairs from a function.
    """

    wave = []
    for x in range(54000):
        wave.append((x / 100, func(x / 100)))

    return wave


def add_waves(wave_1, wave_2):
    """Creates a wave that is the sum of the amplitudes of two waves at
    each point in time.
    """
    return [(w1[0], w1[1] + w2[1]) for w1, w2 in zip(wave_1, wave_2)]