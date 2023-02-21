from tkinter import *
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap.constants import *

root = Tk()
root.geometry("850x800")

#scrolling 



# light-dark mode 
light = PhotoImage(file="light.png")
dark = PhotoImage(file="dark.png")
  
switch_value = True
  
def toggle():
  
    global switch_value
    if switch_value == True:
        switch.config(image=dark)
        style = ttk.Style("darkly")           
        switch_value = False
  
    else:
        switch.config(image=light)
          
        style = ttk.Style("cosmo")
        switch_value = True
  
  
switch = Button(root, image=light,bd=0, bg="white", activebackground="white", command=toggle,borderwidth=2, relief="groove")
switch.grid(row=1, column=4)
  



#main
lbl_mozinev = ttk.Label(root, text="Mozi",font=('Times 40'))
lbl_mozinev.grid(row=1,column=1,columnspan=3)

img = ImageTk.PhotoImage(Image.open("image.png"))
label_img1 = Label(root, image = img,width=200,borderwidth=4, relief="solid")
label_img1.grid(row=2, column=1)
label_leiras3 = Label(root,justify= "left", text="Cím: Big Chungus\n Játékidő: 132 perc\n Időpont: minden nap 18:00", font=('Times 25'))
label_leiras3.grid(row=3, column=1)


img3 = ImageTk.PhotoImage(Image.open("image.png"))
label_img3 = Label(root, image = img,width=200,borderwidth=4, relief="solid")
label_img3.grid(row=4, column=1)
label_leiras3 = Label(root,justify= "left", text="Cím: Big Chungus\n Játékidő: 132 perc\n Időpont: minden nap 18:00", font=('Times 25'))
label_leiras3.grid(row=5, column=1)

img2 = ImageTk.PhotoImage(Image.open("shrek.png"))
label_img2 = Label(root, image = img2,width=200,borderwidth=4, relief="solid")
label_img2.grid(row=2, column=3)
label_leiras3 = Label(root,justify= "left", text="Cím: Shrek\n Játékidő: 132 perc\n Időpont: minden nap 18:00", font=('Times 25'))
label_leiras3.grid(row=3, column=3)



img4 = ImageTk.PhotoImage(Image.open("image.png"))
label_img4 = Label(root, image = img,width=200,borderwidth=4, relief="solid")
label_img4.grid(row=4, column=3)
label_leiras4 = Label(root,justify= "left", text="Cím: Big Chungus\n Játékidő: 132 perc\n Időpont: minden nap 18:00", font=('Times 25'))
label_leiras4.grid(row=5, column=3)




root.mainloop()
