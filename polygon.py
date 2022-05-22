import edge
import numpy as np
from math import sqrt

class Polygon():
    def __init__(self, lines, color):
        self.left = 2
        self.right = -2
        self.top = -2
        self.bottom = 2
        self.id = 0
        self.active = False
        self.color = color

        for l in lines:
            self.left = min(self.left, l.a[0], l.b[0])
            self.right = max(self.right, l.a[0], l.b[0])
            self.top = max(self.top, l.a[1], l.b[1])
            self.bottom = min(self.bottom, l.a[1], l.b[1])
        
        edges = []
        for l in lines:
            if l.visible:
                if (l.a[1] != l.b[1]):
                    e = edge.Edge(l.a, l.b, self)
                    edges.append(e)
        self.edges = edges

    def is_visible(self, top, right, bottom, left, close):
        if self.right < left or self.left > right \
            or self.top < bottom or self.bottom > top:
            return False

        return True

    def depth(self, x, y):
        planePoint = np.array([self.apoint[0], self.apoint[1], self.apoint[2]])
        lineVector = np.array([x, y, 1])
        linePoint = np.array([0, 0, 0])
        dottta = self.plane.dot(lineVector)
        w = linePoint - planePoint
        si = -self.plane.dot(w) / dottta
        po = w + si * lineVector + planePoint
        return po[2]


    def calc_plane(self, a, b, c):
        v1 = np.array([c[0]-a[0], c[1]-a[1], c[2]-a[2]])
        v2 = np.array([b[0]-a[0], b[1]-a[1], b[2]-a[2]])
        self.plane = np.cross(v1, v2)
        self.d = np.dot(self.plane, self.apoint)

    def calc_point(self, p):
        self.apoint =  np.array([p[0], p[1], p[2]])

    def distance(self):
        dis = self.d/sqrt(self.plane[0]**2 + self.plane[1]**2 + self.plane[2]**2)
        return dis