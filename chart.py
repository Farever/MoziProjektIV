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

Meter1 = ttk.Meter(
    bootstyle="primary", 
    subtextstyle="secondary", 
    amounttotal = movies[0].chairs, 
    amountused = database.count(1), 
    subtext= "Foglalt helyek"
    )
Meter1.pack()

if Meter1.amountusedvar.get() >= movies[0].chairs*0.75:
    Meter1.configure(bootstyle="danger")
elif Meter1.amountusedvar.get() >= movies[0].chairs*0.5:
    Meter1.configure(bootstyle="warning")
else:
    Meter1.configure(bootstyle="primary")

root.mainloop()