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
def cerrar():
    master.destroy()

combo = ttk.Combobox(master, state="readonly")
combo.grid(row=0, column=0)
combo['values']= ('SOPDT_Fit_to_Data', 'SOPDT_Generate_Simulated_Data_from_Model')
combo.current(0)

master.geometry("350x200+10+10")
tk.Button(master, text="Execute", command=lambda: Ejecutar()).grid(row=0, column=2)
tk.Button(master, text="Back", command=lambda: cerrar()).grid(row=0, column=3)
tk.mainloop()
