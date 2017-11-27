#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk


class val():
    def __init__(self,x0, y0, to, tf, c1, c2):
        self.x0 = x0
        self.y0 = y0
        self.to = to
        self.tf = tf
        self.c1 = c1
        self.c2 = c2

def PedirDatos(x0, y0, to, tf, c1, c2):
    x0 = int(x0)
    y0 = int(y0)
    to = int(to)
    tf = int(tf)
    c1 = int(c1)
    c2 = int(c2)
    return val(x0, y0, to, tf, c1, c2)
va = PedirDatos(0, 0, 0, 0, 0, 0)

# function that returns dz/dt
def model(z,t,u):
    x = z[0]
    y = z[1]
    dxdt = (-x + u)/2.0
    dydt = (-y + x)/5.0
    dzdt = [dxdt,dydt]
    return dzdt

def SWODIENT_Problema_4(x0, y0, to, tf, c1, c2):
    va1 = PedirDatos(x0, y0, to, tf, c1, c2)
    va.x0 = va1.x0
    va.y0 = va1.y0
    va.t0 = va1.to
    va.tf = va1.tf
    va.c1 = va1.c1
    va.c2 = va1.c2
    # initial condition
    z0 = [va.x0, va.y0]

    # number of time points
    n = (va.c2 - 1) * 10 + 1

    # time points
    t = np.linspace(0,(va.c2 - 1) * 10,n)

    # step input
    u = np.zeros(n)
    # change to 2.0 at time = 5.0
    u[ va.c2 + 1:] = va.c1

    # store solution
    x = np.empty_like(t)
    y = np.empty_like(t)
    # record initial conditions
    x[0] = z0[0]
    y[0] = z0[1]

    # solve ODE
    for i in range(1,n):
        # span for next time step
        tspan = [t[i-1],t[i]]
        # solve for next step
        z = odeint(model,z0,tspan,args=(u[i],))
        # store solution for plotting
        x[i] = z[1][0]
        y[i] = z[1][1]
        # next initial condition
        z0 = z[1]

    # plot results
    plt.plot(t,u,'g:',label='u(t)')
    plt.plot(t,x,'b-',label='x(t)')
    plt.plot(t,y,'r--',label='y(t)')
    plt.ylabel('values')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()

imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/SWODIENT_Problema_4.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
# titulo de la ventana
master.title("SWODIENT Problema 4")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, text="initial condition (x0)").grid(row=2)
Label(master, text="initial condition (y0)").grid(row=3)
Label(master, text="start time").grid(row=4)
Label(master, text="final time").grid(row=5)
Label(master, text="constant (2)").grid(row=6)
Label(master, text="constant (5)").grid(row=7)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)
e4 = Entry(master, textvariable=v4)
e5 = Entry(master, textvariable=v5)
e6 = Entry(master, textvariable=v6)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)
e4.grid(row=5, column=1)
e5.grid(row=6, column=1)
e6.grid(row=7, column=1)

Button(master, text="Calculate", command=lambda: SWODIENT_Problema_4(v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get())).grid(row=8)
master.mainloop()
