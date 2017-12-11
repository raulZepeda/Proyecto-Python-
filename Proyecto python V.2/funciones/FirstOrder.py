#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import os
import time
def Ejecutar():
    funcion()
    os.system('python ~/Documentos/Otros/Proyecto/funciones/'+combo.get()+'.py')
    funcion2()

def funcion():
    master.withdraw()
def funcion2():
    master.deiconify()
master = tk.Tk()
master.configure(background="SkyBlue3")
master.configure(background="SkyBlue3")
def cerrar():
    master.destroy()

combo = ttk.Combobox(master, state="readonly")
combo.grid(row=0, column=0)
combo['values']= ('TimeDelay', 'FOPDTGraphicalFit', 'FOPDTOptimizationFit')
combo.current(0)

master.geometry("350x200+10+10")
tk.Button(master, background="DodgerBlue2", text="Execute", command=lambda: Ejecutar()).grid(row=0, column=2)
tk.Button(master, background="DodgerBlue2", text="Back", command=lambda: cerrar()).grid(row=0, column=3)
tk.mainloop()
