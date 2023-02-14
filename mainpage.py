from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image
import database
from classes import movie

root = ttk.Window(themename="darkly")

hallID = 1
movie = database.selectMovie(hallID)

elsoMeter = ttk.Meter(bootstyle="primary", subtextstyle="secondary", amounttotal = movie.chairs, amountused = database.count(hallID), subtext= "Foglalt helyek")
elsoMeter.pack()

root.mainloop()