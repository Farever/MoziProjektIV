from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image
import database

# Mindent widgetként adunk hozzá

# Root -> a fő widget (a fő ablak)
root = Tk()
root.title("Imageviewer")

# Kép
# Import nélküli módszer
my_img1 = Image.open("images/1.jpg")
my_img1 = my_img1.resize((int(541*0.75), int(960*0.75)))
my_img1 = imgObj = ImageTk.PhotoImage(my_img1)

my_img2 = Image.open("images/2.jpg")
my_img2 = my_img2.resize((int(541*0.75), int(960*0.75)))
my_img2 = imgObj = ImageTk.PhotoImage(my_img2)

my_img3 = Image.open("images/3.jpg")
my_img3 = my_img3.resize((int(541*0.75), int(960*0.75)))
my_img3 = imgObj = ImageTk.PhotoImage(my_img3)

my_img4 = Image.open("images/4.jpg")
my_img4 = my_img4.resize((int(541*0.75), int(960*0.75)))
my_img4 = imgObj = ImageTk.PhotoImage(my_img4)

index = 0
image_list = [my_img1, my_img2, my_img3, my_img4]

textOfStatusbar = StringVar()
movie = database.selectMovie(index+1)
textOfStatusbar.set(movie.title)


# Statusbar
status = ttk.Label(root, textvariable= textOfStatusbar, font=('helvetica', 24))

my_label = Label(root, image=image_list[index])
my_label.grid(row=0, column=0, columnspan=4)


def forward():
    global my_label
    global index
    global status
    my_label.grid_forget()
    if index+1 == len(image_list):
        # Újraindulnak a képek
        index = 0
        # Vagy letiltjuk őket (de akkor eggyel korábban)
        #button_forward['state'] = DISABLED
        # Feladat: Külön ellenőrzés, hogy mikor melyiket kell tiltani
    else:
        index += 1
    my_label = Label(root, image=image_list[index])
    my_label.grid(row=0, column=0, columnspan=4)
    movie = database.selectMovie(index+1)
    textOfStatusbar.set(movie.title)

def back():
    global my_label
    global index
    global status
    my_label.grid_forget()
    if index-1 == -1:
        index = len(image_list)-1
    else:
        index -= 1
    my_label = Label(root, image=image_list[index])
    my_label.grid(row=0, column=0, columnspan=4)
    # Textvariable
    movie = database.selectMovie(index+1)
    textOfStatusbar.set(movie.title)


# Statusbar képernyőre
status.grid(row=2, column=0, columnspan=4)

# Gombok létrehozása
# Előre
button_forward = ttk.Button(root, text=">>", command=forward)
button_forward.grid(row=1, column=3)

# Hátra
button_back = ttk.Button(root, text="<<", command=back)
button_back.grid(row=1, column=0)

# Kilépés
button_quit = ttk.Button(root, text="Kilépés", command=root.quit)
button_quit.grid(row=1, column=1, columnspan=2)
# Event loop létrehozása
root.mainloop()