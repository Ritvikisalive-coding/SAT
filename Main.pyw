import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import csv
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import filedialog#For file explorer
from PIL import ImageTk
from PIL import Image
from winotify import Notification, audio
import time
from win10toast import ToastNotifier
from plyer import notification
from tkinter.messagebox import showinfo
from datetime import datetime
import PIL.Image

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
ctk.deactivate_automatic_dpi_awareness()

def callback(url):
    webbrowser.open_new(url)



def chose_login():

    win = ctk.CTk()
    win.geometry("480x500")
    win.title("PST Log In")
    #win.eval('tk::PlaceWindow . center')
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

    background = ctk.CTkCanvas(win)
    background.pack(expand=YES, fill=BOTH)


    img = PhotoImage(file='Images/choose_login.png')

    background.create_image(-4,-2, image=img, anchor=NW)

    student = ctk.CTkButton(win, text="Parent ", font=("Straight",20),command=lambda:student_sign_in(win))
    teacher = ctk.CTkButton(win, text="Teacher", font=("Straight",20),command=lambda:teacher_sign_in(win))
    student.place(x=85,y=380)
    teacher.place(x=250,y=380)
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
    wins.geometry("480x700")
    wins.title("PST Log In - Parent")
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
            parent_booking_screen(wins)
        else:
            CTkMessagebox(title='Log In Error', message= 'Incorrect Username or Password', icon="cancel")



    def show_pass():
        if passw.cget('show') == '*':
            passw.configure(show='')
        else:
            passw.configure(show='*')


    background = ctk.CTkCanvas(wins)
    background.pack(expand=YES, fill=BOTH)


    img = PhotoImage(file='Images/login.png')

    background.create_image(-4,-2, image=img, anchor=NW)

    username = ctk.CTkEntry(wins,height=65,width=400,bg_color="white",fg_color="white",font=("Arial",20),placeholder_text="Username")
    username.place(x=45,y=385)

    passw = ctk.CTkEntry(wins,height=65,width=364,bg_color="white",fg_color="white",font=("Arial",20),placeholder_text="Password",show="*")
    passw.place(x=45,y=518)
    passw.bind("<Return>", lambda e: clicked())
    def show_pass():
        if passw.cget('show') == '*':
            passw.configure(show='')
            showpas.configure(image=open_eye)
        else:
            passw.configure(show='*')
            showpas.configure(image=closed_eye)
    open_eye = ctk.CTkImage(Image.open("Images/show_eye.png"))
    closed_eye = ctk.CTkImage(Image.open("Images/hide_eye.png"))
    
    signin = ctk.CTkButton(wins, text="Sign In",width=400,height=45,bg_color="white",fg_color="#0e6cd9",hover_color="#0e6cd9",text_color="white",font=("Arial",20,"bold"),cursor="hand2",command=clicked)
    signin.place(x=45,y=600)
    showpas = ctk.CTkButton(master=wins,text="",height=65,width=14,image=closed_eye, command=show_pass,bg_color="white",fg_color="transparent",hover_color="white")
    showpas.place(x=410,y=518)

    

    link = ctk.CTkLabel(wins, text="Contact School",text_color="blue", font= ('Arial',15,"underline"), cursor="hand2",bg_color="white",fg_color="white")
    link.place(x=50,y=645)
    link.bind("<Button-1>", lambda e: callback("https://www.gwsc.vic.edu.au/page/186/Contact-Us"))





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
    wint.geometry("480x700")
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
            teacher_booked_screen(wint)
        else:
            CTkMessagebox(title='Log In Error', message= 'Incorrect Username or Password', icon="cancel")



    def show_pass():
        if passw.cget('show') == '*':
            passw.configure(show='')
        else:
            passw.configure(show='*')


    def show_pass():
        if passw.cget('show') == '*':
            passw.configure(show='')
        else:
            passw.configure(show='*')


    background = ctk.CTkCanvas(wint)
    background.pack(expand=YES, fill=BOTH)


    img = PhotoImage(file='Images/login.png')

    background.create_image(-4,-2, image=img, anchor=NW)

    username = ctk.CTkEntry(wint,height=65,width=400,bg_color="white",fg_color="white",font=("Arial",20),placeholder_text="Username")
    username.place(x=45,y=385)

    passw = ctk.CTkEntry(wint,height=65,width=364,bg_color="white",fg_color="white",font=("Arial",20),placeholder_text="Password",show="*")
    passw.place(x=45,y=518)
    passw.bind("<Return>", lambda e: clicked())
    def show_pass():
        if passw.cget('show') == '*':
            passw.configure(show='')
            showpas.configure(image=open_eye)
        else:
            passw.configure(show='*')
            showpas.configure(image=closed_eye)
    open_eye = ctk.CTkImage(Image.open("Images/show_eye.png"))
    closed_eye = ctk.CTkImage(Image.open("Images/hide_eye.png"))
    
    signin = ctk.CTkButton(wint, text="Sign In",width=400,height=45,bg_color="white",fg_color="#0e6cd9",hover_color="#0e6cd9",text_color="white",font=("Arial",20,"bold"),cursor="hand2",command=clicked)
    signin.place(x=45,y=600)
    showpas = ctk.CTkButton(master=wint,text="",height=65,width=14,image=closed_eye, command=show_pass,bg_color="white",fg_color="transparent",hover_color="white")
    showpas.place(x=410,y=518)

    

    link = ctk.CTkLabel(wint, text="Contact School",text_color="blue", font= ('Arial',15,"underline"), cursor="hand2",bg_color="white",fg_color="white")
    link.place(x=50,y=645)
    link.bind("<Button-1>", lambda e: callback("https://www.gwsc.vic.edu.au/page/186/Contact-Us"))



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
    winbooked.title("All bookings")
    winbooked.iconbitmap('Images/logo.ico')
    winbooked.geometry("815x240")
    sidebar = ctk.CTkFrame(winbooked,width=200, height=400 )
    sidebar.place(x=624,y=-4)
    def file1():
        file = filedialog.asksaveasfile(initialdir="Desktop",initialfile="PSTbookings.csv",defaultextension=".csv",filetypes = [("Excel Files", "*.xls *.csv")])
        insidefile = open("csv/teacherallbooking.csv")
        text=insidefile.read()
        file.write(text)
        file.close
        toast = Notification(app_id="GWSC PST Booking System", title="Download", msg="Your booking confirmation has finished downloading",duration="short")
        toast.set_audio(audio.Default ,loop=False)
        toast.show()
        

    downloadbtn = ctk.CTkButton(sidebar, text="   Download", font=("Arial",25,"bold"),command=file1)
    downloadbtn.place(x=20,y=80)
    symbollbl = ctk.CTkLabel(sidebar,text="⇩",bg_color="#3b8ed0",text_color="white",font=("Arial",32))
    symbollbl.place(x=27,y=80)
    treeviewbookings = ttk.Treeview(winbooked,columns=("student_name","booking_time","subject"),show="headings")
    treeviewbookings.heading("student_name",text="Student Name")
    treeviewbookings.heading("booking_time",text="Time Booked")
    treeviewbookings.heading("subject",text="Subject")
    treeviewbookings.place(x=5,y=5)
    ctk_textbox_scrollbar = ctk.CTkScrollbar(winbooked, command=treeviewbookings.yview)
    ctk_textbox_scrollbar.place(x=608,y=25)

