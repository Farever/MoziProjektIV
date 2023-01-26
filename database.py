from tkinter import *
import sqlite3

#Foglalás törlése
def delete(orderID):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()
    c.execute("DELETE FROM reservations WHERE ID= "+ str(orderID))
    conn.commit()
    conn.close()

#Foglalás hozzáadása
def insert(lastName, firstName, hall, chair):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()
    c.execute("INSERT or REPLACE INTO reservations VALUES (NULL, :last_Name, :first_Name, :hall, :chair)",
        {
            'last_Name':str(lastName),
            'first_Name': str(firstName),
            'hall': int(hall),
            'chair': int(chair),
        }
    )
    conn.commit()
    conn.close()

#Update szerintem nem kell ehhez a projekthez

#Foglalás lekérdezés
def select(orderID):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT * FROM reservations WHERE ID=" + str(orderID))
    records = c.fetchall()
    print(records[0][1]) #A lekérdezetett foglalás 2.recordja (last_Name)

insert("Példa", "János" , 1 , 15)
select(1)