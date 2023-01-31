import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image  

#Adatbázis import
import database
movie = database.selectMovie(1) #ID --> terem szám

root = tk.Tk()
root.resizable(False, False)
#Plakát
imgname = "images/" + str(movie.hall)+".jpg"
image = Image.open(imgname)
image = image.resize((int(image.size[0]*0.75), int(image.size[1]*0.75)))
imgObj = ImageTk.PhotoImage(image)

img_lab = tk.Label(image=imgObj)
img_lab.grid(column=0, row=0, columnspan=2)

#Title
title_lab = ttk.Label(root, text= movie.title, font=('helvetica', 24))
title_lab.grid(column=0, row=1, columnspan=2, ipady=10)

#Date
date_lab1 = ttk.Label(root, text="Megjelenés éve: ", font=('helvetica', 12))
date_lab1.grid(column=0, row=2 , ipady=5)
date_lab2 = ttk.Label(root, text= movie.date, font=('helvetica', 12))
date_lab2.grid(column=1, row=2 , ipady=5)

#Genre
genre_lab1 = ttk.Label(root, text="Műfaj: ", font=('helvetica', 12))
genre_lab1.grid(column=0, row=3 , ipady=5)
genre_lab2 = ttk.Label(root,text= movie.genre, font=('helvetica', 12))
genre_lab2.grid(column=1, row=3 , ipady=5)

#Playtime
time_lab1 = ttk.Label(root, text="Játékidő: ", font=('helvetica', 12))
time_lab1.grid(column=0, row=4 , ipady=5)
time_lab2 = ttk.Label(root,text= movie.playtime, font=('helvetica', 12))
time_lab2.grid(column=1, row=4 , ipady=5)

#Foglalás
btn = ttk.Button(root, bootstyle="info", text="Jegy foglalás")
btn.grid(column=0, row=5, columnspan=2 , ipady=5)

root.mainloop()