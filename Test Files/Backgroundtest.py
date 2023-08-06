from customtkinter import *
from tkinter import *
from PIL import Image
set_appearance_mode("Light")
deactivate_automatic_dpi_awareness()

app = CTk()
app.title("STEEVE")
app.geometry("480x700")
app.resizable(0,0)


background = CTkCanvas(app)
background.pack(expand=YES, fill=BOTH)


img = PhotoImage(file='Images/login.png')

background.create_image(-4,-2, image=img, anchor=NW)

Entry1 = CTkEntry(app,height=65,width=400,bg_color="white",fg_color="white",font=("Arial",20),placeholder_text="Username")
Entry1.place(x=45,y=385)

Entry2 = CTkEntry(app,height=65,width=364,bg_color="white",fg_color="white",font=("Arial",20),placeholder_text="Password",show="*")
Entry2.place(x=45,y=518)
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
signin = CTkButton(app, text="Sign In",width=400,height=66,bg_color="white",fg_color="#0e6cd9",hover_color="#0e6cd9",text_color="white",font=("Arial",20,"bold"),cursor="hand2",command=clicked)
signin.place(x=45,y=610)
showpas = CTkButton(master=app,text="",height=65,width=14,image=closed_eye, command=show_pass,bg_color="white",fg_color="transparent",hover_color="white")
showpas.place(x=410,y=518)
app.mainloop()














