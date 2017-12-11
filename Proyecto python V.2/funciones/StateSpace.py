#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import time
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk
from scipy.optimize import minimize
from scipy.interpolate import interp1d
from scipy import signal

class val():
    def __init__(self, a1, b1, c1, d1, a2a, a2b, a2c, a2d, b2a, b2b, c2a, c2b, d2, a3a, a3b, a3c, a3d, b3a, b3b, c3a, c3b, d3, a4a,a4b,a4c,a4d,b4a,b4b,c4a,c4b,c4c,c4d,d4a,d4b):
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        self.d1 = d1
        self.a2a = a2a
        self.a2b = a2b
        self.a2c = a2c
        self.a2d = a2d
        self.b2a = b2a
        self.b2b = b2b
        self.c2a = c2a
        self.c2b = c2b
        self.d2 = d2
        self.a3a = a3a
        self.a3b = a3b
        self.a3c = a3c
        self.a3d = a3d
        self.b3a = b3a
        self.b3b = b3b
        self.c3a = c3a
        self.c3b = c3b
        self.d3 = d3
        self.a4a = a4a
        self.a4b = a4b
        self.a4c = a4c
        self.a4d = a4d
        self.b4a = b4a
        self.b4b = b4b
        self.c4a = c4a
        self.c4b = c4b
        self.c4c = c4c
        self.c4d = c4d
        self.d4a = d4a
        self.d4b = d4b


def PedirDatos(a1, b1, c1, d1, a2a, a2b, a2c, a2d, b2a, b2b, c2a, c2b, d2, a3a, a3b, a3c, a3d, b3a, b3b, c3a, c3b, d3, a4a,a4b,a4c,a4d,b4a,b4b,c4a,c4b,c4c,c4d,d4a,d4b):
    a1 = float(a1)
    b1 = float(b1)
    c1 = float(c1)
    d1 = float(d1)
    a2a = float(a2a)
    a2b = float(a2b)
    a2c = float(a2c)
    a2d = float(a2d)
    b2a = float(b2a)
    b2b = float(b2b)
    c2a = float(c2a)
    c2b = float(c2b)
    d2 = float(d2)
    a3a = float(a3a)
    a3b = float(a3b)
    a3c = float(a3c)
    a3d = float(a3d)
    b3a = float(b3a)
    b3b = float(b3b)
    c3a = float(c3a)
    c3b = float(c3b)
    d3 = float(d3)
    a4a = float(a4a)
    a4b = float(a4b)
    a4c = float(a4c)
    a4d = float(a4d)
    b4a = float(b4a)
    b4b = float(b4b)
    c4a = float(c4a)
    c4b = float(c4b)
    c4c = float(c4c)
    c4d = float(c4d)
    d4a = float(d4a)
    d4b = float(d4b)
    return val(a1, b1, c1, d1, a2a, a2b, a2c, a2d, b2a, b2b, c2a, c2b, d2, a3a, a3b, a3c, a3d, b3a, b3b, c3a, c3b, d3, a4a,a4b,a4c,a4d,b4a,b4b,c4a,c4b,c4c,c4d,d4a,d4b)
