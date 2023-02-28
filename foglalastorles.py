from tkinter import *
import ttkbootstrap as ttk
import database as database
import math as math

def rDeleteWindow():
    top = Toplevel()
    
    lbl_cim = ttk.Label(top, text="Foglalások törlése", font=("Comic 20"))
    lbl_torles = ttk.Label(top, text="Írja be a foglalás azonosítóját:", font=("Comic 15"), bootstyle = "")
    lbl_cim.grid(row= 0, column= 1, columnspan= 3)
    lbl_torles.grid(row= 1, column= 1)

    spr_torles = ttk.Separator(bootstyle="info")
    spr_torles.grid(row=2, column=0, columnspan= 4)

    ent_torles = ttk.Entry(top, bootstyle="info", )
    ent_torles.grid(row= 3, column= 1, columnspan= 3)
    
    btn_torles= ttk.Button(top, bootstyle = "info", text = "Törlés", command= lambda: database.delete(ent_torles.get()))
    btn_torles.grid(row=4, column=5)


