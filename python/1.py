from tkinter import *
import math
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a + b
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

def szorzás():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a * b
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

def osztás():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= (a / b) if b !=0 else 'Nem lehet nullával osztani'
    mezo3.delete(0, END) 
    mezo3.insert(0, str(c))

def kivonás():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a - b
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

foablak=Tk()
mezo3=Entry(foablak,width =25, justify="center")
mezo3.grid( row = 0, column = 1)
gomb3=Button(foablak,text="Kilepés", fg="black", command=foablak.destroy)
gomb3.grid(row = 8, column = 3)
szoveg1=Label(foablak, text="Első szám:")
szoveg1.grid(row = 1, column=0)
mezo1=Entry(foablak,)
mezo1.grid(row = 1, column=2)
szoveg2=Label(foablak, text="Második szám:")
szoveg2.grid(row = 2, column=0)
mezo2=Entry(foablak)
mezo2.grid(row = 2, column=2)
gomb4=Button(foablak,text="Összeadás", command=osszeg)
gomb4.grid(row = 3, column = 1)
gomb5=Button(foablak,text="Kivonás", command=kivonás)
gomb5.grid(row = 4, column = 1)
gomb6=Button(foablak,text="Szorzás", command=szorzás)
gomb6.grid(row = 5, column = 1)
gomb7=Button(foablak,text="Osztás", command=osztás)
gomb7.grid(row = 6, column = 1)
can1 = Canvas(foablak, width = 460, height = 460, bg = 'white')
photo = PhotoImage(file = '1.gif')
item = can1.create_image(80, 80, image = photo)
can1.grid(row = 11, column = 1)
foablak.mainloop()