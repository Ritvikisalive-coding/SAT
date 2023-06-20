from customtkinter import *
from tkinter import *
set_appearance_mode("Light")

app = CTk()
app.geometry("400x400")
def raise_frame(frame):
    frame.tkraise()
f1 = Frame(app, width=700, height=250)
f2 = Frame(app, width=100, height=250)
f3 = Frame(app, width=250, height=750)
f4 = Frame(app)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

text = CTkLabel(f1,text="CHEESEBALLS")
text.pack()
CTkButton(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
CTkLabel(f1, text='FRAME 1').pack()

CTkLabel(f2, text='FRAME 2').pack()
CTkButton(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

CTkLabel(f3, text='FRAME 3').pack(side='left')
CTkButton(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

CTkLabel(f4, text='FRAME 4').pack()
CTkButton(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()


raise_frame(f1)
app.mainloop()
