from tkinter import *
from tkinter import messagebox
import math
foablak=Tk()
def szamit():
    uresmezonezo = mezo1.get()
    if len(uresmezonezo) == 0:
        messagebox.showerror('Error','A mező üres')
    else:
        pass
    uresmezonezo = int(uresmezonezo)    
    uresmezonezo = mezo2.get()
    if len(uresmezonezo) == 0:
        messagebox.showerror('Error','A mező üres')
    else:
        pass
    uresmezonezo = int(uresmezonezo)    
    uresmezonezo = mezo3.get()
    if len(uresmezonezo) == 0:
        messagebox.showerror('Error','A mező üres')
    else:
        pass
    uresmezonezo = int(uresmezonezo)    
    a = float(mezo1.get())
    b = float(mezo2.get())
    c = float(mezo3.get())
    if a>0 and b>0 and c > 0: 
        V = round(a**2 * b * math.pi)
        cucc = round(V*0.001)
        cucc2 = round(c*(100/cucc), 2)
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
            mezo6.delete(0, END)
            mezo5.insert(0, 'Nem fér bele')
        if belefer:
            szamolas = c/V
            mezo6.delete(0, END)
            mezo6.insert(0, str(cucc2)+' %')
foablak.title('Boros hordó')
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
gomb.grid(row=3,column =0,)
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
can1 = Canvas(foablak, bg = 'white' ,width = 160, height=160)
kep = PhotoImage(file='boroshord.png',)
item = can1.create_image(100, 100, image = kep,)
can1.grid( column=3, row=3, padx = 15)
foablak.mainloop()