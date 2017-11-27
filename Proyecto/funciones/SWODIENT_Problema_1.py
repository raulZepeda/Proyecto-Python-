#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk

class val():
    def __init__(self,y0, to, tf):
        self.y0 = y0
        self.to = to
        self.tf = tf

def PedirDatos(y0, to, tf):
    y0 = float(y0)
    to = int(to)
    tf = int(tf)
    return val(y0, to, tf)


# function that returns dy/dt
def model(y,t):
    dydt = -y + 1.0
    return dydt

def SWODIENT_Problema_1(y0, to, tf):
    # initial condition
    va = PedirDatos(y0, to, tf)
    y0 = va.y0

    # time points
    t = np.linspace(va.to,va.tf)

    # solve ODE
    y = odeint(model,y0,t)

    # plot results
    plt.plot(t,y)
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.show()



imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/SWODIENT_Problema_1.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
# titulo de la ventana
master.title("SWODIENT Problema 1")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, text="initial condition (y0)").grid(row=2)
Label(master, text="start time").grid(row=3)
Label(master, text="final time").grid(row=4)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)

Button(master, text="Calculate", command=lambda: SWODIENT_Problema_1(v1.get(), v2.get(), v3.get())).grid(row=5)








# Mostramos la ventana
master.mainloop()
