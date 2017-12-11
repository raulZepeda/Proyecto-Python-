#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk

class val():
    def __init__(self,y0, t, uo, uf):
        self.y0 = y0
        self.t = t
        self.uo = uo
        self.uf = uf

def PedirDatos(y0, t, uo, uf):
    y0 = float(y0)
    t = int(t)
    uo = int(uo)
    uf = int(uf)
    return val(y0, t, uo, uf)
va = PedirDatos(0, 0, 0, 0)

def model(y,t1):
    # u steps from 0 to 2 at t=10
    if t1<va.t:
        u = va.uo
    else:
        u = va.uf
    dydt = (-y + u)/5.0
    return dydt

def SWODIENT_Problema_2(y0, t, uo, uf):
    va1 = PedirDatos(y0, t, uo, uf)
    va.y0 = va1.y0
    va.t= va1.t
    va.uo = va1.uo
    va.uf =va1.uf
    # initial condition
    y0 = va.y0

    # time points
    t = np.linspace(0,40,1000)

    # solve ODE
    y = odeint(model,y0,t)

    # plot results
    plt.plot(t,y,'r-',label='Output (y(t))')
    plt.plot([0,10,10,40],[0,0,2,2],'b-',label='Input (u(t))')
    plt.ylabel('values')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()

imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/SWODIENT_Problema_2.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("SWODIENT Problema 2")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, background="SkyBlue3", text="initial condition (y0)").grid(row=2)
Label(master, background="SkyBlue3", text="at time").grid(row=3)
Label(master, background="SkyBlue3", text="from u").grid(row=4)
Label(master, background="SkyBlue3", text="to u").grid(row=5)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()

e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)
e4 = Entry(master, textvariable=v4)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)
e4.grid(row=5, column=1)

Label(master, background="SkyBlue3", font=(None, 15), text="Solve With ODEINT").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate" , command=lambda: SWODIENT_Problema_2(v1.get(), v2.get(), v3.get(), v4.get())).grid(row=6)

master.mainloop()
