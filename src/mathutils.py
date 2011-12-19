import math

# When t is 0, returns a, when t is 1, returns b, in between it blends between a and b.
def interpolate(a, b, t):
    return a * (1.0 - t) + b * t


