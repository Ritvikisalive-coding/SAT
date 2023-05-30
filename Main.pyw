import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import csv
from PIL import ImageTk
from PIL import Image
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import filedialog#For file explorer

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")
ctk.deactivate_automatic_dpi_awareness()

def callback(url):
    webbrowser.open_new(url)



def chose_login():

    win = ctk.CTk()
    win.geometry("300x180")
    win.title("PST Log In")
    win.iconbitmap('Images/logo.ico')
    win.resizable(0,0)
    def themed():
        if themeswitch.get() == 1:
            ctk.set_appearance_mode("Dark")
            themeswitch.configure(text="🌙")
        if themeswitch.get() == 0:
            ctk.set_appearance_mode("Light")
            themeswitch.configure(text="☀️")
    themeswitch = ctk.CTkSwitch(win,text="☀️",command=themed)
    themeswitch.place(x=5,y=5)

    student = ctk.CTkButton(win, text="Student / Parent", font=("Straight",12),command=lambda:student_sign_in(win))
    teacher = ctk.CTkButton(win, text="Teacher", font=("Straight",12),command=lambda:teacher_sign_in(win))
    student.place(x=85,y=85)
    teacher.place(x=85,y=120)
    Label = ctk.CTkLabel(win, text="PST Log In", font=("Homework",40))
    Label.place(x=70,y=30)

    win.mainloop()

userpass = {}
def student_sign_in(win):
    win.destroy()
    def themed():
        if themeswitch.get() == 1:
            ctk.set_appearance_mode("Dark")
            themeswitch.configure(text="🌙")
        if themeswitch.get() == 0:
            ctk.set_appearance_mode("Light")
            themeswitch.configure(text="☀️")
    wins = ctk.CTk()
    wins.geometry("300x300")
    wins.title("PST Log In - Parent / Student")
    wins.iconbitmap('Images/logo.ico')
    wins.resizable(0,0)
    themeswitch = ctk.CTkSwitch(wins,text="☀️",command=themed)
    themeswitch.place(x=5,y=5)

    with open("csv//student_userpass.csv") as csvfile:

        reader=csv.reader(csvfile)
        
        for line in reader:
            #username and password format in csv file is username:password

            user = line[0].split(":")[0]
            
            pasw = line[0].split(":")[1]
            userpass[user] = pasw


    def clicked():
    #please help me figure out why it wont compare the correct password and username
        user = username.get()
        pasw = passw.get()

        if userpass.get(user) == pasw:
            print(username.get()+" "+ user)
            print(user+" "+pasw)
            CTkMessagebox(title='Log in successful', message= f'Hello {user}')
        else:
            print(username.get()+" "+ user)
            print(user+" "+pasw)
            CTkMessagebox(title='Log In Error', message= 'Incorrect Username or Password', icon="cancel")



    def show_pass():
        if passw.cget('show') == '*':
            passw.configure(show='')
        else:
            passw.configure(show='*')


    lbl = ctk.CTkLabel(wins, text="Log in", font=("Homework",40))
    lbl.place(x=100,y=2)

    usernamelbl = ctk.CTkLabel(wins,text="Username", font=("Straight",12))
    usernamelbl.place(x=120,y=50)

    username= ctk.CTkEntry(wins, placeholder_text="AAA000", font=("Straight",12))
    username.place(x=65, y=70)

    passwordlbl = ctk.CTkLabel(wins, text="Password", font=("Straight",12))
    passwordlbl.place(x=120,y=100)

    passw = ctk.CTkEntry(wins, show="*", placeholder_text="********")
    passw.place(x=65, y=120)
    passw.bind("<Return>", lambda e: parent_booking_screen(wins))

    showpas = ctk.CTkCheckBox(wins,text="Show password", command=show_pass)
    showpas.place(x=50,y=155)

    

    link = ctk.CTkLabel(wins, text="Contact School",text_color="blue", font= ('Arial',12,"underline"), cursor="hand2")
    link.place(x=50,y=220)
    link.bind("<Button-1>", lambda e: callback("https://www.gwsc.vic.edu.au/page/186/Contact-Us"))

    Login = ctk.CTkButton(wins,text="LOGIN", width=12, command=lambda:parent_booking_screen(wins))
    Login.place(x=100 ,y=190)



    wins.mainloop()
