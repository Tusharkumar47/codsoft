import random 
import string

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from PIL import ImageTk, Image


root= Tk()
root.title('codsoft-password generator')

root.geometry("500x360")
root.configure(bg="cornsilk2")

'''co0= "#444466"   # black
co1= "feffff"    # white
co2=  "6f9fbd"   #blue
co3= "f05a43"    #red'''

label=Label(root,text="Password Generator",font="aerial, 25 bold",width=10,bd=5,bg="bisque3",fg="black")
label.pack(side="top",fill=BOTH)
#label.grid(row=0,column=0)

app_line= Label(root,width=10000,height=1,padx=0,anchor="nw",font=('Arial 1'),bg="cornsilk3",fg="cornsilk3")
app_line.place(x=0,y=50)


#function to generate password

def generate_password():
    lower_case_letters= string.ascii_lowercase
    upper_case_letters= string.ascii_uppercase
    number= '123456789'
    symbols= "{}[]()*;/,_-"

    global combine

    if state_1.get()== upper_case_letters:
        combine = lower_case_letters
    else:
        pass
    
    if state_2.get() == lower_case_letters:
        combine += upper_case_letters
    else:
        pass

    if state_3.get() == number:
        combine += number
    else:
        pass

    if state_4.get() == symbols:
        combine +=  symbols
    else:
        pass

    length = int(spin.get())

    password="".join(random.sample(combine,length))
    

    app_password['text'] = password
    #print(password)
    def copy_password():
        info=password
        root.clipboard_clear()
        root.clipboard_append(info)
        messagebox.showinfo("Success","The password has been copied successfully")

    b_copy=Button(root,command=copy_password,text='Copy',width=7,overrelief='solid',bg="bisque3",fg="black",font=('Ivy 10 bold'),anchor="center",relief=RAISED)
    b_copy.place(x=20,y=320)



lower_case_letters= string.ascii_lowercase
upper_case_letters= string.ascii_uppercase
number= '123456789'
symbols= "{}[]()*;/,_-"






var =IntVar()
var.set(8)
app_info=Label(root,text="ENTER THE LENGTH OF THE PASSWORD",font=("Ivy 10 bold"),height=1,padx=0,anchor="nw",bg="bisque3",fg="black")
app_info.place(x=100,y=80)
spin= Spinbox(root,from_=0, to=20,textvariable=var)
spin.place(x=150,y=120)

app_password=Label(root,text="- - -",font=("Ivy 10 bold"),width=20,height=2,relief='solid',padx=0,anchor="center",bg="cornsilk3",fg="black")
app_password.place(x=133,y=150)

#uppercase letters

app_info=Label(root,text="ABC uppercase letters",font=("Ivy 10 bold"),height=0,padx=0,anchor="nw",bg="cornsilk3",fg="black")
app_info.place(x=133,y=200)

state_1=StringVar()
state_1.set(False)

check_1=Checkbutton(root,width=1,var=state_1,onvalue=upper_case_letters,offvalue='off',bg="cornsilk2")
check_1.place(x=100,y=200)

# lower case letters

app_info=Label(root,text="abc lowercase letters",font=("Ivy 10 bold"),height=0,padx=0,anchor="nw",bg="cornsilk3",fg="black")
app_info.place(x=133,y=230)

state_2=StringVar()
state_2.set(False)

check_2=Checkbutton(root,width=1,var=state_2,onvalue=lower_case_letters,offvalue='off',bg="cornsilk2")
check_2.place(x=100,y=230)

#Numbers 

app_info=Label(root,text="123... Numbers",font=("Ivy 10 bold"),height=0,padx=0,anchor="nw",bg="cornsilk3",fg="black")
app_info.place(x=133,y=260)

state_3=StringVar()
state_3.set(False)

check_3=Checkbutton(root,width=1,var=state_3,onvalue=number,offvalue='off',bg="cornsilk2")
check_3.place(x=100,y=260)



#symmbols 

app_info=Label(root,text="@*{}... symbols",font=("Ivy 10 bold"),height=0,padx=0,anchor="nw",bg="cornsilk3",fg="black")
app_info.place(x=133,y=290)

state_4=StringVar()
state_4.set(False)

check_4=Checkbutton(root,width=1,var=state_4,onvalue=symbols,offvalue='off',bg="cornsilk2")
check_4.place(x=100,y=290)

#generate password button

b_generate_password=Button(root,command=generate_password,text='Generate Password',width=55,overrelief='solid',bg="bisque3",fg="black",font=('Ivy 10 bold'),anchor="center",relief=FLAT)
b_generate_password.place(x=20,y=320)









root.mainloop()




