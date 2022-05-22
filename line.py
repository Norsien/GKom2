import numpy as np

class Line():
    def __init__ (self, a, b):
        self.a = a
        self.b = b
        self.visible = True

def flatten(s, t):
        if s[2] > 0.000001 or t[2] > 0.000001:
            if t[2] <= 0.000001:
                s, t = t, s
            if s[2] <= 0.000001:
                fraction = ((-s[2]+0.000001)/(t[2]-s[2]))
                move(s, t, fraction)
                s[2] = 0.000001
            a = [s[0]/s[2], s[1]/s[2], s[2]]
            b = [t[0]/t[2], t[1]/t[2], t[2]]
            return a, b

def move(a, b, fraction):
    a[0] += (b[0] - a[0]) * fraction
    a[1] += (b[1] - a[1]) * fraction  