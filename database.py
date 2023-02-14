from tkinter import *
import sqlite3
from classes import reservation
from classes import movie

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
def insert(order_ID, lastName, firstName, hall, chair):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()
    c.execute("INSERT or REPLACE INTO reservations VALUES (NULL,:orderID, :last_Name, :first_Name, :hall, :chair)",
        {
            'orderID': int(order_ID),
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
    c.execute("SELECT * FROM reservations WHERE orderID=" + str(orderID))
    records = c.fetchall()
    actual = reservation(records[0][0], records[0][1], records[0][2], records[0][3], records[0][4], records[0][5])
    resList.append(actual) 
    return resList

#Filmadatok lekérdezése
def selectMovie(id):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT * FROM halls WHERE ID=" + str(id))
    records = c.fetchall()
    actual = movie(records[0][0], records[0][1], records[0][2], records[0][3], records[0][4], records[0][5])
    moveiesList.append(actual)
    return actual

#Leszámolás
def count(hallId):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT COUNT(*) FROM reservations WHERE hall =" + str(hallId))
    numberOfRows = c.fetchone()[0]
    return numberOfRows