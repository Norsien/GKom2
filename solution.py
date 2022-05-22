import numpy as np
from math import cos, sin, pi
import tkinter as tk
import objects as ob
import camera_matrix
import line
import polygon
import edge

# calc
RESIZE = 300
eps = 0.00000001

# get objects
objects = ob.getObjects()

def calcPolygons():
    polygons = []
    p_id = 1
    for o in objects:
        Vertices, Edges, Walls, colors = o
        points = []
        for point in Vertices:
            f = c.matrix()*(point-c.position()).T
            b = [f.item(0), f.item(1), f.item(2)]
            points.append(b)

        for w in Walls:
            newColor = colors[p_id%6]
            lines = []
            p1 = points[Edges[w[0]][0]]
            p2 = points[Edges[w[0]][1]]
            p3 = points[Edges[w[2]][0]]
            plane = line.plane(p1, p2, p3)
            for e in w:
                s = points[Edges[e][0]].copy()
                t = points[Edges[e][1]].copy()
                pt = line.flatten(s, t)
                if pt != None:
                    l = line.Line(pt[0], pt[1])
                    lines.append(l)
            p = polygon.Polygon(lines, newColor)
            p_id += 1
            if p.is_visible(1, 1, -1, -1):
                p.id = p_id
                p.plane = plane
                p.apoint = p1
                polygons.append(p)

    edges = []
    for p in polygons:
        for e in p.edges:
            edges.append(e)

    currentY = -1.0
    Ygain = 1.0/RESIZE
    edges.sort(key=edge.Ysort)

    current_edges = []
    w = 0
    for q in range (0, 2*RESIZE):
        for p in polygons:
            e.polygon.active = False
        while (w < len(edges) and edges[w].Ymin <= currentY):
            current_edges.append(edges[w])
            w += 1
        current_edges = [e for e in current_edges if e.Ymax > currentY]
        for e in current_edges:
            e.x = e.Xmin + (currentY - e.Ymin) * e.slope
            
        current_edges.sort(key=edge.Xsort)
        current_walls = []
        currentX = -1.0
        for e in current_edges:
            if e.x > currentX:
                if len(current_walls) > 0:
                    top_layer = current_walls[0]
                    leftZ = top_layer.depth(currentX, currentY)
                    rightZ = top_layer.depth(e.x, currentY)
                    for i in range(1, len(current_walls)):
                        ed = current_walls[i]
                        lZ = ed.depth(currentX, currentY)
                        rZ = ed.depth(e.x, currentY)
                        if lZ <= leftZ + eps  and rZ <= rightZ + eps:
                            top_layer = ed
                            leftZ = top_layer.depth(currentX, currentY)
                            rightZ = top_layer.depth(e.x, currentY)
                        # elif not (lZ >= leftZ  and rZ >= rightZ ):
                        #     print ("Nie fajnie")
                        #     print(lZ, leftZ, rZ, rightZ)
                    color = top_layer.color

                    l = screen.create_line(currentX*RESIZE+RESIZE, RESIZE-currentY*RESIZE, \
                        e.x*RESIZE + RESIZE, RESIZE-currentY*RESIZE, fill=color)

                # for h in current_walls:
                #     h.printplane()

                currentX = e.x
            if (e.polygon.active):
                e.polygon.active = False
                current_walls.remove(e.polygon)
            else:
                e.polygon.active = True
                current_walls.append(e.polygon)

        currentY += Ygain
        
def updatePos():
    positionsField.configure(state="normal")
    positionsField.delete(1.0, "end")
    txt = "x = {:.2f}, y = {:.2f}, z = {:.2f}"
    poz = c.position()
    positionsField.insert(1.0, txt.format(poz[0], poz[1], poz[2]))
    positionsField.configure(state="disabled")

def showNow():
    screen.delete('all')
    calcPolygons()
    updatePos()

def r1():
    c.rotateX(-1)
    showNow()

def r2():
    c.rotateX(1)
    showNow()

def r3():
    c. rotateY(-1)
    showNow()

def r4():
    c.rotateY(1)
    showNow()

def r5():
    c.rotateZ(1)
    showNow()

def r6():
    c.rotateZ(-1)
    showNow()

def goLeft():
    c.go(-1, 0, 0)
    showNow()

def goRight():
    c.go(1, 0, 0)
    showNow()

def goUp():
    c.go(0, 1, 0)
    showNow()

def goDown():
    c.go(0, -1, 0)
    showNow()

def goForw():
    c.go(0, 0, 1)
    showNow()

def goBack():
    c.go(0, 0, -1)
    showNow()

def zoomIn():
    c.changeZoom(1)
    showNow()

def zoomOut():
    c.changeZoom(-1)
    showNow()

def reset():
    c.__init__()
    showNow()

def ground():
    c.ground()
    showNow()

# tkinter
root = tk.Tk()
root.title("Virtual Camera")
root.geometry("1024x800")
root.minsize(max(295, 2*RESIZE), 168+2*RESIZE)
bottompanel=tk.Frame(root, background="#83eeff", height=14)
bottompanel.pack(side="bottom", fill="x")
mainpanel=tk.Frame(root,  background="#222222")
mainpanel.pack(anchor='center', fill="both", expand=True)
screen = tk.Canvas(mainpanel, height=2*RESIZE, width=2*RESIZE)
screen.pack(anchor='center',fill="none", expand=True)
positionsField = tk.Text(mainpanel, height = 1, width = 33)
positionsField.insert("1.0", "x= a, y= b, z= c")
positionsField.configure(state="disabled")
positionsField.pack()
c = camera_matrix.Camera()
showNow()
buttonpanel=tk.Frame(bottompanel)
buttonpanel.pack()
buttons = ["up", "down", "", "look up", "look down",
           "left", "right", "reset", "turn left", "turn right",
           "forward", "back", "ground", "tilt left", "tilt right"]
commands = [goUp, goDown, "", r1, r2,
            goLeft, goRight, reset, r3, r4,
            goForw, goBack, ground, r5, r6]
for i, item in enumerate(buttons):
    if i != 2:
        but = tk.Button(buttonpanel, text=buttons[i], height=3, width=9, command=commands[i])
        but.grid(column=i%5, row=i//5)
zoomButtons = tk.Frame(buttonpanel)
zoomButtons.grid(column=2, row=0)
but = tk.Button(zoomButtons, text="+", height= 1, width=9, command=zoomIn)
but.grid(column=0, row=0)
but = tk.Button(zoomButtons, text="-", height=1, width=9, command=zoomOut)
but.grid(column=0, row=1) 
root.mainloop()