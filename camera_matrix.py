import numpy as np
from math import cos, sin, pi

ONEROTATION = pi/18
ONESTEP = 0.5

class Camera():
    def __init__(self):
        self.zoom_now = 5
        self.poz = np.array([3.0, 5.0, -15.0])
        self.C = np.array([ [1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1.0]])
        self.R = np.matrix([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]])

    def reset(self):
        self.zoom_now = 5
        self.poz = np.array([3.0, 5.0, -15.0])
        self.C = np.array([ [1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1.0]])
        self.R = np.matrix([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]])

    def ground(self):
        self.R = np.matrix([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]])

    def rotateX(self, K):
        Rx = np.matrix([[1, 0,      0],
                        [0, cos(ONEROTATION*K), sin(ONEROTATION*K)],
                        [0, -sin(ONEROTATION*K), cos(ONEROTATION*K)]])
        self.R = Rx * self.R

    def rotateY(self, K):  
        Ry = np.matrix([[cos(ONEROTATION*K),  0, -sin(ONEROTATION*K)],
                        [0,       1, 0],
                        [sin(ONEROTATION*K), 0, cos(ONEROTATION*K)]])
        self.R = Ry * self.R

    def rotateZ(self, K):
        Rz = np.matrix([[cos(ONEROTATION*K), sin(ONEROTATION*K), 0],
                        [-sin(ONEROTATION*K), cos(ONEROTATION*K),  0],
                    [0,      0,       1]])
        self.R = Rz * self.R

    def go(self, x, y, z):
        mv = np.matrix([ONESTEP*x, ONESTEP*y, ONESTEP*z]).T
        Rinv = np.linalg.inv(self.R)
        step = np.array((Rinv*mv).T).flatten()
        self.poz += step

    def changeZoom(self, d):
        zoom = [1.5, 1.4, 1.3, 1.2, 1.1, 1, 0.9, 0.8, 0.7, 0.6, 0.5]
        self.zoom_now += d
        self.zoom_now = max(0, self.zoom_now)
        self.zoom_now = min(len(zoom)-1, self.zoom_now)
        self.C[2][2] = zoom[self.zoom_now]

    def matrix(self):
        return self.C * self.R

    def position(self):
        return self.poz