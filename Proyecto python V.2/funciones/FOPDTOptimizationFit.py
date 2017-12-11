#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk
from scipy.optimize import minimize
from scipy.interpolate import interp1d


class val():
    def __init__(self,ns, to, tf, n1, kp1, taup1):
        self.ns = ns
        self.to = to
        self.tf = tf
        self.n1 = n1
        self.kp1 = kp1
        self.taup1 = taup1

def PedirDatos(ns, to, tf, n1, kp1, taup1):
    ns = int(ns)
    to = int(to)
    tf = int(tf)
    n1 = int(n1)
    kp1 = float(kp1)
    taup1 = float(taup1)
    return val(ns, to, tf, n1, kp1, taup1)
va = PedirDatos(0, 0, 0, 0, 0, 0)

# define process model (to generate process data)
def process(y,t,n,u,Kp,taup):
    # arguments
    #  y[n] = outputs
    #  t    = time
    #  n    = order of the system
    #  u    = input value
    #  Kp   = process gain
    #  taup = process time constant

    # equations for higher order system
    dydt = np.zeros(n)
    # calculate derivative
    dydt[0] = (-y[0] + Kp * u)/(taup/n)
    for i in range(1,n):
       dydt[i] = (-y[i] + y[i-1])/(taup/n)
    return dydt

# use this function or replace yp with real process data
def sim_process_data(n1, kp1, taup1, ns, delta_t, u):
    # higher order process
    n=n1       # order
    Kp=kp1    # gain
    taup=taup1   # time constant
    # storage for predictions or data
    yp = np.zeros(ns+1)  # process
    for i in range(1,ns+1):
        if i==1:
            yp0 = np.zeros(n)
        ts = [delta_t*(i-1),delta_t*i]
        y = odeint(process,yp0,ts,args=(n,u[i],Kp,taup))
        yp0 = y[-1]
        yp[i] = y[1][n-1]
    return yp

def Generate_Simulated_Data_from_Model(ns, to, tf, n1, kp1, taup1):
    va1 = PedirDatos(ns, to, tf, n1, kp1, taup1)
    va.ns = va1.ns
    va.to = va1.to
    va.tf = va1.tf
    va.n1 = va1.n1
    va.kp1 = va1.kp1
    va.taup1 = va1.taup1

    # specify number of steps
    ns = va.ns
    # define time points
    t = np.linspace(va.to,va.tf,ns+1)
    delta_t = t[1]-t[0]
    # define input vector
    u = np.zeros(ns+1)
    u[5:20] = 1.0
    u[20:30] = 0.1
    u[30:] = 0.5
    # Construct results and save data file
    # Column 1 = time
    # Column 2 = input
    # Column 3 = output
    yp = sim_process_data(va.n1, va.kp1, va.taup1, va.ns, delta_t, u)
    data = np.vstack((t,u,yp)) # vertical stack
    data = data.T              # transpose data
    np.savetxt('data.txt',data,delimiter=',')

    # plot results
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(t,yp,'kx-',linewidth=2,label='Output')
    plt.ylabel('Output Data')
    plt.legend(loc='best')
    plt.subplot(2,1,2)
    plt.plot(t,u,'bx-',linewidth=2)
    plt.legend(['Input'],loc='best')
    plt.ylabel('Input Data')
    plt.show()

imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/FOPDTOptimizationFit.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("Generate Simulated Data from Model")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lableconstant (2) dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, background="SkyBlue3", text="steps").grid(row=2)
Label(master, background="SkyBlue3", text="start time").grid(row=3)
Label(master, background="SkyBlue3", text="final time").grid(row=4)
Label(master, background="SkyBlue3", text="order (n)").grid(row=5)
Label(master, background="SkyBlue3", text="gain (kp)").grid(row=6)
Label(master, background="SkyBlue3", text="time constant (taup)").grid(row=7)
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

Label(master, background="SkyBlue3", font=(None, 15), text="FOPDT Optimization Fit").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate" , command=lambda: Generate_Simulated_Data_from_Model(v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get())).grid(row=8)
master.mainloop()
