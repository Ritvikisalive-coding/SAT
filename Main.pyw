#Import all libraries needed
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import csv
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from winotify import Notification, audio
from tkinter.messagebox import showinfo
import datetime
from datetime import datetime
#Set basic customtkinter atributes
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
ctk.deactivate_automatic_dpi_awareness()
#function to allow hyperlink to open web pages
def callback(url):
    webbrowser.open_new(url)
#---------------------------------------------------------Main window initilisation and frame configuration--------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Initialise the main window 
rootwindow = Tk()
rootwindow.resizable(FALSE,FALSE)
rootwindow.title("PST Booking System")#set the name of the window
rootwindow.iconbitmap('Images/logo.ico')#set the favicon for the windows
#all frames
choseframe = Frame(rootwindow)
studentsigninframe = Frame(rootwindow)
teachersigninframe = Frame(rootwindow)
parentbookingframe = Frame(rootwindow)
teacherbookedframe = Frame(rootwindow)
#-----------------------------------------------------Chose LogIn page----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Function to generate window to choose which log in you want wheater thats to log in as a parent or to log in as a teacher
def chose_login():
    rootwindow.geometry("480x480")#set the winow size
    choseframe.pack(fill='both', expand=1)
    rootwindow.title("PST Booking System")
    #open image and set it to be the background image by adding it to the Label
    img = ImageTk.PhotoImage(Image.open('Images/choose_login.png'))
    image = ctk.CTkLabel(choseframe, image=img,text="",anchor="center")
    image.place(x=0,y=-24)
    #Create buttons to select which mode you would like to log in as
    student = ctk.CTkButton(choseframe, text="Parent ", font=("Straight",20),command=lambda:student_sign_in())
    teacher = ctk.CTkButton(choseframe, text="Teacher", font=("Straight",20),command=lambda:teacher_sign_in())
    student.place(x=85,y=380)
    teacher.place(x=250,y=380)
#userpass is a dictionary that is defined but is empty at this stage as it is used latter during the linear search
userpass = {}
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Functions to swap from the login pages back to the selection screen
def chose_login2():
    studentsigninframe.forget()
    chose_login()
def chose_login3():
    teachersigninframe.forget()
    chose_login()
#---------------------------------------------------Student / Parent Login Page------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Sign in for students/ Parents after they select the Parent button on the selection window
def student_sign_in():
    #update the window to change its size, title and change the frame that is being showed
    rootwindow.geometry("480x720")
    studentsigninframe.pack(fill='both', expand=1)
    choseframe.forget()
    rootwindow.title("PST Booking System - Parent Log In")
    #Linear search to access student / parental usernames and passwords
    with open("csv//student_userpass.csv") as csvfile:

        reader=csv.reader(csvfile)
        
        for line in reader:
            #username and password format in csv file is username:password, lines 74 and 76 split them to add to the dictionary making it so the program can compare the passwords and usernames to see if the accoutn exists

            user = line[0].split(":")[0]
            
            pasw = line[0].split(":")[1]
            userpass[user] = pasw


    def clicked():
        user = username.get()
        pasw = passw.get()

        if userpass.get(user) == pasw:
            parent_booking_screen()#If password is correct and matches the username that it is assigned to in the csv it will then open that booking screen
        else:
            CTkMessagebox(title='Log In Error', message= 'Incorrect Username or Password', icon="cancel")

    studentsigninframe.config(background="white")
    #Image for the background of the window that the other widgets in the frame are placed ontop of
    img = ImageTk.PhotoImage(Image.open('Images/login.png'))
    image = ctk.CTkLabel(studentsigninframe, image=img,text="",anchor="center")
    image.pack(anchor="center")
    #username and password entry fields with their specifications stating the hight, place holder text, font size and location
    username = ctk.CTkEntry(studentsigninframe,height=65,width=400,bg_color="white",fg_color="white",font=("Arial",25),placeholder_text="ABC0000")
    username.place(x=41,y=348)
    passw = ctk.CTkEntry(studentsigninframe,height=65,width=364,bg_color="white",fg_color="white",font=("Arial",25),placeholder_text="Password",show="•")
    passw.place(x=41,y=481)
    passw.bind("<Return>", lambda e: clicked())#Allows the user to click return (Enter key) whilst in the password entry field to try logging in instead of always having to click the login button
    #Change settings for the password entry allowing the user to see what they have typed once they click the show password button (showpas)
    def show_pass():
        if passw.cget('show') == '•':
            passw.configure(show='')
            showpas.configure(image=open_eye)
        else:
            passw.configure(show='•')
            showpas.configure(image=closed_eye)
    #Images are asigned to variables so they can be used later in buttons 
    open_eye = ctk.CTkImage(Image.open("Images/show_eye.png"))
    closed_eye = ctk.CTkImage(Image.open("Images/hide_eye.png"))
    backbtnicon = Image.open("Images/back.png")
    backbtnicon = backbtnicon.resize((40,40),Image.ANTIALIAS)
    backbtnicon= ImageTk.PhotoImage(backbtnicon)
    #other buttons that allow sign in, showing the users password aswell as returning back to the chose log in page
    chosescreenbtn = ctk.CTkButton(studentsigninframe,image=backbtnicon,text="",fg_color="white",bg_color="white",hover_color="white",width=50,font=("Arial",20),command=chose_login2)
    chosescreenbtn.place(x=2,y=2)    
    signin = ctk.CTkButton(studentsigninframe, text="Sign In",width=400,height=45,bg_color="white",fg_color="#0e6cd9",hover_color="#0e6cd9",text_color="white",font=("Arial",20,"bold"),cursor="hand2",command=clicked)
    signin.place(x=41,y=570)
    showpas = ctk.CTkButton(master=studentsigninframe,text="",height=65,width=14,image=closed_eye, command=show_pass,bg_color="white",fg_color="transparent",hover_color="white")
    showpas.place(x=405,y=481)
    #Contact us link that opens up the schools contact us page
    link = ctk.CTkLabel(studentsigninframe, text="Contact School",text_color="blue", font= ('Arial',15,"underline"), cursor="hand2",bg_color="white",fg_color="white")
    link.place(x=50,y=645)
    link.bind("<Button-1>", lambda e: callback("https://www.gwsc.vic.edu.au/page/186/Contact-Us"))
