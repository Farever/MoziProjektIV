from tkinter import *
import ttkbootstrap as ttk
import database as database
import math as math

def rDeleteWindow():
    global top
    top = Toplevel()
    
    lbl_cim = ttk.Label(top, text="Foglalások törlése", font=("Times 18"))
    lbl_torles = ttk.Label(top, text="Írja be a foglalás azonosítóját:", font=("Times 15"), bootstyle = "")
    lbl_cim.grid(row= 0, column= 1, columnspan= 3)
    lbl_torles.grid(row= 1, column= 1)

    spr_torles = ttk.Separator(bootstyle="info")
    spr_torles.grid(row=2, column=0, columnspan= 4)

    ent_torles = ttk.Entry(top, bootstyle="info", )
    ent_torles.grid(row= 3, column= 1, columnspan= 3)
    
    btn_torles= ttk.Button(top, bootstyle = "danger", text = "Törlés", command= lambda: deleter(ent_torles.get()))
    btn_torles.grid(row=4, column=5)

def deleter(id):
    database.delete(id)
    top.destroy()


