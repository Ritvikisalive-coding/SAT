from customtkinter import *
from tkinter import *
from PIL import Image
set_appearance_mode("Light")


app = CTk()
app.title("STEEVE")
app.geometry("390x600")
app.resizable(0,0)


background = CTkCanvas(app)
background.pack(expand=YES, fill=BOTH)


img = PhotoImage(file='C:\\Users\\ritvi\\Documents\\GitHub\\SAT\\Images\\Background_slimed.png')

background.create_image(-4,-2, image=img, anchor=NW)

Entry1 = CTkEntry(app,height=50,width=322,bg_color="white",fg_color="white",font=("Arial",20),placeholder_text="Username")
Entry1.place(x=35,y=308)

Entry2 = CTkEntry(app,height=50,width=305,bg_color="white",fg_color="white",font=("Arial",20),placeholder_text="Password",show="*")
Entry2.place(x=35,y=414)
def clicked():
    username = Entry1.get()
    password = Entry2.get()
    print("Username: "+username +", Password: "+ password)
def show_pass():
    if Entry2.cget('show') == '*':
        Entry2.configure(show='')
        showpas.configure(image=open_eye)
    else:
        Entry2.configure(show='*')
        showpas.configure(image=closed_eye)
open_eye = CTkImage(Image.open("Images/show_eye.png"))
closed_eye = CTkImage(Image.open("Images/hide_eye.png"))
signin = CTkButton(app, text="Sign In",width=322,height=50,bg_color="white",fg_color="#0e6cd9",hover_color="#0e6cd9",text_color="white",font=("Arial",15,"bold"),cursor="hand2",command=clicked)
signin.place(x=35,y=480)
showpas = CTkButton(master=app,text="",height=60,width=5,image=closed_eye, command=show_pass,bg_color="white",fg_color="transparent",hover_color="white")
showpas.place(x=340,y=410)
app.mainloop()