#------------------------------------------------------------------Teacher log in page--------------------------------------------------------------------------------------------------------------------------------------------------------#
def teacher_sign_in():
    #Adjust window for new frame
    teachersigninframe.pack(fill='both', expand=1)
    choseframe.forget()
    rootwindow.geometry("480x720")
    rootwindow.title("PST Booking System - Teacher Log In")
    #linear search for log in
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
            teacher_booked_screen()
        else:
            CTkMessagebox(title='Log In Error', message= 'Incorrect Username or Password', icon="cancel")
    

    teachersigninframe.config(background="white")
    #Set background for window
    img = ImageTk.PhotoImage(Image.open('Images/login.png'))
    image = ctk.CTkLabel(teachersigninframe, image=img,text="",anchor="center")
    image.pack(anchor="center")


    username = ctk.CTkEntry(teachersigninframe,height=65,width=400,bg_color="white",fg_color="white",font=("Arial",25),placeholder_text="AAA")
    username.place(x=41,y=348)

    passw = ctk.CTkEntry(teachersigninframe,height=65,width=364,bg_color="white",fg_color="white",font=("Arial",25),placeholder_text="Password",show="•")
    passw.place(x=41,y=481)
    passw.bind("<Return>", lambda e: clicked())
    #Show password when show password button is clicked
    def show_pass():
        if passw.cget('show') == '•':
            passw.configure(show='')
            showpas.configure(image=open_eye)
        else:
            passw.configure(show='•')
            showpas.configure(image=closed_eye)
    #open and define images for buttons
    open_eye = ctk.CTkImage(Image.open("Images/show_eye.png"))
    closed_eye = ctk.CTkImage(Image.open("Images/hide_eye.png"))
    backbtnicon = Image.open("Images/back.png")
    backbtnicon = backbtnicon.resize((40,40),Image.ANTIALIAS)
    backbtnicon= ImageTk.PhotoImage(backbtnicon)
    #Buttons to return to the chose login screen, signin button and the show password button
    chosescreenbtn = ctk.CTkButton(teachersigninframe,image=backbtnicon,text="",fg_color="white",bg_color="white",hover_color="white",width=50,font=("Arial",20),command=chose_login3)
    chosescreenbtn.place(x=2,y=2)
    signin = ctk.CTkButton(teachersigninframe, text="Sign In",width=400,height=45,bg_color="white",fg_color="#0e6cd9",hover_color="#0e6cd9",text_color="white",font=("Arial",20,"bold"),cursor="hand2",command=clicked)
    signin.place(x=41,y=570)
    showpas = ctk.CTkButton(master=teachersigninframe,text="",height=65,width=14,image=closed_eye, command=show_pass,bg_color="white",fg_color="transparent",hover_color="white")
    showpas.place(x=405,y=481)
    #Contact us hyperlink that links to the schools contact us page
    link = ctk.CTkLabel(teachersigninframe, text="Contact School",text_color="blue", font= ('Arial',15,"underline"), cursor="hand2",bg_color="white",fg_color="white")
    link.place(x=50,y=645)
    link.bind("<Button-1>", lambda e: callback("https://www.gwsc.vic.edu.au/page/186/Contact-Us"))
#reutn to the parent sign in frame and remove all widgets from the booking window
def exitparentview():
    parentbookingframe.forget()
    rootwindow.title("PST Booking System")
    student_sign_in()

