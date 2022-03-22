from tkinter import *
import math
foablak=Tk()
def térfogat():
    a = int(mezo1.get())
    b = int(mezo2.get())
    V = a**2 * b * math.pi
    mezo3.delete(0, END)
    mezo3.insert(0, ''+str(V))
def vashenger():
    a = int(mezo1.get())
    b = int(mezo2.get())
    V = a**2 * b * math.pi
    p = 2700
    m = p * V
    mezo4.delete(0, END)
    mezo4.insert(0, ''+str(m))
szoveg1=Label(foablak, text='Sugár (cm):')
szoveg1.grid(row=0,column=0)
mezo1=Entry(foablak)
mezo1.grid(row=0,column=1,)
szoveg2=Label(foablak, text='Magasság (cm):')
szoveg2.grid(row=1,column=0)
mezo2=Entry(foablak)
mezo2.grid(row=1,column=1,)
gomb = Button(foablak, text='Kiszámít', command=lambda:[térfogat(), vashenger()])
gomb.grid(row=2,column =1)
szoveg3=Label(foablak, text='Térfogat:')
szoveg3.grid(row=3,column=0)
mezo3=Entry(foablak)
mezo3.grid(row=3,column=1)
szoveg4=Label(foablak, text='Vashenger:')
szoveg4.grid(row=4,column=0)
mezo4=Entry(foablak)
mezo4.grid(row=4,column=1)
szoveg5=Label(foablak, text='Fa henger:')
szoveg5.grid(row=5,column=0)
mezo5=Entry(foablak)
mezo5.grid(row=5,column=1)
foablak.mainloop()