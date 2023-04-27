import tkinter.dnd
from tkinter import *
from tkinter import ttk
import time
from vpython import *
from decimal import Decimal


root = Tk()
root.geometry("250x200")


def start(event):

    print("start")
    scene.width = 2000
    scene.height = 1000
    #scene.camera.pos=vector(0,20,40)
    scene.camera.pos = vector(0, 15, 60)
    a = int(axEntry.get())
    T = int(timeEntry.get())
    v0 = int(veEntry.get())

    root.destroy()

    A = vertex(pos = vector(-scene.width*2, -0.5, scene.width*2))
    b = vertex(pos = vector(scene.width*2, -0.5, scene.width*2))
    d = vertex(pos = vector(-scene.width*2,-0.5, -scene.width*2))
    c = vertex(pos = vector(scene.width*2, -0.5, -scene.width*2))
    Q = quad(vs=[A,b,c,d])
    sph = sphere(color=color.red, pos=vector(0, 0, 0))



    #setingWind = Tk()
    #setingWind.geometry("250x200")
    #textS = Text(setingWind, width=25, height=5)
    #textS.pack()
    sec = 0
    s = 0
    #setingWind.mainloop()



    while sec <= T:
        Tex = label(text= 'Перемещение равно: ' + str(s),
                    pos=vector(0, 20, 0), color=color.green)
        rate(100)
        time.sleep(0.01)
        sec +=0.02
        v = v0 + (a * sec)
        s = v0*sec +((a * sec * sec) / 2)
        s = round(s,1)
       # s = float(Decimal(str(s)))

        l = vector(s, 0, 0)
        sph.pos = sph.pos + l
        print(v)
        Tex.delete()



















StartBtn = Button(root, text="Start")
StartBtn.bind("<Button-1>", start)
StartBtn.pack()
axEntry = Entry()
axEntry.pack(side='bottom')
axEntry.insert(END,'Введите ускорение')
timeEntry = Entry()
timeEntry.insert(END, 'Введите время')
timeEntry.pack(side='left')
veEntry = Entry()
veEntry.insert(END, 'Введите нач.скорость')
veEntry.pack(side='right')
root.mainloop()
