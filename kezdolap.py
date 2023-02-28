from tkinter import *
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap.constants import *
import database
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



#main
lbl_mozinev = ttk.Label(root, text="Mozi",font=('Times 40'))
lbl_mozinev.grid(row=1,column=1,columnspan=4)


#első negyed
img1 = ImageTk.PhotoImage(Image.open("images/1.jpg").resize((200,300)))
label_img1 = Label(root, image = img1,width=200,borderwidth=4, relief="solid")
label_img1.grid(row=2, column=1, rowspan=3)
def on_click(event=None):
    print("image clicked")
button_img1 = Button(root, image= img1, command=on_click)
button_img1.grid(row=2, column=1, rowspan=3)
label_leiras1 = Label(root,justify= "left", text="Cím: Big Chungus\n Játékidő: 132 perc\n Időpont: minden nap 18:00", font=('Times 18'))
label_leiras1.grid(row=2, column=2)
button_f1 = ttk.Button(bootstyle="success-outline", text="Foglalás")
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
button_img3 = Button(root, image= img3, command=on_click3)
button_img3.grid(row=5, column=1,rowspan=3)
label_leiras3 = Label(root,justify= "left", text="Cím: Big Chungus\n Játékidő: 132 perc\n Időpont: minden nap 18:00", font=('Times 18'))
label_leiras3.grid(row=5, column=2)
button_f3 = ttk.Button(bootstyle="success-outline", text="Foglalás")
button_f3.grid(row=6,column=2)
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
Meter1.grid(row=7,column=2)

if Meter1.amountusedvar.get() >= movies[0].chairs*0.75:
    Meter1.configure(bootstyle="danger")
elif Meter1.amountusedvar.get() >= movies[0].chairs*0.5:
    Meter1.configure(bootstyle="warning")
else:
    Meter1.configure(bootstyle="primary")


#második negyed
img2 = ImageTk.PhotoImage(Image.open("images/3.jpg").resize((200,300)))
label_img2 = Label(root, image = img2,width=200,borderwidth=4, relief="solid")
label_img2.grid(row=2, column=3, rowspan=3)
def on_click2(event=None):
    print("image2 clicked")
button_img2 = Button(root, image= img2, command=on_click2)
button_img2.grid(row=2, column=3,rowspan=3)
label_leiras2 = Label(root,justify= "left", text="Cím: Shrek\n Játékidő: 132 perc\n Időpont: minden nap 18:00", font=('Times 18'))
label_leiras2.grid(row=2, column=4)
button_f2 = ttk.Button(bootstyle="success-outline", text="Foglalás")
button_f2.grid(row=3,column=4)
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
Meter1.grid(row=4,column=4)

if Meter1.amountusedvar.get() >= movies[0].chairs*0.75:
    Meter1.configure(bootstyle="danger")
elif Meter1.amountusedvar.get() >= movies[0].chairs*0.5:
    Meter1.configure(bootstyle="warning")
else:
    Meter1.configure(bootstyle="primary")


#negyedik negyed

img4 = ImageTk.PhotoImage(Image.open("images/4.jpg").resize((200,300)))
label_img4 = Label(root, image = img4,width=200,borderwidth=4, relief="solid")
label_img4.grid(row=5, column=3,rowspan=3)
def on_click4(event=None):
    print("image4 clicked")
button_img4 = Button(root, image= img4, command=on_click4)
button_img4.grid(row=5, column=3,rowspan=3)
label_leiras4 = Label(root,justify= "left", text="Cím: Big Chungus\n Játékidő: 132 perc\n Időpont: minden nap 18:00", font=('Times 18'))
label_leiras4.grid(row=5, column=4)
button_f3 = ttk.Button(bootstyle="success-outline", text="Foglalás")
button_f3.grid(row=6,column=4)
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
Meter1.grid(row=7,column=4)

if Meter1.amountusedvar.get() >= movies[0].chairs*0.75:
    Meter1.configure(bootstyle="danger")
elif Meter1.amountusedvar.get() >= movies[0].chairs*0.5:
    Meter1.configure(bootstyle="warning")
else:
    Meter1.configure(bootstyle="primary")




root.mainloop()
