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
    def __init__(self, kp, taup, thetap):
        self.kp = kp
        self.taup = taup
        self.thetap = thetap

def PedirDatos(kp, taup, thetap):
    kp = float(kp)
    taup = float(taup)
    thetap = float(thetap)
    return val(kp, taup, thetap)
va = PedirDatos(0, 0, 0)

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

# define first-order plus dead-time approximation
def fopdt(y,t,uf,Km,taum,thetam):
    # arguments
    #  y      = output
    #  t      = time
    #  uf     = input linear function (for time shift)
    #  Km     = model gain
    #  taum   = model time constant
    #  thetam = model time constant
    # time-shift u
    try:
        if (t-thetam) <= 0:
            um = uf(0.0)
        else:
            um = uf(t-thetam)
    except:
        #print('Error with time extrapolation: ' + str(t))
        um = 0
    # calculate derivative
    dydt = (-y + Km * um)/taum
    return dydt

# specify number of steps
ns = 40
# define time points
t = np.linspace(0,16,ns+1)
delta_t = t[1]-t[0]
# define input vector
u = np.zeros(ns+1)
u[5:] = 1.0
# create linear interpolation of the u data versus time
uf = interp1d(t,u)

# use this function or replace yp with real process data
def sim_process_data():
    # higher order process
    n=10       # order
    Kp=3.0    # gain
    taup=5.0   # time constant
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
yp = sim_process_data()

# simulate FOPDT model with x=[Km,taum,thetam]
def sim_model(Km,taum,thetam):
    # input arguments
    #Km
    #taum
    #thetam
    # storage for model values
    ym = np.zeros(ns+1)  # model
    # initial condition
    ym[0] = 0
    # loop through time steps
    for i in range(1,ns+1):
        ts = [delta_t*(i-1),delta_t*i]
        y1 = odeint(fopdt,ym[i-1],ts,args=(uf,Km,taum,thetam))
        ym[i] = y1[-1]
    return ym

def FOPDTGraphicalFit(kp, taup, thetap):
    va1 = PedirDatos(kp, taup, thetap)
    va.kp = va1.kp
    va.taup = va1.taup
    va.thetap = va1.thetap
    # calculate model with updated parameters
    Km = va.kp
    taum = va.taup
    thetam = va.thetap
    ym = sim_model(Km,taum,thetam)

    # plot results
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(t,ym,'r--',linewidth=3,label='Fit FOPDT')
    plt.plot(t,yp,'kx-',linewidth=2,label='Process Data')
    plt.ylabel('Output')
    plt.legend(loc='best')
    plt.subplot(2,1,2)
    plt.plot(t,u,'bx-',linewidth=2)
    plt.plot(t,uf(t),'r--',linewidth=3)
    plt.legend(['Measured','Interpolated'],loc='best')
    plt.ylabel('Input Data')
    plt.show()


imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/FOPDTGraphicalFit.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("FOPDT Graphical Fit")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, background="SkyBlue3", text="Kp").grid(row=2)
Label(master, background="SkyBlue3", text="taup").grid(row=3)
Label(master, background="SkyBlue3", text="theta_p").grid(row=4)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)
Label(master, background="SkyBlue3", font=(None, 15), text="FOPDT Graphical Fit").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate" , command=lambda: FOPDTGraphicalFit(v1.get(), v2.get(), v3.get())).grid(row=5)
master.mainloop()
