class Edge():
    def __init__(self, s, t, polygon):
        if t[1] < s[1] :
            s, t = t, s
        self.Xmin = s[0]
        self.x = self.Xmin
        self.Ymin = s[1]
        self.Ymax = t[1]
        if (t[1] != s[1]): # do not add horizontal lines
            self.slope = (t[0]-s[0])/(t[1]-s[1])
        self.polygon = polygon

def Ysort(e):
    return e.Ymin

def Xsort(e):
    return e.x