import math

def atan2d(a, b) -> float:
    return math.degrees(math.atan2(b[0] - a[0], b[1] - a[1]))
    