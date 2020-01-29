from tkinter import *
from tkinter import messagebox

def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    #age_info = str(age_info)
    print(firstname_info, lastname_info, age_info)

    file = open("user1.txt","a")
    file.write(firstname_info)
    file.write(lastname_info)
    file.write(age_info)
    file.close()
    print("User",firstname_info,"has been registered successfully")
    messagebox.showinfo('Info','User data saved successfully')
    #screen.withdraw()

    firstname_entry.delete(0,END)
    lastname_entry.delete(0,END)
    age_entry.delete(0,END)

screen = Tk()
screen.geometry("500x500")
screen.title("Assignment")
heading = Label(text="Assignment", bg="grey",fg="black")
heading.pack()


def view_info():
   
        
    
    
    screen.withdraw()
    screen1 = Tk()
    configfile = Text(screen1, wrap=WORD, width=45, height=20)
    #filename='/etc/hosts'
    f=open("user1.txt","r")
    configfile.insert(INSERT, f.read())
    #configfile.insert(INSERT,[print (i) for i in f])
    configfile.pack(fill="none",expand=TRUE)
    print("Value are",f.readlines())
    f.close()
    #screen1.filename=filedialog.askopenfilename\(filetypes=(("Python Stuff",".txt"),("all files","*.*")))
    screen1.geometry("500x500")
    screen1.title("Details")
    heading = Label(text="Details", bg="grey",fg="black")
    heading.pack()

    firstname1_text = Label(text ="Firstname")
    lastname1_text = Label(text ="Lastname")
    age1_text = Label(text ="Age")
    firstname1_text.place(x=15,y=70)
    lastname1_text.place(x=15,y=140)
    age1_text.place(x=15,y=210)

    
    
    #screen.draw()


firstname_text = Label(text ="Firstname")
lastname_text = Label(text ="Lastname")
age_text = Label(text ="Age")
firstname_text.place(x=15,y=70)
lastname_text.place(x=15,y=140)
age_text.place(x=15,y=210)

firstname = StringVar()
lastname = StringVar()
age = StringVar()

firstname_entry = Entry(textvariable = firstname, width ="30")
lastname_entry = Entry(textvariable = lastname, width ="30")
age_entry = Entry(textvariable = age, width ="30")


firstname_entry.place(x=15,y=100)
lastname_entry.place(x=15,y=170)
age_entry.place(x=15,y=240)

write = Button(screen,text="Write",width="30",height="2",command= save_info)
write.place(x=15,y=290)
view = Button(screen, text="View",width="30",height="2",command=view_info)
view.place(x=15,y=340)
screen.mainloop()
