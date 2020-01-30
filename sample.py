from tkinter import *

def reverse():
    String = Name.get()
    if len(String) == 0:
        print("Pls input a string :")
        return
    else: 
        print("reversed string:",String[::-1])

def isPalindrome():
    String = Name.get()
    if(String == String[:: - 1]):
     print("This is a Palindrome String")
    else:
     print("This is Not a Palindrome String")

window=Tk()
window.geometry("500x500")
window.title("welcome")
    

label1=Label(window,text="welcome",relief="solid",width=20,font=("arial",19,"bold"))
label1.place(x=90,y=53)

label2=Label(window,text="String :",width=20,font=("arial",10,"bold"))
label2.place(x=80,y=130)

Name = StringVar()
Name_entry= Entry(window,textvariable= Name,width=20)
Name_entry.place(x=200,y=130)

b1=Button(window,text="String",width=12,bg='brown',fg='white',command=reverse)
b1.place(x=150,y=380)


b2=Button(window,text="Palindrome",width=12,bg='brown',fg='white',command=isPalindrome)
b2.place(x=280,y=380)
window.mainloop()