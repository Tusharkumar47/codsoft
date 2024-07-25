import tkinter
from tkinter import *
from tkinter import ttk
import os

class Todo:
    def __init__(self,root):
        self.root=root
        self.root.title("Tushar's To-Do list")
        self.root.geometry("650x410+300+150")
        self.label=Label(self.root,text="TO-Do list app",font="aerial, 25 bold",width=10,bd=5,bg="RosyBrown1",fg="black")
        self.label.pack(side="top",fill=BOTH)

        self.label2=Label(self.root,text="Add task",font="aerial, 18 bold",width=10,bd=5,bg="RosyBrown1",fg="black")
        self.label2.place(x=40,y=54)

        self.label3=Label(self.root,text="Tasks",font="aerial, 18 bold",width=10,bd=5,bg="RosyBrown1",fg="black")
        self.label3.place(x=410,y=54)

        self.main_text=Listbox(self.root,height=8,width=23,bd=5,font="segoe 18 bold",bg="MistyRose2")
        self.main_text.place(x=280,y=100)

        self.text=Text(self.root,bd=5,height=2,width=30,font="aerial, 10 bold",bg="MistyRose2")
        self.text.place(x=20,y=120)


        #***************************====================add task================================**************************

        def add():
            content=self.text.get(1.0,END).strip()
            if content:  # Only add non-empty tasks
                self.main_text.insert(END,content)
                with open("data.txt",'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0,END)

        def delete():
            delete = self.main_text.curselection()
            if delete:
                look = self.main_text.get(delete)
                with open("data.txt",'r+') as file:
                    new_file = file.readlines()
                    file.seek(0)
                    for line in new_file:
                        if line.strip() != look:
                            file.write(line)
                    file.truncate()
                self.main_text.delete(delete)
        
        # Create the data.txt file if it doesn't exist
        if not os.path.exists("data.txt"):
            open("data.txt", 'w').close()

        with open("data.txt",'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.strip()  # Strip any newline characters
                self.main_text.insert(END,ready)
        
        self.button=Button(self.root,text="ADD",font="segoe 18 bold ",width=10,fg="black",bg="LightPink1",command=add)
        self.button.place(x=30,y=180)

        self.button2=Button(self.root,text="DELETE",font="segoe 18  bold ",width=10,fg="black",bg="LightPink1",command=delete)
        self.button2.place(x=30,y=280)


def main():
    root=Tk()
    ui=Todo(root)
    root.mainloop()

if __name__=="__main__":
    main()

