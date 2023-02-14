from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image
import database
from classes import movie

movies = []
for i in range(4):
    movie = database.selectMovie(i+1)
    movies.append(movie)

root = ttk.Window(themename="darkly")

Meter1 = ttk.Meter(bootstyle="primary", subtextstyle="secondary", amounttotal = movies[0].chairs, amountused = database.count(1), subtext= "Foglalt helyek")
Meter1.pack()

Meter2 = ttk.Meter(bootstyle="primary", subtextstyle="secondary", amounttotal = movies[1].chairs, amountused = database.count(2), subtext= "Foglalt helyek")
Meter2.pack()

Meter3 = ttk.Meter(bootstyle="primary", subtextstyle="secondary", amounttotal = movies[2].chairs, amountused = database.count(3), subtext= "Foglalt helyek")
Meter3.pack()

Meter4 = ttk.Meter(bootstyle="primary", subtextstyle="secondary", amounttotal = movies[3].chairs, amountused = database.count(4), subtext= "Foglalt helyek")
Meter4.pack()

root.mainloop()