from tkinter import *

def printt():
    radius=float(r.get())
    a=3.14*radius
    c=2*3.14*radius
    print("Area of circle=\n",a)
    print("Circumfernenceof circle =\n",c)
    print (radius)

def ract():
    radius=float(r.get())
    area=radius*radius
    perimeter=2*(radius+radius)
    print("Area of Rectangle : ",area)
    print("Perimeter of Rectangle : ",perimeter)
    
def triag():
    radius=float(r.get())
    s = (radius + radius + radius) / 2
    # calculate the area
    area = (s*(s-radius)*(s-radius)*(s-radius)) ** 0.5
    print('The area of the triangle is %0.2f' %area)
    
window=Tk()
window.geometry("700x500")
window.title("welcome")



label1=Label(window,text="GEOMETRY",relief="solid",width=20,font=("arial",19,"bold"))
label1.place(x=180,y=53)

label2=Label(window,text="Enter value",width=20,font=("arial",10,"bold"))
label2.place(x=80,y=130)

r = StringVar()
r_entry= Entry(window,textvariable= r,width=20)
r_entry.place(x=200,y=130)

b1=Button(window,text="circle",width=12,bg='brown',fg='white',command=printt)
b1.place(x=150,y=380)

b2=Button(window,text="traingle",width=12,bg='brown',fg='white',command=triag)
b2.place(x=280,y=380)

b3=Button(window,text="ractangle",width=12,bg='brown',fg='white',command=ract)
b3.place(x=400,y=380)
window.mainloop()
