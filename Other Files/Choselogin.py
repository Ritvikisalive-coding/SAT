from customtkinter import *
from tkinter import *
from PIL import Image
set_appearance_mode("Light")
deactivate_automatic_dpi_awareness()

app = CTk()
app.title("STEEVE")
app.geometry("480x500")
app.resizable(0,0)


background = CTkCanvas(app)
background.pack(expand=YES, fill=BOTH)


img = PhotoImage(file='Images/choose_login.png')

background.create_image(-4,-2, image=img, anchor=NW)

student = CTkButton(app, text="Parent ", font=("Straight",20))
teacher = CTkButton(app, text="Teacher", font=("Straight",20))
student.place(x=85,y=380)
teacher.place(x=250,y=380)
app.mainloop()


