from tkinter import *
def klikk():
    print('Kilkeltem')
ablak1 = Tk()
gyoker = 'H:\\ikt\\python\\'
ablak1.geometry('420x420')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file='kép.png')
ablak1.iconphoto(True, icon)
ablak1.config(bg = 'black')
kep= PhotoImage(file=gyoker+'png.png',width=150,height= 150)
gombkep =PhotoImage(file=gyoker+'png.png')




cimke = Label(ablak1,
                text='Üdvözlet!',
                fg = '#555312',
                bg = '#c3cee0',
                font = ('Arial', 45, 'bold'), 
                bd = 10,
                relief=RAISED,
                padx = 25,
                pady= 30,
                image=kep,
                compound='center').pack()

gomb = Button(ablak1,
                text ='Kattints',
                fg = 'blue',
                font=('Comic Sans', 35, 'bold'),
                bg = 'yellow',
                relief=SUNKEN,
                bd = 10,
                command=klikk,
                padx= 12,
                pady = 12,
                image= gombkep,
                compound='center',
                activebackground= 'blue',
                activeforeground= 'yellow',
                state = ACTIVE).pack()



ablak1.mainloop()