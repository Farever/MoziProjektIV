from tkinter import *
import sqlite3

from classes import reservation
from classes import movie

resList = []
moveiesList = []
seatsList = []

#Foglalás törlése
def delete(orderID):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()
    c.execute("DELETE FROM reservations WHERE orderID= "+ str(orderID))
    conn.commit()
    conn.close()

#Foglalás hozzáadása
def insert(order_ID, lastName, firstName, hall, chair):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()
    c.execute("begin")
    try:
        c.execute("INSERT INTO reservations VALUES (NULL,:orderID, :last_Name, :first_Name, :hall, :chair)",
            {
                'orderID': int(order_ID),
                'last_Name':str(lastName),
                'first_Name': str(firstName),
                'hall': int(hall),
                'chair': int(chair),
            }
        )
        conn.commit()
    except sqlite3.Error:
        print("failed!")
        c.execute("rollback")
    conn.close()

#Foglalás lekérdezés
def selectReservation(orderID):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT * FROM reservations WHERE orderID=" + str(orderID))
    records = c.fetchall()
    for record in records:
        actual = reservation(record[0], record[1], record[2], record[3], record[4], record[5])
        resList.append(actual)
    return resList

#legnagyobb orderID megkeresése
def getMaxOrderID():
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT MAX(orderID) FROM reservations")
    maxID = c.fetchone()
    return maxID[0]

#Filmadatok lekérdezése
def selectMovie(id):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT * FROM halls WHERE ID=" + str(id))
    records = c.fetchall()
    actual = movie(records[0][0], records[0][1], records[0][2], records[0][3], records[0][4], records[0][5])
    return actual

#Leszámolás
def count(hallId):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT COUNT(*) FROM reservations WHERE hall =" + str(hallId))
    numberOfRows = c.fetchone()[0]
    return numberOfRows

#Foglalt székek listája
def reservedseats(hallId):
    conn = sqlite3.connect("moziProjekt.db")
    c = conn.cursor()   
    c.execute("SELECT * FROM reservations WHERE reservations.hall =" + str(hallId))
    records = c.fetchall()
    for i in range(len(records)):
        actual = reservation(records[i][0], records[i][1], records[i][2], records[i][3], records[i][4], records[i][5])
        seatsList.append(actual.chair)
    return seatsList