va = PedirDatos(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

def StateSpace(a1, b1, c1, d1, a2a, a2b, a2c, a2d, b2a, b2b, c2a, c2b, d2, a3a, a3b, a3c, a3d, b3a, b3b, c3a, c3b, d3, a4a,a4b,a4c,a4d,b4a,b4b,c4a,c4b,c4c,c4d,d4a,d4b):
    va = PedirDatos(a1, b1, c1, d1, a2a, a2b, a2c, a2d, b2a, b2b, c2a, c2b, d2, a3a, a3b, a3c, a3d, b3a, b3b, c3a, c3b, d3, a4a,a4b,a4c,a4d,b4a,b4b,c4a,c4b,c4c,c4d,d4a,d4b)
    a1 = va.a1
    b1 = va.b1
    c1 = va.c1
    d1 = va.d1
    a2a = va.a2a
    a2b = va.a2b
    a2c = va.a2c
    a2d = va.a2d
    b2a = va.b2a
    b2b = va.b2b
    c2a = va.c2a
    c2b = va.c2b
    d2 = va.d2
    a3a = va.a3a
    a3b = va.a3b
    a3c = va.a3c
    a3d = va.a3d
    b3a = va.b3a
    b3b = va.b3b
    c3a = va.c3a
    c3b = va.c3b
    d3 = va.d3
    a4a = va.a4a
    a4b = va.a4b
    a4c = va.a4c
    a4d = va.a4d
    b4a = va.b4a
    b4b = va.b4b
    c4a = va.c4a
    c4b = va.c4b
    c4c = va.c4c
    c4d = va.c4d
    d4a = va.d4a
    d4b = va.d4b

    # problem 1
    A = [a1]
    B = [b1]
    C = [c1]
    D = [d1]
    sys1 = signal.StateSpace(A,B,C,D)
    t1,y1 = signal.step(sys1)

    # problem 2
    A = [[a2a,a2b],[a2c,a2d]]
    texto1.set(np.linalg.eig(A)[0])
    B = [[b2a],[b2b]]
    C = [c2a,c2b]
    D = [d2]
    sys2 = signal.StateSpace(A,B,C,D)
    t2,y2 = signal.step(sys2)

    # problem 3
    A = [[a3a,a3b],[a3c,a3d]]
    texto2.set(np.linalg.eig(A)[0])
    B = [[b3a],[b3b]]
    C = [c3a,c3b]
    D = [d3]
    sys3 = signal.StateSpace(A,B,C,D)
    t = np.linspace(0,30,100)
    u = np.zeros(len(t))
    u[5:50] = 1.0 # first step input
    u[50:] = 2.0  # second step input
    t3,y3,x3 = signal.lsim(sys3,u,t)

    # problem 4
    A = [[a4a,a4b],[a4c,a4d]]
    texto3.set(np.linalg.eig(A)[0])
    B = [[b4a],[b4b]]
    C = [[c4a,c4b],[c4c,c4d]]
    D = [[d4a],[d4b]]
    sys4 = signal.StateSpace(A,B,C,D)
    t4,y4 = signal.step(sys4)


    plt.figure(1)
    plt.subplot(4,1,1)
    plt.plot(t1,y1,'r-',linewidth=3)
    plt.ylabel('Problem 1')
    plt.legend(['y'],loc='best')
    plt.subplot(4,1,2)
    plt.plot(t2,y2,'b--',linewidth=3)
    plt.ylabel('Problem 2')
    plt.legend(['y'],loc='best')
    plt.subplot(4,1,3)
    plt.plot(t3,y3,'k-',linewidth=3)
    plt.plot(t,u,'r-')
    plt.ylabel('Problem 3')
    plt.legend(['y','u'],loc='best')
    plt.subplot(4,1,4)
    plt.plot(t4,y4[:,0]+2.0,'r--',linewidth=3)
    plt.plot(t4,y4[:,1]+2.0,'b-',linewidth=3)
    plt.legend(['y1','y2'],loc='best')
    plt.ylabel('Problem 4')
    plt.xlabel('Time')
    plt.show()




imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/StateSpace.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("State Space")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)


v1= StringVar()
v2= StringVar()
v3= StringVar()
v4= StringVar()
v5= StringVar()
v6= StringVar()
v7= StringVar()
v8= StringVar()
v9= StringVar()
v10 = StringVar()
v11 = StringVar()
v12 = StringVar()
v13 = StringVar()
v14 = StringVar()
v15 = StringVar()
v16 = StringVar()
v17 = StringVar()
v18 = StringVar()
v19 = StringVar()
v20 = StringVar()
v21 = StringVar()
v22 = StringVar()
v23 = StringVar()
v24 = StringVar()
v25 = StringVar()
v26 = StringVar()
v27 = StringVar()
v28 = StringVar()
v29 = StringVar()
v30 = StringVar()
v31 = StringVar()
v32 = StringVar()
v33 = StringVar()
v34 = StringVar()

