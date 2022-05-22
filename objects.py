import numpy as np

def box(ax, ay, az, bx, by, bz):
    vertices = np.matrix([[ ax, ay, az],
                          [ ax, ay, bz],
                          [ ax, by, bz],
                          [ ax, by, az],
                          [ bx, ay, az],
                          [ bx, ay, bz],
                          [ bx, by, bz],
                          [ bx, by, az]])
    edges = [[0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]]
    walls = [[0, 1, 2, 3], [4, 5, 6, 7],
            [0, 8, 4, 9], [1, 9, 5, 10],
            [2, 10, 6, 11], [3, 11, 7, 8]]
    return vertices, edges, walls

def getObjects():
    ARoad = np.matrix([[-20, 0, -1],
                    [20, 0, -1],
                    [-20, 0, -5],
                    [20, 0, -5]])
    VRoad = [[0, 1], [1, 3], [2, 3], [2, 0]]
    WRoad = [[0, 1, 2, 3]]
    ARoad2 = np.matrix([[-0.5, 0, -12],
                    [-0.5, 0, -5],
                    [0.5, 0, -12],
                    [0.5, 0, -5]])
    VRoad2 = [[0, 1], [1, 3], [2, 3], [2, 0]]
    WRoad2 = [[0, 1, 2, 3]]

    A1, V1, W1 = box(1, 0 , 1, 4, 5, 3)
    A2, V2, W2 = box(-1, 0, 2, -4, 3, 4)
    A2b, V2b, W2b = box(-5, 0, 2, -8, 4, 4)
    A2c, V2c, W2c = box(-9, 0, 2, -12, 3, 4)
    A3, V3, W3 = box(-1, 0, -7, -5, 2, -11)
    A4, V4, W4 = box(2, 0, -7, 8, 2, -10)

    colors = ["#7DCEA0", "#16A085", "#8E44AD", "#EC7063", "#F39C12", "#145A32"]
    objects = []
    #objects.append((ARoad, VRoad, WRoad, colors))
    #objects.append((ARoad2, VRoad2, WRoad2,"colors"))
    objects.append((A1, V1, W1, colors))
    objects.append((A2, V2, W2, colors))
    objects.append((A2b, V2b, W2b, colors))
    objects.append((A2c, V2c, W2c, colors))
    objects.append((A3, V3, W3, colors))
    objects.append((A4, V4, W4, colors))
    return objects

def getObjects2():
    ARoad = np.matrix([[-20, 0, -1],
                    [20, 0, -1],
                    [-20, 0, -5],
                    [20, 0, -5]])
    VRoad = [[0, 1], [1, 3], [2, 3], [2, 0]]
    WRoad = [[0, 1, 2, 3]]
    A1, V1, W1 = box(1, 0 , 1, 4, 5, 3)

    colors = ["#7DCEA0", "#16A085", "#8E44AD", "#EC7063", "#F39C12", "#145A32"]
    objects = []
    #objects.append((ARoad, VRoad, WRoad, "black"))
    objects.append((A1, V1, W1, colors))

    return objects