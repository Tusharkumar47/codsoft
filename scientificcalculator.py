import tkinter
import math
import tkinter.messagebox
from tkinter import *
root=Tk()
root.geometry("650x400+300+300")
root.title("TUSHAR SCIENTIFIC CALCULATOR")
switch= None
disp=Entry(root,font="verdana 20",fg="Black",bg="Lightcyan2",bd=4,justify=RIGHT,insertbackground="#abbab1",cursor="arrow")
disp.pack(expand=True,fill=BOTH)
disp.insert(0,'0')

def btn_1():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'1')


def btn_2():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'2')


def btn_3():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'3')


def btn_4():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'4')

def btn_5():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'5')


def btn_6():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'6')


def btn_7():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'7')


def btn_8():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'8')


def btn_9():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'9')

def btn_0():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'0')

def btn_p():
    pos=len(disp.get())
    disp.insert(pos,'+')


def btn_s():
    pos=len(disp.get())
    disp.insert(pos,'-')    


def btn_ml():
    pos=len(disp.get())
    disp.insert(pos,'*')


def btn_di():
    pos=len(disp.get())
    disp.insert(pos,'/')

def sin():
    try:
        ans=float(disp.get())
        if switch==True:
            ans=math.sin(math.radians(ans))
        else:
            ans=math.sin(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error !......")


def sin_clicked():
    try:
        ans=float(disp.get())
        if switch==True:
            ans=math.sin(math.radians(ans))
        else:
            ans=math.sin(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error !......")


def cos_clicked():
    try:
        ans=float(disp.get())
        if switch==True:
            ans=math.cos(math.radians(ans))
        else:
            ans=math.cos(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error !......")


def tan_clicked():
    try:
        ans=float(disp.get())
        if switch==True:
            ans=math.tan(math.radians(ans))
        else:
            ans=math.tan(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error !......")


def arcsin_clicked():
    try:
        ans=float(disp.get())
        if switch==True:
            ans=math.degrees(math.radians(ans))
        else:
            ans=math.asin(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error !......")


def arccos_clicked():
    try:
        ans=float(disp.get())
        if switch==True:
            ans=math.degrees(math.radians(ans))
        else:
            ans=math.acos(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error !......")


def arctan_clicked():
    try:
        ans=float(disp.get())
        if switch==True:
            ans=math.degrees(math.radians(ans))
        else:
            ans=math.atan(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error !......")


def pow_clicked():
    pos=len(disp.get())
    disp.insert(pos,'**')

def dot_clicked():
    pos=len(disp.get())
    disp.insert(pos,'.')

def br_clicked():
    pos=len(disp.get())
    disp.insert(pos,')')

def bl_clicked():
    pos=len(disp.get())
    disp.insert(pos,'(')

def mod_clicked():
    pos=len(disp.get())
    disp.insert(pos,'%')

def cl_clicked():
    pos=len(disp.get())
    display=str(disp.get())
    if display=='':
        disp.insert(0,'0')
    elif display==' ':
        disp.insert(0,'0')
    elif display=='0':
        pass
    else:
        disp.delete(0,END)

def log_clicked():
    try:
        ans=float(disp.get())
        ans=math.log10(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("value error")

def ln_clicked():
    try:
        ans=float(disp.get())
        ans=math.log(ans)
        disp.delete(0,END)
        disp.insert(0,ans)    
    except Exception:
        tkinter.messagebox.showerror("value error") 

def pi_clicked():
    if disp.get()=='0':
        pos=len(disp.get())
        disp.delete(0,END)
        disp.insert(pos,str(math.pi))
    else:
        pos=len(disp.get())
        disp.insert(pos,str(math.pi))

def sqrt_clicked():
    ans=float(disp.get())
    pos=len(disp.get())
    disp.delete(0,END)
    disp.insert(pos,str(math.sqrt(ans)))

def e_clicked():
    if disp.get()=='0':
        disp.delete(0,END)
        pos=len(disp.get())
        disp.insert(pos,str(math.e))
    else:
        pos=len(disp.get())
        disp.insert(pos,math.e)

def fact_clicked():
    try:
        ans=float(disp.get())
        ans=math.factorial(ans)
        disp.delete(0,END)
        #pos=len(disp.get())
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("value error")

def round_clicked():
    ans=float(disp.get())
    ans=round(ans)
    disp.delete(0,END)
    disp.insert(0,str(ans))

def del_clicked():
    pos=len(disp.get())
    display=str(disp.get())
    if display=='':
        disp.insert(0,'0')
    elif display==' ':
        disp.insert(0,'0')
    elif display=='0':
        pass
    else:
        disp.delete(0,END)
        disp.insert(0,display[0:pos-1])

def conv_clicked():
    global switch
    if switch is NONE:
        switch =True
        button_rad["text"]="Deg"
    else:
        switch=None
        button_rad["text"]="Rad"
    
def eq_clicked():
    try:
        ans=disp.get()
        ans=eval(ans)
        disp.delete(0,END)
        disp.insert(0,ans)

    except Exception:
        tkinter.messagebox.showerror("value error !......")

row1=Frame(root,bg="#000000")
row1.pack(expand=TRUE,fill=BOTH)
pibutton=Button(row1,text="π",font="segoe 18",relief=GROOVE,bd=0,command=pi_clicked,fg="white",bg="#333333")
pibutton.pack(side=LEFT,expand=TRUE,fill=BOTH)
factbutton=Button(row1,text=" x!",font="segoe 18",relief=GROOVE,bd=0,command=fact_clicked,fg="white",bg="#333333")
factbutton.pack(side=LEFT,expand=TRUE,fill=BOTH)
sinbutton=Button(row1,text="sin",font="segoe 18",relief=GROOVE,bd=0,command=sin_clicked,fg="white",bg="#333333")
sinbutton.pack(side=LEFT,expand=TRUE,fill=BOTH)
cosbutton=Button(row1,text="cos",font="segoe 18",relief=GROOVE,bd=0,command=cos_clicked,fg="white",bg="#333333")
cosbutton.pack(side=LEFT,expand=TRUE,fill=BOTH)
tanbutton=Button(row1,text="tan",font="segoe 18",relief=GROOVE,bd=0,command=tan_clicked,fg="white",bg="#333333")
tanbutton.pack(side=LEFT,expand=TRUE,fill=BOTH)
button1=Button(row1,text="1",font="segoe 23",relief=GROOVE,bd=0,command=btn_1,fg="white",bg="#333333")
button1.pack(side=LEFT,expand=TRUE,fill=BOTH)
button2=Button(row1,text="2",font="segoe 23",relief=GROOVE,bd=0,command=btn_2,fg="white",bg="#333333")
button2.pack(side=LEFT,expand=TRUE,fill=BOTH)
button3=Button(row1,text="3",font="segoe 23",relief=GROOVE,bd=0,command=btn_3,fg="white",bg="#333333")
button3.pack(side=LEFT,expand=TRUE,fill=BOTH)
#button4=Button(row1,text="4",font="segoe 18",relief=GROOVE,bd=0,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
button_plus=Button(row1,text="+",font="segoe 23",relief=GROOVE,bd=0,command=btn_p,fg="white",bg="#333333")
button_plus.pack(side=LEFT,expand=TRUE,fill=BOTH)
# Row 2 buttons 
row2=Frame(root)
row2.pack(expand=TRUE,fill=BOTH)
button_exp=Button(row2,text="e",font="segoe 18",relief=GROOVE,bd=0,command=e_clicked,fg="white",bg="#333333")
button_exp.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_sqrt=Button(row2,text="√x",font="segoe 18",relief=GROOVE,bd=0,command=sqrt_clicked,fg="white",bg="#333333")
button_sqrt.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_sinh=Button(row2,text="sin-1",font="segoe 11 bold",relief=GROOVE,bd=0,command=arcsin_clicked,fg="white",bg="#333333")
button_sinh.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_cosh=Button(row2,text="cos-1",font="segoe 11 bold",relief=GROOVE,bd=0,command=arccos_clicked,fg="white",bg="#333333")
button_cosh.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_tanh=Button(row2,text="tan-1",font="segoe 11 bold",relief=GROOVE,bd=0,command=arctan_clicked,fg="white",bg="#333333")
button_tanh.pack(side=LEFT,expand=TRUE,fill=BOTH)
button4=Button(row2,text="4",font="segoe 23",relief=GROOVE,bd=0,command=btn_4,fg="white",bg="#333333")
button4.pack(side=LEFT,expand=TRUE,fill=BOTH)
button5=Button(row2,text="5",font="segoe 23",relief=GROOVE,bd=0,command=btn_5,fg="white",bg="#333333")
button5.pack(side=LEFT,expand=TRUE,fill=BOTH)
button6=Button(row2,text="6",font="segoe 23",relief=GROOVE,bd=0,command=btn_6,fg="white",bg="#333333")
button6.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_minus=Button(row2,text="-",font="segoe 23",relief=GROOVE,bd=0,command=btn_s,fg="white",bg="#333333")
button_minus.pack(side=LEFT,expand=TRUE,fill=BOTH)
#row 3 buttons
row3=Frame(root)
row3.pack(expand=TRUE,fill=BOTH)
button_rad=Button(row3,text="Rad",font="segoe 12 bold",relief=GROOVE,bd=0,command=conv_clicked,fg="white",bg="#333333")
button_rad.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_round=Button(row3,text="round",font="segoe 10 bold",relief=GROOVE,bd=0,command=round_clicked,fg="white",bg="#333333")
button_round.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_ln=Button(row3,text="ln",font="segoe 18",relief=GROOVE,bd=0,command=ln_clicked,fg="white",bg="#333333")
button_ln.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_log=Button(row3,text="log",font="segoe 17",relief=GROOVE,bd=0,command=log_clicked,fg="white",bg="#333333")
button_log.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_pow=Button(row3,text="x^y",font="segoe 17",relief=GROOVE,bd=0,command=pow_clicked,fg="white",bg="#333333")
button_pow.pack(side=LEFT,expand=TRUE,fill=BOTH)
button7=Button(row3,text="7",font="segoe 23",relief=GROOVE,bd=0,command=btn_7,fg="white",bg="#333333")
button7.pack(side=LEFT,expand=TRUE,fill=BOTH)
button8=Button(row3,text="8",font="segoe 23",relief=GROOVE,bd=0,command=btn_8,fg="white",bg="#333333")
button8.pack(side=LEFT,expand=TRUE,fill=BOTH)
button9=Button(row3,text="9",font="segoe 23",relief=GROOVE,bd=0,command=btn_9,fg="white",bg="#333333")
button9.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_multiply=Button(row3,text="*",font="segoe 23",relief=GROOVE,bd=0,command=btn_ml,fg="white",bg="#333333")
button_multiply.pack(side=LEFT,expand=TRUE,fill=BOTH)
# row 4 buttons
row4=Frame(root)
row4.pack(expand=TRUE,fill=BOTH)
button_mod=Button(row4,text="%",font="segoe 21",relief=GROOVE,bd=0,command=mod_clicked,fg="white",bg="#333333")
button_mod.pack(side=LEFT,expand=TRUE,fill=BOTH)
bl_btn=Button(row4,text="(",font="segoe 21",relief=GROOVE,bd=0,command=bl_clicked,fg="white",bg="#333333")
bl_btn.pack(side=LEFT,expand=TRUE,fill=BOTH)
br_btn=Button(row4,text=")",font="segoe 21",relief=GROOVE,bd=0,command=br_clicked,fg="white",bg="#333333")
br_btn.pack(side=LEFT,expand=TRUE,fill=BOTH)
dot_button=Button(row4,text=".",font="segoe 21",relief=GROOVE,bd=0,command=dot_clicked,fg="white",bg="#333333")
dot_button.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_c=Button(row4,text="C",font="segoe 23",relief=GROOVE,bd=0,command=cl_clicked,fg="white",bg="#333333")
button_c.pack(side=LEFT,expand=TRUE,fill=BOTH)
del_button=Button(row4,text="⌫",font="segoe 18",relief=GROOVE,bd=0,command=del_clicked,fg="white",bg="#333333")
del_button.pack(side=LEFT,expand=TRUE,fill=BOTH)
button0=Button(row4,text="0",font="segoe 23",relief=GROOVE,bd=0,command=btn_0,fg="white",bg="#333333")
button0.pack(side=LEFT,expand=TRUE,fill=BOTH)
btn_equal=Button(row4,text="=",font="segoe 23",relief=GROOVE,bd=0,command=eq_clicked,fg="white",bg="#333333")
btn_equal.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_division=Button(row4,text="/",font="segoe 23",relief=GROOVE,bd=0,command=btn_di,fg="white",bg="#333333")
button_division.pack(side=LEFT,expand=TRUE,fill=BOTH)
root.mainloop()