Label(master, background="SkyBlue3", text="Problem 1").grid(row=1, column=2)
Label(master, background="SkyBlue3", text="a1").grid(row=2,column=1)
e1= Entry(master, textvariable=v1)
e1.grid(row=2, column=2)
Label(master, background="SkyBlue3", text="b1").grid(row=2,column=3)
e2= Entry(master, textvariable=v2)
e2.grid(row=2, column=4)
Label(master, background="SkyBlue3", text="c1").grid(row=2,column=5)
e3= Entry(master, textvariable=v3)
e3.grid(row=2, column=6)
Label(master, background="SkyBlue3", text="d1").grid(row=2,column=7)
e4= Entry(master, textvariable=v4)
e4.grid(row=2, column=8)
##########
Label(master, background="SkyBlue3", text="Problem 2").grid(row=3, column=2)
Label(master, background="SkyBlue3", text="a2a").grid(row=4, column=1)
e5= Entry(master, textvariable=v5)
e5.grid(row=4, column=2)
Label(master, background="SkyBlue3", text="a2b").grid(row=4, column=3)
e6= Entry(master, textvariable=v6)
e6.grid(row=4, column=4)
Label(master, background="SkyBlue3", text="a2c").grid(row=4, column=5)
e7= Entry(master, textvariable=v7)
e7.grid(row=4, column=6)
Label(master, background="SkyBlue3", text="a2d").grid(row=4, column=7)
e8= Entry(master, textvariable=v8)
e8.grid(row=4, column=8)
Label(master, background="SkyBlue3", text="b2a").grid(row=5, column=1)
e9= Entry(master, textvariable=v9)
e9.grid(row=5, column=2)
Label(master, background="SkyBlue3", text="b2b").grid(row=5, column=3)
e10= Entry(master, textvariable=v10)
e10.grid(row=5, column=4)
Label(master, background="SkyBlue3", text="c2a").grid(row=5, column=5)
e11= Entry(master, textvariable=v11)
e11.grid(row=5, column=6)
Label(master, background="SkyBlue3", text="c2b").grid(row=5, column=7)
e12= Entry(master, textvariable=v12)
e12.grid(row=5, column=8)
Label(master, background="SkyBlue3", text="d2").grid(row=6, column=1)
e13= Entry(master, textvariable=v13)
e13.grid(row=6, column=2)
#############
Label(master, background="SkyBlue3", text="Problem 3").grid(row=7, column=2)
Label(master, background="SkyBlue3", text="a3a").grid(row=8, column=1)
e14= Entry(master, textvariable=v14)
e14.grid(row=8, column=2)
Label(master, background="SkyBlue3", text="a3b").grid(row=8, column=3)
e15= Entry(master, textvariable=v15)
e15.grid(row=8, column=4)
Label(master, background="SkyBlue3", text="a3c").grid(row=8, column=5)
e16= Entry(master, textvariable=v16)
e16.grid(row=8, column=6)
Label(master, background="SkyBlue3", text="a3d").grid(row=8, column=7)
e17= Entry(master, textvariable=v17)
e17.grid(row=8, column=8)
Label(master, background="SkyBlue3", text="b3a").grid(row=9, column=1)
e18= Entry(master, textvariable=v18)
e18.grid(row=9, column=2)
Label(master, background="SkyBlue3", text="b3b").grid(row=9, column=3)
e19= Entry(master, textvariable=v19)
e19.grid(row=9, column=4)
Label(master, background="SkyBlue3", text="c3a").grid(row=9, column=5)
e20= Entry(master, textvariable=v20)
e20.grid(row=9, column=6)
Label(master, background="SkyBlue3", text="c3b").grid(row=9, column=7)
e21= Entry(master, textvariable=v21)
e21.grid(row=9, column=8)
Label(master, background="SkyBlue3", text="d3").grid(row=10, column=1)
e22= Entry(master, textvariable=v22)
e22.grid(row=10, column=2)
##########
Label(master, background="SkyBlue3", text="Problem 4").grid(row=11, column=2)
Label(master, background="SkyBlue3", text="a4a").grid(row=12, column=1)
e23= Entry(master, textvariable=v23)
e23.grid(row=12, column=2)
Label(master, background="SkyBlue3", text="a4b").grid(row=12, column=3)
e24= Entry(master, textvariable=v24)
e24.grid(row=12, column=4)
Label(master, background="SkyBlue3", text="a4c").grid(row=12, column=5)
e25= Entry(master, textvariable=v25)
e25.grid(row=12, column=6)
Label(master, background="SkyBlue3", text="a4d").grid(row=12, column=7)
e26= Entry(master, textvariable=v26)
e26.grid(row=12, column=8)
Label(master, background="SkyBlue3", text="b4a").grid(row=13, column=1)
e27= Entry(master, textvariable=v27)
e27.grid(row=13, column=2)
Label(master, background="SkyBlue3", text="b4b").grid(row=13, column=3)
e28= Entry(master, textvariable=v28)
e28.grid(row=13, column=4)
Label(master, background="SkyBlue3", text="c4a").grid(row=13, column=5)
e29= Entry(master, textvariable=v29)
e29.grid(row=13, column=6)
Label(master, background="SkyBlue3", text="c4b").grid(row=13, column=7)
e30= Entry(master, textvariable=v30)
e30.grid(row=13, column=8)
Label(master, background="SkyBlue3", text="c4c").grid(row=14, column=1)
e31= Entry(master, textvariable=v31)
e31.grid(row=14, column=2)
Label(master, background="SkyBlue3", text="c4d").grid(row=14, column=3)
e32= Entry(master, textvariable=v32)
e32.grid(row=14, column=4)
Label(master, background="SkyBlue3", text="d4a").grid(row=14, column=5)
e33= Entry(master, textvariable=v33)
e33.grid(row=14, column=6)
Label(master, background="SkyBlue3", text="d4b").grid(row=14, column=7)
e34= Entry(master, textvariable=v34)
e34.grid(row=14, column=8)
texto1 = StringVar()
texto2 = StringVar()
texto3 = StringVar()
Label(master, background="SkyBlue3", textvariable=texto1).grid(row=15, column=3)
Label(master, background="SkyBlue3", textvariable=texto2).grid(row=15, column=4)
Label(master, background="SkyBlue3", textvariable=texto3).grid(row=15, column=5)


Label(master, background="SkyBlue3", font=(None, 15), text="State Space").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate" , command=lambda: StateSpace(v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get(), v8.get(), v9.get(), v10.get(), v11.get(), v12.get(), v13.get(), v14.get(), v15.get(), v16.get(), v17.get(), v18.get(), v19.get(), v20.get(), v21.get(), v22.get(), v23.get(), v24.get(), v25.get(), v26.get(), v27.get(), v28.get(), v29.get(), v30.get(), v31.get(), v32.get(), v33.get(), v34.get())).grid(row=5)
master.mainloop()
