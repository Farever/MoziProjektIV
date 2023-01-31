from tkinter import *
from ttkbootstrap import *
import math

root = Tk()

chairs = []
sor = []

ferohely = 43

foglaltak = []
windowWidth = math.floor((ferohely / 5) * 100)

root.geometry(f'{windowWidth}x500')

for i in range(ferohely + 1):
    chairs.append(0)

with open("chairs.txt", encoding="utf8") as file:
    for i in file:
        sor = i.strip().split(";")
        foglaltak.append(int(sor[0]))

for i in range(len(foglaltak)):
    chairs[foglaltak[i]] = 1

def foglalas():
    print("foglal")

def buttonStructure():
    sor = 0
    oszlop = 0
    for i in range(1, ferohely +1):

        if(i % 5 == 1 and i != 1):
            sor += 1
            oszlop = 0
        
        #print(chairs[i])
        if(chairs[i] == 1):    
            btn = Button(root, text = i, bootstyle="danger",  width = 10,)
            btn.grid(row = sor, column= oszlop,  padx= 2, pady= 2)
            oszlop += 1
        
        else:
            btn = Button(root, text = i, bootstyle="success", command= foglalas, state="on", width = 10)
            btn.grid(row = sor, column= oszlop,padx= 2, pady= 2)
            oszlop += 1

        
            

buttonStructure()


root.mainloop()