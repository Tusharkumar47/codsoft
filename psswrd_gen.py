#from tkinter import *
import random
import string 

'''root =Tk()
root.title('codsoft - password generator')

root.geometry("500x300")'''
def generate_password():
    lower_case_letters= string.ascii_lowercase
    upper_case_letters= string.ascii_uppercase
    number= '123456789'
    symbols= "{}[]()*;/,_-"

    combine= lower_case_letters
    combine+= upper_case_letters
    combine+= number
    combine+=  symbols

    length = int(input("enter the elnth of the password"))

    password="".join(random.sample(combine,length))

    print(password)

generate_password()






#root.mainloop()