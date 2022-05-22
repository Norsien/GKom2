class Edge():
    def __init__(self, s, t, polygon):
        if t[1] < s[1] :
            s, t = t, s
        self.Xmin = s[0]
        self.x = self.Xmin
        self.Zmin = s[2]
        self.z = self.Zmin
        self.Ymin = s[1]
        self.Ymax = t[1]
        if (t[1] != s[1]): # do not add horizontal lines
            self.slope = (t[0]-s[0])/(t[1]-s[1])
            self.zlope = (t[2]-s[2])/(t[1]-s[1])
        self.polygon = polygon
    
    def print(self):
        print(  "Ymin = " + str(round(self.Ymin, 2)) + \
                " Ymax = " + str(round(self.Ymax, 2)) + \
                " Xmin = " + str(round(self.Xmin, 2)) + \
                " sl = " + str(round(self.slope, 2)) + \
                "    x = " + str (round(self.x, 2)) + \
                "    z = " + str (round(self.z, 2)) + \
                " p = " + str(self.polygon.id))

    def depth(self, x, y):
        return

def Ysort(e):
    return e.Ymin

def Xsort(e):
    return e.x