def teacher_sign_in(win):
    win.destroy()
    def themed():
        if themeswitch.get() == 1:
            ctk.set_appearance_mode("Dark")
            themeswitch.configure(text="🌙")
        if themeswitch.get() == 0:
            ctk.set_appearance_mode("Light")
            themeswitch.configure(text="☀️")
    wint = ctk.CTk()
    wint.geometry("300x300")
    wint.title("PST Log In - Teacher")
    wint.iconbitmap('Images/logo.ico')
    wint.resizable(0,0)
    themeswitch = ctk.CTkSwitch(wint,text="☀️",command=themed)
    themeswitch.place(x=5,y=5)

    with open("csv//teacher_userpass.csv") as csvfile:

        reader=csv.reader(csvfile)
        
        for line in reader:
            #username and password format in csv file is username:password

            user = line[0].split(":")[0]
            
            pasw = line[0].split(":")[1]
            userpass[user] = pasw


    def clicked():
    #please help me figure out why it wont compare the correct password and username
        user = username.get()
        pasw = passw.get()

        if userpass.get(user) == pasw:
            print(username.get()+" "+ user)
            print(user+" "+pasw)
            CTkMessagebox(title='Log in successful', message= f'Hello {user}')
        else:
            print(username.get()+" "+ user)
            print(user+" "+pasw)
            CTkMessagebox(title='Log In Error', message= 'Incorrect Username or Password', icon="cancel")



    def show_pass():
        if passw.cget('show') == '*':
            passw.configure(show='')
        else:
            passw.configure(show='*')


    lbl = ctk.CTkLabel(wint, text="Log in", font=("Homework",40))
    lbl.place(x=100,y=2)

    usernamelbl = ctk.CTkLabel(wint,text="Username")
    usernamelbl.place(x=120,y=50)

    username= ctk.CTkEntry(wint)
    username.place(x=40, y=70)

    passwordlbl = ctk.CTkLabel(wint, text="Password")
    passwordlbl.place(x=120,y=100)

    passw = ctk.CTkEntry(wint, show="*")
    passw.place(x=40, y=120)
    passw.bind("<Return>", lambda e: teacher_booked_screen(wint))

    showpas = ctk.CTkCheckBox(wint,text="Show password", command=show_pass)
    showpas.place(x=50,y=155)

    link = ctk.CTkLabel(wint, text="Contact School",text_color="blue", font= ('Arial',15,"underline"), cursor="hand2")
    link.place(x=50,y=220)
    link.bind("<Button-1>", lambda e: callback("https://www.gwsc.vic.edu.au/page/186/Contact-Us"))

    Login = ctk.CTkButton(wint,text="LOGIN", width=12, command=clicked)
    Login.place(x=100 ,y=190)



    wint.mainloop()

def parent_booking_screen(wins):
    wins.destroy()
    winbooking = ctk.CTk()
    winbooking.iconbitmap('Images/logo.ico')
    winbooking.title("PST Parent Booking")
    winbooking.geometry("600x400")
    def combobox_callback(choice):
        if choice == "CHILDREN":
            CTkMessagebox(title='The goblin of GWSC', message= f'I hear you want to see your children again')
        elif choice == "BOOKINGS":
            CTkMessagebox(title='The Bookings of GWSC', message= f'You should remember your bookings not make me tell you')
        else:
            CTkMessagebox(title='You are already on your account', message= f'Account already opened')
    combobox = ctk.CTkOptionMenu(winbooking, values=["NAME", "BOOKINGS","CHILDREN"],command=combobox_callback,state="readonly")
    combobox.set("NAME")
    combobox.place(x=460,y=5)



    winbooking.mainloop()

def teacher_booked_screen(wint):
    wint.destroy()
    winbooked = ctk.CTk()
    winbooked.resizable(0,0)
    winbooked.iconbitmap('Images/logo.ico')
    winbooked.geometry("815x240")
    sidebar = ctk.CTkFrame(winbooked,width=200, height=400 )
    sidebar.place(x=620,y=-4)
    def file1():
        file = filedialog.asksaveasfile(initialdir="Desktop",initialfile="PSTbookings.csv",defaultextension=".csv",filetypes = [("Excel Files", "*.xls *.csv")])
        insidefile = open("csv/teacherallbooking.csv")
        text=insidefile.read()
        file.write(text)
        file.close

    downloadbtn = ctk.CTkButton(sidebar, text="   Download", font=("Arial",14,"bold"),command=file1)
    downloadbtn.place(x=30,y=80)
    symbollbl = ctk.CTkLabel(sidebar,text="⇩",bg_color="#2cc985",text_color="white",font=("Arial",20))
    symbollbl.place(x=58,y=80)
    treeviewbookings = ttk.Treeview(winbooked,columns=("student_name","booking_time","subject"),show="headings")
    treeviewbookings.heading("student_name",text="Student Name")
    treeviewbookings.heading("booking_time",text="Time Booked")
    treeviewbookings.heading("subject",text="Subject")

    treeviewbookings.place(x=5,y=5)

    winbooked.mainloop()










































































































































chose_login()
