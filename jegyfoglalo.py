from tkinter import *
import ttkbootstrap as ttk
import math

root = Tk()

chairs = []
sor = []

ferohely = 43

ujfoglalas = []

seats = []
#
foglaltak = []
windowWidth = math.floor((ferohely / 5) * 100)

root.geometry(f'{windowWidth}x500')

lbl_foglalasKiiras = ttk.Label(root, bootstyle="primary", text ="Foglalások: ")
#lbl_foglalasFrame = Labelframe(root, bootstyle="success", text="Foglalások aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", height=50)
lbl_foglalasKiiras.grid(column= 0, row = 15, columnspan= 5)
#lbl_foglalasFrame.grid(column= 0, row = 15, columnspan= 5)


for i in range(ferohely + 1):
    chairs.append(0)

with open("chairs.txt", encoding="utf8") as file:
    for i in file:
        sor = i.strip().split(";")
        foglaltak.append(int(sor[0]))

for i in range(len(foglaltak)):
    chairs[foglaltak[i]] = 1

def foglalas(szekszam, button):
    
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



def buttonStructure():
    sor = 0
    oszlop = 0
    for i in range(1, ferohely +1):

        if(i % 5 == 1 and i != 1):
            sor += 1
            oszlop = 0
        
        #print(chairs[i])
        if(chairs[i] == 0):    
            btn = ttk.Button(root, text = i, bootstyle="success", command= lambda seat_number = i:foglalas(seat_number, btn.config("bootstyle")), state="on", width = 10)
            btn.grid(row = sor, column= oszlop,padx= 2, pady= 2)
            oszlop += 1
                
        else:   
            btn = ttk.Button(root, text = i, bootstyle="danger",  width = 10,)
            btn.grid(row = sor, column= oszlop,  padx= 2, pady= 2)
            oszlop += 1
        
        

        
            

buttonStructure()


root.mainloop()