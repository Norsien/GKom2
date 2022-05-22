import numpy as np

class Line():
    def __init__ (self, a, b):
        self.a = a
        self.b = b
        self.visible = True
    
    def cut(self, top, right, bottom, left):
        compare(self, 1, bottom, -1)
        compare(self, 1, top, 1)

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

def plane(a, b, c):
    v1 = np.array([c[0]-a[0], c[1]-a[1], c[2]-a[2]])
    v2 = np.array([b[0]-a[0], b[1]-a[1], b[2]-a[2]])
   # p = np.array([c[0], c[1], c[2]])
    cp = np.cross(v1, v2)
    a, b, c = cp
   # d = np.dot(cp, p)
    return [a, b, c]


def move(a, b, fraction):
    a[0] += (b[0] - a[0]) * fraction
    a[1] += (b[1] - a[1]) * fraction  
        
def compare(self, i, val, a):
    s = self.a
    t = self.b
    if s[i] * a > val * a:
        if t[i] * a <= val * a:
            fraction = (val - s[i])/(t[i]-s[i])
            move(s, t, fraction)
            return
        else:
            self.visible = False
            return
    if t[i] * a > val * a:
        fraction = (val - t[i])/(s[i]-t[i])
        move(t, s, fraction)
        return
    return

def intersect(planeNormal, planePoint, lineVector, linePoint):
    planeNormal = np.array([10, 0, 0])
    planePoint = np.array([1, 0, 0])
    lineVector = np.array([0.06, 0.11, 1])
    linePoint = np.array([0, 0, 0])

    dottta = planeNormal.dot(lineVector)
    w = linePoint - planePoint
    si = -planeNormal.dot(w) / dottta
    po = w + si * lineVector + planePoint
    return po