#------------------------------------------------------------------Parent Booking page--------------------------------------------------------------------------------------------------------------------------------------------------------#
def parent_booking_screen():
    #adjust window for new frame
    parentbookingframe.pack(fill='both', expand=1)
    studentsigninframe.forget()
    rootwindow.title("PST Booking System - Parent Booking Screen")
    rootwindow.geometry("600x400")
    #define actions for what will happen based of what is chosen in the drop down option menu
    def combobox_callback(choice):
        if choice == "CHILDREN":
            CTkMessagebox(title='The goblin of GWSC', message= f'I hear you want to see your children again')
        elif choice == "BOOKINGS":
            CTkMessagebox(title='The Bookings of GWSC', message= f'You should remember your bookings not make me tell you')
        elif choice == "LOG OUT":
            exitparentview()
        elif choice == "EXIT":
            rootwindow.destroy()
        else:
            CTkMessagebox(title='You are already on your account', message= f'Account already opened')
    combobox = ctk.CTkOptionMenu(parentbookingframe, values=["NAME", "BOOKINGS","CHILDREN","LOG OUT","EXIT"],command=combobox_callback,state="readonly")
    combobox.set("NAME")
    combobox.place(x=460,y=5)
#Remove all widgets from window so it can load the teacher sign in page
def exitteacherview():
    teacherbookedframe.forget()
    rootwindow.title("PST Booking System")
    teacher_sign_in()
#------------------------------------------------------------------Teacher all bookings page--------------------------------------------------------------------------------------------------------------------------------------------------------#
def teacher_booked_screen():
    #adjust window for new frame
    teacherbookedframe.pack(fill='both', expand=1)
    teachersigninframe.forget()
    rootwindow.geometry("815x240")
    rootwindow.title("PST Booking System - Teacher All Bookings")
    #Define and place the side bar that appears after loging in
    sidebar = ctk.CTkFrame(teacherbookedframe,width=200, height=400)
    sidebar.place(x=624,y=-4)
    #Retrieve current year for file download name
    year = datetime.now().strftime("%y")
    year = str(year)
    filename = "PSTbookings_"+year+".csv" #File name will be outputed like "PSTbookings_23.csv" Number will change depending on computers internal calendar
    #save file window pop up asking where to save and what they would like to name it. Default Location: Desktop default name: PSTbookings_{year}.csv
    def file1():
        file = filedialog.asksaveasfile(initialdir="Desktop",initialfile=filename,defaultextension=".csv",filetypes = [("Excel Files", "*.xls *.csv")])
        #open sorted csv to read the bookings within and write them to the file that the file dialog is saving to your computer
        insidefile = open("csv/sortedallbookings.csv")
        text=insidefile.read()
        file.write(text)
        file.close
        #windows notifications indicating that the users download has finished
        toast = Notification(app_id="GWSC PST Booking System", title="Download", msg="Your booking confirmation has finished downloading",duration="short")
        toast.set_audio(audio.Default ,loop=False)
        toast.show()
    #file download button and opening of image. downloadbtn links back to file1 function to trigger the saving of the file
    filedownloadicon = ctk.CTkImage(Image.open("Images/filedownload.png"))
    downloadbtn = ctk.CTkButton(sidebar, text="Download",image=filedownloadicon, font=("Arial",25,"bold"),command=file1)
    downloadbtn.place(x=20,y=80)
    #Create and place treeview onto frame 
    #Treeview shows all bookings for the teacher in accending time order.
    treeviewbookings = ttk.Treeview(teacherbookedframe,columns=("student_name","booking_time","subject"),show="headings")
    treeviewbookings.heading("student_name",text="Student Name")
    treeviewbookings.heading("booking_time",text="Time Booked")
    treeviewbookings.heading("subject",text="Subject")
    treeviewbookings.place(x=5,y=5)
    ctk_textbox_scrollbar = ctk.CTkScrollbar(teacherbookedframe, command=treeviewbookings.yview)
    ctk_textbox_scrollbar.place(x=608,y=25)
    #logout button that returns user to teacher log in frame
    logouticon = ctk.CTkImage(Image.open("Images/logout.png"))
    logoutbtn = ctk.CTkButton(sidebar, text="Logout",width=15,image=logouticon,fg_color="red",hover_color="#e01304",cursor="hand2",command=exitteacherview)
    logoutbtn.place(x=90,y=210)

    #connect textbox scroll event to CTk scrollbar
    treeviewbookings.configure(yscrollcommand=ctk_textbox_scrollbar.set)
    
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
    
    csvfile2 = open("csv/sortedallbookings.csv","w")
# add data to the treeview
    for i in range(len(data)):
        sname = data[i][0]
        stime = data[i][1]
        ssubject = data[i][2]  
        #Converts booking time from 24 hour format back into 12 hour format
        dateTime = datetime.strptime(stime, '%H:%M')
        timein12 = dateTime.strftime('%I:%M %p').lstrip('0')      
        treeviewbookings.insert('', END, values=(sname, timein12, ssubject))
        csvfile2.write(sname+", "+timein12+", "+ssubject+"\n")
    def item_selected(event):
        for selected_item in treeviewbookings.selection():
            item = treeviewbookings.item(selected_item)
            record = item['values']
            record = record
            showinfo(title='Information', message=', '.join(record))


    treeviewbookings.bind('<<TreeviewSelect>>', item_selected)
#call the window to chose login mode
chose_login()
rootwindow.mainloop()
