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


x=0

class val():
    def __init__(self, km, taum, thetam):
        self.km = km
        self.taum = taum
        self.thetam = thetam

def PedirDatos(km, taum, thetam):
    km = float(km)
    taum = float(taum)
    thetam = float(thetam)
    return val(km, taum, thetam)
va = PedirDatos(0, 0, 0)


# define first-order plus dead-time approximation
def fopdt(y,t,uf,Km,taum,thetam,u0,yp,yp0):
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
        um = u0
    # calculate derivative
    dydt = (-(y-yp0) + Km * (um-u0))/taum
    return dydt

# simulate FOPDT model with x=[Km,taum,thetam]
def sim_model(x,ns,yp0, t, uf,u0,yp):
    # input arguments
    Km = x[0]
    taum = x[1]
    thetam = x[2]
    # storage for model values
    ym = np.zeros(ns)  # model
    # initial condition
    ym[0] = yp0
    # loop through time steps
    for i in range(0,ns-1):
        ts = [t[i],t[i+1]]
        y1 = odeint(fopdt,ym[i],ts,args=(uf,Km,taum,thetam,u0,yp,yp0))
        ym[i+1] = y1[-1]
    return ym

# define objective
def objective(x,ns,yp0, t, uf,u0,yp):
    # simulate model
    ym = sim_model(x,ns,yp0, t, uf,u0,yp)
    # calculate objective
    obj = 0.0
    for i in range(len(ym)):
        obj = obj + (ym[i]-yp[i])**2
    # return result
    return obj

def FOPDT_Fit_to_Data(km, taum, thetam):
    texto11.set('Graphing... wait please..')

    # Import CSV data file
    # Column 1 = time (t)
    # Column 2 = input (u)
    # Column 3 = output (yp)
    data = np.loadtxt('data.txt',delimiter=',')
    u0 = data[0,1]
    yp0 = data[0,2]
    t = data[:,0].T - data[0,0]
    u = data[:,1].T
    yp = data[:,2].T

    # specify number of steps
    ns = len(t)
    delta_t = t[1]-t[0]
    # create linear interpolation of the u data versus time
    uf = interp1d(t,u)



    # initial guesses
    x0 = np.zeros(3)
    x0[0] = 2.0 # Km
    x0[1] = 3.0 # taum
    x0[2] = 0.0 # thetam

    # show initial objective
    texto6.set('Initial SSE Objective: ' + str(objective(x0,ns,yp0, t, uf,u0,yp)))

    # optimize Km, taum, thetam
    solution = minimize(objective,x0)

    # Another way to solve: with bounds on variables
    #bnds = ((0.4, 0.6), (1.0, 10.0), (0.0, 30.0))
    #solution = minimize(objective,x0,bounds=bnds,method='SLSQP')
    x = solution.x

    # show final objective
    texto7.set('Final SSE Objective: ' + str(objective(x,ns,yp0, t, uf,u0,yp)))

    texto8.set('Kp: ' + str(x[0]))
    texto9.set('taup: ' + str(x[1]))
    texto10.set('thetap: ' + str(x[2]))

    # calculate model with updated parameters
    ym1 = sim_model(x0,ns,yp0, t, uf,u0,yp)
    ym2 = sim_model(x,ns,yp0, t, uf,u0,yp)
    # plot results
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(t,yp,'kx-',linewidth=2,label='Process Data')
    plt.plot(t,ym1,'b-',linewidth=2,label='Initial Guess')
    plt.plot(t,ym2,'r--',linewidth=3,label='Optimized FOPDT')
    plt.ylabel('Output')
    plt.legend(loc='best')
    plt.subplot(2,1,2)
    plt.plot(t,u,'bx-',linewidth=2)
    plt.plot(t,uf(t),'r--',linewidth=3)
    plt.legend(['Measured','Interpolated'],loc='best')
    plt.ylabel('Input Data')
    texto11.set('')
    plt.show()




imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/FOPDTOptimizationFit.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
# titulo de la ventana
master.title("FOPDT Fit to Data")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, text="kp").grid(row=1)
Label(master, text="taup").grid(row=2)
Label(master, text="thetap").grid(row=3)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)


texto6 = StringVar()
texto7 = StringVar()
texto8 = StringVar()
texto9 = StringVar()
texto10 = StringVar()
texto11 = StringVar()
Label(master, textvariable=texto6).grid(row=6)
Label(master, textvariable=texto7).grid(row=7)
Label(master, textvariable=texto8).grid(row=8)
Label(master, textvariable=texto9).grid(row=9)
Label(master, textvariable=texto10).grid(row=10)
Label(master, textvariable=texto11).grid(row=6, column=1)

Button(master, text="Calculate", command=lambda: FOPDT_Fit_to_Data(v1.get(), v2.get(), v3.get())).grid(row=5)
master.mainloop()
