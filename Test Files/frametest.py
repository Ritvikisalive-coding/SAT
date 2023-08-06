from tkinter import *
rootwindow = Tk()
rootwindow.geometry("400x400")
rootwindow.resizable(FALSE,FALSE)
rootwindow.title("Frame testing")#set the name of the window

#all frames
choseframe = Frame(rootwindow)
studentsigninframe = Frame(rootwindow)
teachersigninframe = Frame(rootwindow)
parentbookingframe = Frame(rootwindow)
teacherbookedframe = Frame(rootwindow)

def toteacher():
    teachersigninframe.pack(fill='both', expand=1)
    studentsigninframe.forget()

def tostudent():
    studentsigninframe.pack(fill='both', expand=1)
    teachersigninframe.forget()

studentsigninframe.pack(fill='both', expand=1)

lbl = Label(studentsigninframe, text="HEllo WORLD")
lbl.pack()

lbl1 = Label(teachersigninframe, text="HIIII")
lbl1.pack()

btn = Button(studentsigninframe, text="To HI frame", command=toteacher)
btn.pack()

btn2 = Button(teachersigninframe, text="To Hello World Frame", command=tostudent)
btn2.pack()
rootwindow.mainloop()