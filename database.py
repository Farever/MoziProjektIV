from tkinter import *
import sqlite3
from reservationClass import reservation
from movieClass import movie

resList = []
moveiesList = []

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

#Foglalás lekérdezés
def selectReservation(orderID):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT * FROM reservations WHERE ID=" + str(orderID))
    records = c.fetchall()
    actual = reservation(records[0][0], records[0][1], records[0][2], records[0][3], records[0][4])
    resList.append(actual)

#Filmadatok lekérdezése
def selectMovie(id):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT * FROM halls WHERE ID=" + str(id))
    records = c.fetchall()
    actual = movie(records[0][0], records[0][1], records[0][2], records[0][3], records[0][4], records[0][5])
    moveiesList.append(actual)
    print(moveiesList[0].title)