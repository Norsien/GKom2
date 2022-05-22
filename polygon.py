import line
import edge
import numpy as np

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
            l.cut(1, 1, -1, -1)
            if l.visible:
                if (l.a[1] != l.b[1]):
                    e = edge.Edge(l.a, l.b, self)
                    edges.append(e)
        self.lines = lines
        self.edges = edges

    def is_visible(self, top, right, bottom, left):
        if self.right < left or self.left > right \
            or self.top < bottom or self.bottom > top:
            return False
        return True

    def is_inside(self, top, right, bottom, left):
        if self.right > right or self.left < left \
            or self.top > top or self.bottom < bottom:
            return False
        return True

    # def printplane(self):
    #    print(  "z = " + str(self.leftone.z) + \
    #           " zzlope = " + str(self.zzlope) )

    def printplane(self):
        print(str(self.plane[0]) + "x + " + \
                str(self.plane[1]) + "y + " + \
                str(self.plane[2]) + "z")

    def depth(self, x, y):
        planeNormal = np.array([self.plane[0], self.plane[1], self.plane[2]])
        planePoint = np.array([self.apoint[0], self.apoint[1], self.apoint[2]])
        lineVector = np.array([x, y, 1])
        linePoint = np.array([0, 0, 0])
        dottta = planeNormal.dot(lineVector)
        w = linePoint - planePoint
        si = -planeNormal.dot(w) / dottta
        po = w + si * lineVector + planePoint
        return po[2]

    