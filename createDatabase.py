import sqlite3
#Adatbázis létrehozása: egyszer kell lefuttatni!

#1. lépés: kapcsolódás adatbázishoz (sqlite3)
conn = sqlite3.connect("moziProjekt.db")

#2. lépés: Létrehozunk egy úgynevezett "kurzort". Ez a kurzor felelős azért, hogy a parancsainkat az sqlite feldolgozza és végrehajtsa
c = conn.cursor()

#3. lépés: végrehajtjuk a parancsot (itt tábla létrehozása először az attribútum nevével, majd a típusával)
c.execute(""" CREATE TABLE halls (
    ID integer PRIMARY KEY,
    chairs integer,
    movie_Title text,
    movie_Date text,
    movie_Genre text,
    movie_PlayTime text
    
 )""")


c.execute(""" CREATE TABLE reservations (
    ID integer PRIMARY KEY AUTOINCREMENT,
    orderID integer,
    last_Name text NOT NULL,
    first_Name text NOT NULL,
    hall integer,
    chair integer,
    FOREIGN KEY (hall) REFERENCES halls (id)
    
 )""")

with open("movies.txt", "r",encoding = 'utf-8') as f:
    for line in f:
        Id, Chairs, Title, Date, Genre, PlayTime = line.strip().split("&")
        c.execute("INSERT INTO halls VALUES (:ID, :chairs, :movie_Title, :movie_Date, :movie_Genre, :movie_PlayTime)",
        {
            'ID': int(Id),
            'chairs':int(Chairs),
            'movie_Title':Title,
            'movie_Date': Date,
            'movie_Genre': Genre,
            'movie_PlayTime' : PlayTime
        }
        )

#4. lépés Kommitoljuk a lépést (alkalmazzuk)
conn.commit()

#5. lépés: lezárjuk a kapcsolatot
conn.close()