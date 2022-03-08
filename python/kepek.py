from tkinter import *
ablak1 = Tk()
gyoker = 'H:\\ikt\\python\\'
ablak1.geometry('420x420')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file='kép.png')
ablak1.iconphoto(True, icon)
ablak1.config(bg = 'black')
kep= PhotoImage(file=gyoker+'png.png')





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

ablak1.mainloop()