# connect textbox scroll event to CTk scrollbar
    treeviewbookings.configure(yscrollcommand=ctk_textbox_scrollbar.set)
    #insidefile = open("csv/teacherallbooking.csv")
    #text=insidefile.read()
    #text = text.split("\n")
    contacts = []
    #contacts.append((text))
    #print(contacts)

    data = []
    with open("csv/teacherallbooking.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    def selectionSort(data, size):
   
        for step in range(size):
            min_idx = step

            for i in range(step + 1, size):
            
                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if data[i][1] < data[min_idx][1]:
                    min_idx = i
            
            # put min at the correct position
            (data[step], data[min_idx]) = (data[min_idx], data[step])
    size = len(data)
    selectionSort(data, size)
    

# add data to the treeview
    for i in range(len(data)):
        sname = data[i][0]
        stime = data[i][1]
        ssubject = data[i][2]  
        dateTime = datetime.strptime(stime, '%H:%M')
        timein12 = dateTime.strftime('%I:%M %p').lstrip('0')      
        treeviewbookings.insert('', END, values=(sname, timein12, ssubject))
    def item_selected(event):
        for selected_item in treeviewbookings.selection():
            item = treeviewbookings.item(selected_item)
            record = item['values']
            record = record
            showinfo(title='Information', message=', '.join(record))


    treeviewbookings.bind('<<TreeviewSelect>>', item_selected)
    winbooked.mainloop()

chose_login()
