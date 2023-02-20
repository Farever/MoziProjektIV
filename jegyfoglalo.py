from tkinter import *
import ttkbootstrap as ttk
import database
import math as math

from classes import reservation
from classes import movie

root = Tk()
style = ttk.Style("darkly")

orderID = 1
chairs = []
sor = []

ferohely = database.selectMovie(1).chairs

ujfoglalas = []

seats = []

foglaltak = database.reservedseats(1)

lbl_foglalasKiiras = ttk.Label(root, bootstyle="warning", text ="Foglalások: ")
#lbl_foglalasFrame = Labelframe(root, bootstyle="success", text="Foglalások aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", height=50)
lbl_foglalasKiiras.grid(column= 0, row = 15, columnspan= 5)
#lbl_foglalasFrame.grid(column= 0, row = 15, columnspan= 5)


for i in range(ferohely + 1):
    chairs.append(0)

#with open("chairs.txt", encoding="utf8") as file:
#   for i in file:
#        sor = i.strip().split(";")
#        foglaltak.append(int(sor[0]))

for i in range(len(foglaltak)):
    chairs[foglaltak[i]] = 1

def foglalasLista(szekszam, button):
    
    if(chairs[szekszam] == 0):
        print("foglal" + str(szekszam))
        ujfoglalas.append(szekszam)
        lbl_foglalasKiiras["text"] = lbl_foglalasKiiras["text"] + str(szekszam) + "; "
        chairs[szekszam] = 1
        button= "warning"
    
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
#
        for i in ujfoglalas:
            lbl_foglalasKiiras["text"] += str(i) + "; "
                
        button= "success"

def foglalasAdatbazis():
    for i in range(len(ujfoglalas)):
        database.insert(1111, ent_Vezeteknev.get(), ent_Keresztnev.get(), 1, ujfoglalas[i])
    orderID += 1
    ujfoglalas.clear()
    lbl_foglalasKiiras["text"] = "Foglalások: "
    top.destroy()
    buttonStructure()

    

def nevAblak():
    global ent_Keresztnev
    global ent_Vezeteknev
    global top
    top = ttk.Toplevel()
    
    top.geometry("400x200")

    lbl_visszaigazolas = ttk.Label(top, text= "Foglalás", font=("Arial", 25))
    lbl_Vezeteknev = ttk.Label(top, text ="Kérem írja be a Vezeték nevét! ", font=("Arial", 10), bootstyle ="info")
    lbl_Keresztnev = ttk.Label(top, text ="Kérem írja be a Kereszt nevét! ", font=("Arial", 10), bootstyle ="info")
    ent_Vezeteknev = ttk.Entry(top, bootstyle="primary", width= 50)
    ent_Keresztnev = ttk.Entry(top, bootstyle="primary", width= 50)
    btn_foglalas = ttk.Button(top, bootstyle = "info", text=" Foglalás", command=foglalasAdatbazis)


    lbl_visszaigazolas.grid(row= 1, column= 1, columnspan= 4,pady= 2)
    lbl_Vezeteknev.grid(row=2, column=1, pady= 2)
    ent_Vezeteknev.grid(row= 3, column= 1, columnspan= 4, pady= 2)
    
    lbl_Keresztnev.grid(row=4, column=1, pady= 2)
    ent_Keresztnev.grid(row= 5, column=1 , pady= 2, columnspan= 4)
    btn_foglalas.grid(row= 6, column= 4, pady= 2)




def buttonStructure():
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
            btn = ttk.Button(root, text = i, bootstyle="success",command= lambda seat_number = i:foglalasLista(seat_number, btn.config("bootstyle")), state="on", width = 10)
            btn.grid(row = sor, column= oszlop,padx= 2, pady= 2)
            oszlop += 1
                
        else:   
            btn = ttk.Button(root, text = i, bootstyle="danger",  width = 10,)
            btn.grid(row = sor, column= oszlop,  padx= 2, pady= 2)
            oszlop += 1

        if(i == ferohely):
            btn_foglalo = ttk.Button(root, bootstyle="primary", text = "Foglalás", width = 10, command= nevAblak)
            btn_foglalo.grid(row= sor + 1, column= oszlop + 1)

buttonStructure()


root.mainloop()