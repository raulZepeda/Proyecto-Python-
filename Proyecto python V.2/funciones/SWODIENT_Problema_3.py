#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk


class val():
    def __init__(self,x0, y0, to, tf, c):
        self.x0 = x0
        self.y0 = y0
        self.to = to
        self.tf = tf
        self.c = c

def PedirDatos(x0, y0, to, tf, c):
    x0 = float(x0)
    y0 = float(y0)
    to = int(to)
    tf = int(tf)
    c = float(c)
    return val(x0, y0, to, tf, c)
va = PedirDatos(0, 0, 0, 0, 0)

# function that returns dz/dt
def model(z,t):
    dxdt = va.c * np.exp(-t)
    dydt = -z[1] + va.c
    dzdt = [dxdt,dydt]
    return dzdt
def SWODIENT_Problema_3(x0, y0, to, tf, c):
    va1 = PedirDatos(x0, y0, to, tf, c)
    va.x0 = va1.x0
    va.y0 = va1.y0
    va.t0 = va1.to
    va.tf =va1.tf
    va.c= va1.c
    # initial condition
    z0 = [va.x0,va.y0]

    # time points
    t = np.linspace(va.t0,va.tf)

    # solve ODE
    z = odeint(model,z0,t)

    # plot results
    plt.plot(t,z[:,0],'b-',label=r'$\frac{dx}{dt}='+ str(va.c) +'\; \exp(-t)$')
    plt.plot(t,z[:,1],'r--',label=r'$\frac{dy}{dt}=-y+'+ str(va.c) +'$')
    plt.ylabel('response')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()

imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/SWODIENT_Problema_3.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("SWODIENT Problema 3")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, background="SkyBlue3", text="initial condition (x0)").grid(row=2)
Label(master, background="SkyBlue3", text="initial condition (y0)").grid(row=3)
Label(master, background="SkyBlue3", text="start time").grid(row=4)
Label(master, background="SkyBlue3", text="final time").grid(row=5)
Label(master, background="SkyBlue3", text="constant (3)").grid(row=6)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)
e4 = Entry(master, textvariable=v4)
e5 = Entry(master, textvariable=v5)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)
e4.grid(row=5, column=1)
e5.grid(row=6, column=1)

Label(master, background="SkyBlue3", font=(None, 15), text="Solve With ODEINT").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate" , command=lambda: SWODIENT_Problema_3(v1.get(), v2.get(), v3.get(), v4.get(), v5.get())).grid(row=7)
master.mainloop()
