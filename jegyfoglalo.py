from tkinter import *
import ttkbootstrap as ttk
import database
import pdfGen as pdf
import math as math
from PIL import ImageTk, Image
from classes import reservation
from classes import movie

orderID = 1

sor = []

chairs = []

ujfoglalas = []

seats = []

foglaltak = []

def foglalasLista(szekszam, button):
    
    if(chairs[szekszam] == 0):
        print("foglal" + str(szekszam))
        ujfoglalas.append(szekszam)
        lbl_foglalasKiiras["text"] = lbl_foglalasKiiras["text"] + str(szekszam) + "; "
        chairs[szekszam] = 1
        button[szekszam-1].config(bootstyle = "warning")
    
    else:
        chairs[szekszam] = 0
        label = lbl_foglalasKiiras["text"]
        DeletaionId = 0
        for i in range(len(ujfoglalas)):
            print(i)
            if(ujfoglalas[i] == szekszam):
                print("megtaláltam!!" ,ujfoglalas[i], i)
                DeletaionId = i

        ujfoglalas.pop(DeletaionId)
                
        
        lbl_foglalasKiiras["text"] = "Foglalások: "

        for i in ujfoglalas:
            lbl_foglalasKiiras["text"] += str(i) + "; "
                
        button[szekszam-1].config(bootstyle = "success")

def foglalasAdatbazis(teremszam, fogloldal, nevoldal):
    orderID = database.getMaxOrderID()
    if(orderID != None):
        orderID = int(orderID) + 1
    else:
        orderID = 1
    vezeteknev = ent_Vezeteknev.get()
    keresztnev = ent_Keresztnev.get()
    
    lbl_foglalasKiiras["text"] = "Foglalások: "
    for i in range(len(ujfoglalas)):
        foglaltak.append(ujfoglalas[i])
        database.insert(orderID, vezeteknev, keresztnev, teremszam, ujfoglalas[i])

    pdf.pdfGEN(orderID)

    ujfoglalas.clear()
    nevoldal.destroy()
    fogloldal.destroy()
    buttonStructure(teremszam)
    
    
def nevAblak(teremszam, fogloldal):
    global ent_Keresztnev
    global ent_Vezeteknev
    top = ttk.Toplevel()
    top.geometry("400x200")
    top.resizable(False, False)
    top.title("MoziTown jegyfogglalás")

    ico = Image.open('logo-color.png')
    photo = ImageTk.PhotoImage(ico)
    top.wm_iconphoto(False, photo)
    
    

    lbl_visszaigazolas = ttk.Label(top, text= "Foglalás", font=("Arial", 25))
    lbl_Vezeteknev = ttk.Label(top, text ="Kérem írja be a Vezeték nevét! ", font=("Arial", 10), bootstyle ="info")
    lbl_Keresztnev = ttk.Label(top, text ="Kérem írja be a Kereszt nevét! ", font=("Arial", 10), bootstyle ="info")
    ent_Vezeteknev = ttk.Entry(top, bootstyle="primary", width= 50)
    ent_Keresztnev = ttk.Entry(top, bootstyle="primary", width= 50)
    btn_foglalas = ttk.Button(top, bootstyle = "info", text=" Foglalás", command=lambda: foglalasAdatbazis(teremszam, fogloldal, top))


    lbl_visszaigazolas.grid(row= 1, column= 1, columnspan= 4,pady= 2)
    lbl_Vezeteknev.grid(row=2, column=1, pady= 2)
    ent_Vezeteknev.grid(row= 3, column= 1, columnspan= 4, pady= 2)
    
    lbl_Keresztnev.grid(row=4, column=1, pady= 2)
    ent_Keresztnev.grid(row= 5, column=1 , pady= 2, columnspan= 4)
    btn_foglalas.grid(row= 6, column= 4, pady= 2)




def buttonStructure(teremszam):
    top = ttk.Toplevel()

    top.resizable(False, False)
    top.title(database.selectMovie(teremszam).title + " jegyfoglalás")

    ico = Image.open('logo-color.png')
    photo = ImageTk.PhotoImage(ico)
    top.wm_iconphoto(False, photo)

    global foglaltak
    global lbl_foglalasKiiras

    lbl_foglalasKiiras = ttk.Label(top, bootstyle="warning", text ="Foglalások: ")
    lbl_foglalasKiiras.grid(column= 0, row = 15, columnspan= 5)
    Buttons = []


    foglaltak.clear()
    chairs.clear()


    ferohely = database.selectMovie(teremszam).chairs
    foglaltak = database.reservedseats(teremszam)


    for i in range(ferohely + 1):
        chairs.append(0)
    
    for i in range(len(foglaltak)):
        print(foglaltak[i] , "EZ EGY FOGLALAS")
        chairs[foglaltak[i]] = 1
    
    sor = 0
    oszlop = 0

    felsoOszlop =  ferohely - (math.floor(math.sqrt(ferohely))**2)
    
    tobbiOszlop =ferohely - felsoOszlop

    print("Urolsó oszlop ", felsoOszlop, "másik ", tobbiOszlop)

    for i in range(1, ferohely +1):
        
        if(i <= (felsoOszlop + math.sqrt(tobbiOszlop))):
            sor = 0
            print(i)

        elif((i - felsoOszlop) % math.sqrt(tobbiOszlop)  == 1 and i != 1):
            sor += 1
            oszlop = math.floor(felsoOszlop / 2)
        
        if(i == felsoOszlop + math.sqrt(tobbiOszlop) + 1):
            sor = 1
            oszlop = math.floor(felsoOszlop / 2)
        
        #print(chairs[i])
        if(chairs[i] == 0):    
            btn = ttk.Button(top, text = i, bootstyle="success",command= lambda seat_number = i:foglalasLista(seat_number, Buttons), state="on", width = 10)
            Buttons.append(btn)
            btn.grid(row = sor, column= oszlop,padx= 2, pady= 2)
            oszlop += 1
                
        else:   
            btn = ttk.Button(top, text = i, bootstyle="danger",  width = 10,)
            Buttons.append(btn)
            btn.grid(row = sor, column= oszlop,  padx= 2, pady= 2)
            oszlop += 1

        if(i == ferohely):
            btn_foglalo = ttk.Button(top, bootstyle="primary", text = "Foglalás", width = 10, command= lambda:nevAblak(teremszam, top))
            btn_foglalo.grid(row= sor + 1, column= oszlop + 1)