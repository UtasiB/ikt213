from tkinter import *
import math
foablak=Tk()
def szamit():
    a = float(mezo1.get())
    b = float(mezo2.get())
    c = float(mezo3.get())
    V = a**2 * b * math.pi
    cucc = V/1000
    mezo4.delete(0, END)
    mezo4.insert(0, ''+str("%.2f" % cucc)+ ' l')
    if cucc > c:
        belefer = True
    else:
        belefer = False
    if belefer:
        mezo5.delete(0, END)
        mezo5.insert(0,'Belefér')
    else:
        mezo5.delete(0, END)
        mezo5.insert(0, 'Nem fér bele')
    if belefer:
        szamolas = c/V
        mezo6.delete(0, END)
        mezo6.insert(0, 'Ennyi % van még'+szamolas)

    

szoveg1=Label(foablak, text='Sugár (cm):')
szoveg1.grid(row=0,column=0)
mezo1=Entry(foablak)
mezo1.grid(row=0,column=1,)
szoveg2=Label(foablak, text='Magasság (cm):')
szoveg2.grid(row=1,column=0)
mezo2=Entry(foablak)
mezo2.grid(row=1,column=1,)
szoveg3=Label(foablak, text ='Bor (l):')
szoveg3.grid(row=2,column =0)
mezo3=Entry(foablak)
mezo3.grid(row=2,column=1,)
gomb = Button(foablak, text='Kiszámít', command=szamit)
gomb.grid(row=3,column =2,)
szoveg4=Label(foablak, text ='Térfogat:')
szoveg4.grid(row=4,column =0)
mezo4=Entry(foablak)
mezo4.grid(row=4,column=1,)
szoveg5=Label(foablak, text ='Belefér a hordóba?')
szoveg5.grid(row=5,column =0)
mezo5=Entry(foablak)
mezo5.grid(row=5,column=1,)
szoveg6=Label(foablak, text ='Ennyi maradt:')
szoveg6.grid(row=6,column =0)
mezo6=Entry(foablak)
mezo6.grid(row=6,column=1,)


foablak.mainloop()
