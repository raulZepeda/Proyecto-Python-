#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk

class val():
    def __init__(self,k, tau, to, tf):
        self.k = k
        self.tau = tau
        self.to = to
        self.tf = tf

def PedirDatos(k, tau, to, tf):
    k = int(k)
    tau = float(tau)
    to = int(to)
    tf = int(tf)
    return val(k, tau, to, tf)
va = PedirDatos(0, 0, 0, 0)

def LaplaceTransforms(k, tau, to, tf):
    va1 = PedirDatos(k, tau, to, tf)
    va.k = va1.k
    va.tau = va1.tau
    va.to = va1.to
    va.tf = va1.tf
    K = va.k
    tau = va.tau
    n = va.tf * 10 + 1
    t = np.linspace(va.to, va.tf,n)
    s1 = np.zeros(n)
    s1[11:] = 1.0
    s2 = np.zeros(n)
    s2[51:] = 1.0

    y = 3*K*(1-np.exp(-(t-1)/tau))*s1 \
       -3*K*(1-np.exp(-(t-5)/tau))*s2

    plt.figure(1)
    plt.plot([0,1,1.001,5,5.001,8],[0,0,3,3,0,0],'b-',linewidth=2)
    plt.plot(t,y,'r--')
    plt.ylabel('y(t)')
    plt.xlabel('time (t)')
    plt.legend(['u(t)','y(t)'])
    plt.grid()
    plt.savefig('fig1.png')

    plt.show()


imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/LaplaceTransform.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
# titulo de la ventana
master.title("Laplace Transforms")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, text="K").grid(row=2)
Label(master, text="tau").grid(row=3)
Label(master, text="start time").grid(row=4)
Label(master, text="final time").grid(row=5)
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

Button(master, text="Calculate", command=lambda: LaplaceTransforms(v1.get(), v2.get(), v3.get(), v4.get())).grid(row=6)
master.mainloop()
