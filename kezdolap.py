from tkinter import *
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap.constants import *
import database
import jegyfoglalo
from classes import movie

root = Tk()
root.geometry("1100x700")
style = ttk.Style("cosmo")

def toggle():

    if var1.get() == 1:
        style = ttk.Style("darkly")  

    else:     
        style = ttk.Style("cosmo") 


var1 = IntVar()
t1 = ttk.Checkbutton(root, variable=var1, onvalue=1, offvalue=0, command=toggle,bootstyle="light-square-toggle", text = "Éjszakai mód")
t1.grid(row=0, column=5)

movies = []
for i in range(4):
    movie = database.selectMovie(i+1)
    movies.append(movie)


#main
lbl_mozinev = ttk.Label(root, text="Mozi",font=('Times 40'))
lbl_mozinev.grid(row=1,column=1,columnspan=4)


#első negyed
img1 = ImageTk.PhotoImage(Image.open("images/1.jpg").resize((200,300)))
label_img1 = Label(root, image = img1,width=200,borderwidth=4, relief="solid")
label_img1.grid(row=2, column=1, rowspan=3)
def on_click(event=None):
    print("image clicked")
button_img1 = Button(root, image= img1, command=lambda:jegyfoglalo.buttonStructure(1))
button_img1.grid(row=2, column=1, rowspan=3)
label_leiras1 = Label(root,justify= "left", text="Cím: " + movies[0].title +"\n Játékidő: " + movies[0].playtime +"\n Műfaj: " + movies[0].genre, font=('Times 18'))
label_leiras1.grid(row=2, column=2)
button_f1 = ttk.Button(bootstyle="success-outline", text="Foglalás", command=lambda:jegyfoglalo.buttonStructure(1))
button_f1.grid(row=3,column=2)
movies = []
for i in range(4):
    movie = database.selectMovie(i+1)
    movies.append(movie)

Meter1 = ttk.Meter(
    bootstyle="primary", 
    subtextstyle="secondary", 
    amounttotal = movies[0].chairs, 
    amountused = database.count(1), 
    subtext= "Foglalt helyek",
    metersize = 150
    )
Meter1.grid(row=4,column=2)

if Meter1.amountusedvar.get() >= movies[0].chairs*0.75:
    Meter1.configure(bootstyle="danger")
elif Meter1.amountusedvar.get() >= movies[0].chairs*0.5:
    Meter1.configure(bootstyle="warning")
else:
    Meter1.configure(bootstyle="primary")

#harmadik negyed
img3 = ImageTk.PhotoImage(Image.open("images/2.jpg").resize((200,300)))
label_img3 = Label(root, image = img3,width=200,borderwidth=4, relief="solid")
label_img3.grid(row=5, column=1,rowspan=3)
def on_click3(event=None):
    print("image3 clicked")
button_img3 = Button(root, image= img3, command=lambda:jegyfoglalo.buttonStructure(3))
button_img3.grid(row=5, column=1,rowspan=3)
label_leiras3 = Label(root,justify= "left", text="Cím: " + movies[2].title +"\n Játékidő: " + movies[2].playtime +"\n Műfaj: " + movies[2].genre, font=('Times 18'))
label_leiras3.grid(row=5, column=2)
button_f3 = ttk.Button(bootstyle="success-outline", text="Foglalás", command=lambda:jegyfoglalo.buttonStructure(3))
button_f3.grid(row=6,column=2)
movies = []
for i in range(4):
    movie = database.selectMovie(i+1)
    movies.append(movie)

Meter3 = ttk.Meter(
    bootstyle="primary", 
    subtextstyle="secondary", 
    amounttotal = movies[2].chairs, 
    amountused = database.count(3), 
    subtext= "Foglalt helyek",
    metersize = 150
    )
Meter3.grid(row=7,column=2)

if Meter3.amountusedvar.get() >= movies[2].chairs*0.75:
    Meter3.configure(bootstyle="danger")
elif Meter3.amountusedvar.get() >= movies[2].chairs*0.5:
    Meter3.configure(bootstyle="warning")
else:
    Meter3.configure(bootstyle="primary")


#második negyed
img2 = ImageTk.PhotoImage(Image.open("images/3.jpg").resize((200,300)))
label_img2 = Label(root, image = img2,width=200,borderwidth=4, relief="solid")
label_img2.grid(row=2, column=3, rowspan=3)
def on_click2(event=None):
    print("image2 clicked")
button_img2 = Button(root, image= img2, command=lambda:jegyfoglalo.buttonStructure(2))
button_img2.grid(row=2, column=3,rowspan=3)
label_leiras2 = Label(root,justify= "left", text="Cím: " + movies[1].title +"\n Játékidő: " + movies[1].playtime +"\n Műfaj: " + movies[1].genre, font=('Times 18'))
label_leiras2.grid(row=2, column=4)
button_f2 = ttk.Button(bootstyle="success-outline", text="Foglalás", command=lambda:jegyfoglalo.buttonStructure(2))
button_f2.grid(row=3,column=4)
movies = []
for i in range(4):
    movie = database.selectMovie(i+1)
    movies.append(movie)

Meter2 = ttk.Meter(
    bootstyle="primary", 
    subtextstyle="secondary", 
    amounttotal = movies[1].chairs, 
    amountused = database.count(2), 
    subtext= "Foglalt helyek",
    metersize = 150
    )
Meter2.grid(row=4,column=4)

if Meter2.amountusedvar.get() >= movies[1].chairs*0.75:
    Meter2.configure(bootstyle="danger")
elif Meter2.amountusedvar.get() >= movies[1].chairs*0.5:
    Meter2.configure(bootstyle="warning")
else:
    Meter2.configure(bootstyle="primary")


#negyedik negyed

img4 = ImageTk.PhotoImage(Image.open("images/4.jpg").resize((200,300)))
label_img4 = Label(root, image = img4,width=200,borderwidth=4, relief="solid")
label_img4.grid(row=5, column=3,rowspan=3)
def on_click4(event=None):
    print("image4 clicked")
button_img4 = Button(root, image= img4, command=lambda:jegyfoglalo.buttonStructure(4))
button_img4.grid(row=5, column=3,rowspan=3)
label_leiras4 = Label(root,justify= "left", text="Cím: " + movies[3].title +"\n Játékidő: " + movies[3].playtime +"\n Műfaj: " + movies[3].genre, font=('Times 18'))
label_leiras4.grid(row=5, column=4)
button_f3 = ttk.Button(bootstyle="success-outline", text="Foglalás", command=lambda:jegyfoglalo.buttonStructure(4))
button_f3.grid(row=6,column=4)
movies = []
for i in range(4):
    movie = database.selectMovie(i+1)
    movies.append(movie)

Meter4 = ttk.Meter(
    bootstyle="primary", 
    subtextstyle="secondary", 
    amounttotal = movies[3].chairs, 
    amountused = database.count(4), 
    subtext= "Foglalt helyek",
    metersize = 150
    )
Meter4.grid(row=7,column=4)

if Meter4.amountusedvar.get() >= movies[3].chairs*0.75:
    Meter4.configure(bootstyle="danger")
elif Meter4.amountusedvar.get() >= movies[3].chairs*0.5:
    Meter4.configure(bootstyle="warning")
else:
    Meter4.configure(bootstyle="primary")




root.mainloop()
