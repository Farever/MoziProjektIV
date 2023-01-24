from tkinter import *
import sqlite3

#Foglalás törlése
def delete(orderID):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()
    c.execute("DELETE FROM reservations WHERE ID= "+ orderID)
    conn.commit()
    conn.close()

#Insert
def insert(orderID, lastName, firstName, hall, chair):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()
    c.execute("INSERT INTO reservations VALUES (:ID, :last_Name, :first_Name, :hall, :chair)",
        {
            'ID':orderID,
            'last_Name':lastName,
            'first_Name':firstName,
            'hall': hall,
            'chair': chair,
        }
    )
    conn.commit()
    conn.close()